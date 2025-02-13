
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    hour,
    col, 
    count,
    when,
    first,
    format_string
)
from pyspark.sql.window import Window
import pyspark.sql.functions as F

spark = SparkSession.builder.appName("Taxi task 4").getOrCreate()
spark.setLogLevel("DEBUG")

account_file = "newsdata/accounts.csv"
comfort_file = "newsdata/comfort_care.csv"
wide_vital_file = "newsdata/vitals_wide.xlsx"

accounts = spark.read.csv(account_file, header=True, inferSchema=True)
wide_vital_file = spark.read.excel(wide_vital_file, header=True, inferSchema=True)



data = data.filter(col("trip_distance") > 2)

brooklyn_zones = zone_map.filter(col("Borough") == "Brooklyn")

# join
hourly_pickups = (
    data
    .withColumn("hour", hour("tpep_pickup_datetime"))
    .join(brooklyn_zones, col("PULocationID") == col("LocationID"))
    .groupBy("hour", "Zone")
    .agg(count("*").alias("pickups"))
)

# window function to find pickups in each hour ordered by pickups
window = Window.partitionBy("hour").orderBy(col("pickups").desc(), col("Zone"))
