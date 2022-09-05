from  pyspark.sql.functions import lit,substring, col,filter
from pyspark.sql import SparkSession
spark = SparkSession.builder.  \
        master("local").  \
        appName("date_manipulation").  \
        getOrCreate()

df_file=spark.read.csv("C:/Users/Ganesh Dabhade/PycharmProjects/pythonProject3/data_files/retail_db/orders/part-00000", \
            schema='''
            order_id INT, 
            order_date STRING, 
            order_customer_id INT, 
            order_status STRING
        '''
       )
df_file.show()
df_file.filter("order_id BETWEEN 20 and 50 and order_status in('PENDING','COMPLETE')").show()
df_file.withColumn('or_date',substring(col('order_date'),1,9)).filter("order_id BETWEEN 20 and 50 and order_status in('PENDING','COMPLETE')").show()