from pyspark.sql.functions import ltrim, rtrim, trim, lpad, rpad, col
from pyspark.sql import SparkSession
spark= SparkSession.builder.  \
    master("local").  \
    appName("trim_pad"). \
    getOrCreate()


l = [("     halloo   " , )]

df=spark.createDataFrame(l,schema= "char STRING")
#df.select(ltrim(col("char").alias("trim"))).show()
df.withColumn("ltrim", ltrim(col("char"))). \
    withColumn("rtrim",rtrim(col("char"))).  \
    withColumn("lpad", lpad(col("char"),20,"_")).  \
    show()