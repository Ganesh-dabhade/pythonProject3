from pyspark.sql.functions import window

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
#orders.show()
#order_items.show()
orders.join(
    order_items, on=orders.order_id ==order_items.order_item_order_id,
    how="right"
).select('order_id','order_status','order_item_subtotal').groupby('order_id').max('order_item_subtotal'). \
    orderBy('max(order_item_subtotal)').show()



