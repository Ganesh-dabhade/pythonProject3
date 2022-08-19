from pyspark.sql.functions import col, substring, lit, explode,split
from pyspark.sql import SparkSession

spark = SparkSession.builder.  \
        appName("substring").  \
        master("local").  \
        getOrCreate()

employees = [(1, "Scott", "Tiger", 1000.0,
                      "united states", "+1 123 456 7890", "123 45 6789"
                     ),
                     (2, "Henry", "Ford", 1250.0,
                      "India", "+91 234 567 8901", "456 78 9123"
                     ),
                     (3, "Nick", "Junior", 750.0,
                      "united KINGDOM", "+44 111 111 1111", "222 33 4444"
                     ),
                     (4, "Bill", "Gomes", 1500.0,
                      "AUSTRALIA", "+61 987 654 3210", "789 12 6118"
                     )
                ]
employeesDF = spark. \
    createDataFrame(employees,
                    schema="""employee_id INT, first_name STRING, 
                    last_name STRING, salary FLOAT, nationality STRING,
                    phone_number STRING, ssn STRING"""
                   )

employeesDF.show()
employeesDF.withColumn("ois_id",substring(col("phone_number"),0,5)).show()
employeesDF.withColumn("Id", split("ssn"," ")[1]).orderBy(col("Id").desc()).show()