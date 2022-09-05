from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local").appName("my_app").  \
    getOrCreate()

employees = [(1, "Scott", "Tiger", 1000.0, "united states"),
             (2, "Henry", "Ford", 1250.0, "India"),
             (3, "Nick", "Junior", 750.0, "united KINGDOM"),
             (4, "Bill", "Gomes", 1500.0, "AUSTRALIA")
            ]
print(employees)
df1=spark.createDataFrame(employees,
                          schema="""employee_id INT, first_name STRING, 
                    last_name STRING, salary FLOAT, nationality STRING""")

df1.show()
df1. \
    select("first_name", "last_name"). \
    show()
l=[1,2,4,5,6,7]

rd=spark.sparkContext.parallelize()
