import pyspark
from pyspark.sql import SparkSession
spark = SparkSession. \
    builder. \
    master('local'). \
    getOrCreate()
print(spark)
df_info=spark.read.csv("C:/Users/Ganesh Dabhade/PycharmProjects/pythonProject3/data_files/informations.csv",
                       header=True, inferSchema=True
                     )
df_info.printSchema()
# print(df_info.count())
#df_info.show()
sc=spark.sparkContext
sc.setLogLevel("INFO")