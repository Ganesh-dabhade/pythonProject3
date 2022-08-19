from pyspark.sql import SparkSession
spark=SparkSession.builder.master('local').appName("ABC").getOrCreate()
print(spark)