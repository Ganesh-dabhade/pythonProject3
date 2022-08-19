from  pyspark.sql.functions import lit,substring, col
from pyspark.sql import SparkSession
spark = SparkSession.builder.  \
        master("local").  \
        appName("date_manipulation").  \
        getOrCreate()

df= spark.read.csv("C:/Users/Ganesh Dabhade/PycharmProjects/pythonProject3/data_files/retail_db/orders/part-00000", schema="""order_id INT, order_date STRING ,
                                                                    customer_order_id STRING, order_status STRING""")
df.filter("order_status = 'COMPLETE'").show()
df.filter(df["order_status"] == 'COMPLETE').show()
#df.select(substring(col("order_date"),9,2)).show()
df.filter(substring(col("order_date"),9,2)== 25).show()