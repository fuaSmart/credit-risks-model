"""PySpark ETL pipeline to process Xente data into Delta Lake."""

from delta.tables import DeltaTable
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("CreditDataPipeline")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .getOrCreate()
)


def process_raw_data():
    """Ingests raw Xente CSV/Parquet and writes processed Delta tables."""
    raw_df = spark.read.csv("data/raw/xente_*.csv", header=True)
    raw_df.write.format("delta").save("data/processed/transactions")
