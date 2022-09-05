import pyspark
from pyspark.sql import SparkSession
spark = SparkSession. \
    builder. \
    master('local'). \
    getOrCreate()
print(spark)
df_file=spark.read.csv("C:/Users/Ganesh Dabhade/PycharmProjects/pythonProject3/data_files/retail_db/orders/part-00000", \
            schema='''
            order_id INT, 
            order_date STRING, 
            order_customer_id INT, 
            order_status STRING
        '''
       )
df_info=spark.read.csv("C:\Users\Ganesh Dabhade\PycharmProjects\pythonProject3\data_files\informations.csv", \
                       header=True, inferSchema=True
                    )
df_file.show()
help(spark.read.csv)
#df_file.show()
#df2=df_file.rdd.map(lambda x: x)
#df2=df_file.rdd.reduce(lambda x:x)
#print(df2.count())
#df3=df2.collect()
#for i in df3:
 #       print(i)





