import logging
import pandas as pd
from sqlalchemy import create_engine
from Ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def create_vendor_summary(engine):
    vendor_sales_summary = pd.read_sql_query("""
    WITH FreightSummary AS (
        SELECT vendornumber, SUM(freight) AS "FreightCost"
        FROM vendor_invoice
        GROUP BY vendornumber
    ),
    PurchaseSummary AS (
        SELECT
            p."VendorNumber",
            p."VendorName",
            p."Brand",
            p."PurchasePrice",
            pp."Volume",
            pp."Price" AS "ActualPrice",
            SUM(p."Quantity") AS "TotalPurchaseQuantity",
            SUM(p."Dollars") AS "TotalPurchaseDollars"
        FROM purchases AS p
        JOIN purchase_prices AS pp
            ON p."Brand" = pp."Brand"
           AND p."VendorNumber" = pp."VendorNumber"
        WHERE p."PurchasePrice" > 0
        GROUP BY p."VendorNumber", p."VendorName", p."Brand",
                 p."PurchasePrice", pp."Volume", pp."Price"
    ),
    SalesSummary AS (
        SELECT
            vendorno,
            brand,
            SUM(salesdollars) AS "TotalSalesDollars",
            SUM(SalesPrice) AS "TotalSalesPrice",
            SUM(SalesQuantity) AS "TotalSalesQuantity",
            SUM(Excisetax) AS "TotalExciseTax"
        FROM sales
        GROUP BY vendorno, brand
    )
    SELECT
        ps."VendorNumber",
        ps."VendorName",
        ps."Brand",
        ps."PurchasePrice",
        ps."ActualPrice",
        ps."Volume",
        ps."TotalPurchaseQuantity",
        ps."TotalPurchaseDollars",
        ss."TotalSalesQuantity",
        ss."TotalSalesDollars",
        ss."TotalSalesPrice",
        ss."TotalExciseTax",
        fs."FreightCost"
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps."VendorNumber" = ss.vendorno
        AND ps."Brand" = ss.brand
    LEFT JOIN FreightSummary fs
        ON ps."VendorNumber" = fs.vendornumber
    ORDER BY ps."TotalPurchaseDollars" DESC
    """, engine)
    return vendor_sales_summary


def clean_data(df):
    df['Volume'] = df['Volume'].astype('float64')
    df.fillna(0, inplace=True)
    df['VendorName'] = df['VendorName'].str.strip()
    df['Gross Profit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['Profit Margin (%)'] = (
        df['Gross Profit'] / df['TotalSalesDollars']
    ) * 100
    df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['SalestoPurchaseratio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars']
    return df


if __name__ == '__main__':
    engine = create_engine("postgresql+psycopg2://postgres:Abhi%40123@localhost:5432/inventory")
    logging.info('Creating Vendor Summary table....')

    summary_df = create_vendor_summary(engine)
    clean_df = clean_data(summary_df)

    logging.info(clean_df.head().to_string())
    logging.info('Ingesting data')

    ingest_db(clean_df, 'vendor_sales_summary', engine)
    logging.info('Completed')