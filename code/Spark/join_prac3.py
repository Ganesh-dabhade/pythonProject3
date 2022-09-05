from pyspark.sql.functions import col,substring
from pyspark.sql import SparkSession
spark = SparkSession.builder.  \
        master("local").  \
        appName("date_manipulation").  \
        getOrCreate()

orders=spark.read.csv("C:/Users/Ganesh Dabhade/PycharmProjects/pythonProject3/data_files/retail_db/orders/part-00000", \
            schema='''
            order_id INT, 
            order_date STRING, 
            order_customer_id INT, 
            order_status STRING
        ''')

order_items =spark.read.csv("C:/Users/Ganesh Dabhade/PycharmProjects/pythonProject3/data_files/retail_db/order_items/part-00000", \
                       schema="""
                           order_item_id INT ,
                           order_item_order_id INT,
                           order_item_product_id INT,
                           order_item_quantity INT,
                           order_item_subtotal float,
                           order_item_product_price float
                      """
                       )

orders.join(order_items, on=orders.order_id== order_items.order_item_order_id, how='inner'). \
    withColumn('order_day',substring(col('order_date'),1,10)).groupby('order_day').sum('order_item_subtotal').alias("tatal_revenue"). \
    orderBy('order_day').show()
