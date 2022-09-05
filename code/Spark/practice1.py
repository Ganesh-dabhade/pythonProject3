from pyspark.sql.functions import date_format
from pyspark.sql import SparkSession
spark = SparkSession.builder. \
                     appName("App name"). \
                     master("local"). \
                     getOrCreate()
print(spark)
Df=spark.read.csv("data_files/retail_db/orders/part-00000",
    schema='order_id INT, order_date STRING, order_customer_id INT, order_status STRING')
#Df.show()
#Df.select('order_id',date_format('order_date', 'yyyyMM').alias("Date")).show()
Df.withColumn("Date", date_format("order_date", 'yyyyMM')).select('order_id',("order_customer_id")).show()

Df.filter("order_id >=30").show()
#Df.filter(Df['order_status'] == "COMPLETE").show()