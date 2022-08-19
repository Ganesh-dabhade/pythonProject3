import pyspark
from pyspark.sql.functions import lit, concat,col
from pyspark.sql import SparkSession
spark = SparkSession. \
    builder. \
    master('local'). \
    getOrCreate()
print(spark)

employees = [(1, "Scott", "Tiger", 1000.0, "united states"),
             (2, "Henry", "Ford", 1250.0, "India"),
             (3, "Nick", "Junior", 750.0, "united KINGDOM"),
             (4, "Bill", "Gomes", 1500.0, "AUSTRALIA")
            ]
employeesDF = spark. \
    createDataFrame(employees,
                    schema="""employee_id INT, first_name STRING, 
                    last_name STRING, salary FLOAT, nationality STRING"""
                   )

employeesDF.show()
#Read schema of DF
employeesDF.printSchema()
#  change Datatype using withColumn function
employeesDF1=employeesDF.withColumn("salary",col("salary").cast("Integer"))

employeesDF1.printSchema()
employeesDF1.show()
# change value of columns
employeesDF1.withColumn("salary",col("salary")*12).show()
#Give dewali bonus o
employeesDF1.withColumn("Bonus",col("salary")*12*30/100).show()
