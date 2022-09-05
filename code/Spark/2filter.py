from  pyspark.sql.functions import lit,substring, col
from pyspark.sql import SparkSession
spark = SparkSession.builder.  \
        master("local").  \
        appName("date_manipulation").  \
        getOrCreate()

# df= spark.read.csv("C:/Users/Ganesh Dabhade/PycharmProjects/pythonProject3/data_files/retail_db/orders/part-00000", schema="""order_id INT, order_date STRING ,
#                                                                     customer_order_id STRING, order_status STRING""")
# df.filter("order_id BETWEEN 2 AND 30 AND order_status IN ('COMPLETE','PROCESSING')").show()
l = [("ram","pawar", 22, "male"),("sana","mulik",23,"female"),
     ("pavan","Yadav",17,"male"),("shreya","pardesi", 18,"female"),
     ("anuj","Yadav",19,"male")]

rdd=spark.sparkContext.parallelize(l);
rdd.foreach()