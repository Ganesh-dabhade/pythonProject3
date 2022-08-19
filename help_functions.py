import pyspark
from pyspark.sql import SparkSession
spark = SparkSession. \
    builder. \
    master('local'). \
    getOrCreate()
print(spark)
a= spark.createDataFrame(["SAM","JOHN","AND","ROBIN","ANAND"], "string").toDF("Name")
b= spark.createDataFrame(["DAN","JACK","AND"], "string").toDF("Name")
c = a.union(b).show()
