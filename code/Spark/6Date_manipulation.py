from pyspark.sql.functions import col,lit, current_date, current_timestamp, to_date, to_timestamp
from pyspark.sql import SparkSession

spark = SparkSession.builder.  \
        master("local").  \
        appName("date_manipulation").  \
        getOrCreate()

l = [("ram","pawar", 22, "male"),("sana","mulik",23,"female"),
     ("pavan","Yadav",17,"male"),("shreya","pardesi", 18,"female"),
     ("anuj","Yadav",19,"male")]

df1=spark.createDataFrame(l,schema ="""std_fName STRING,std_lName STRING,
                                        std_Age INT, Gender STRING""")

df1.select(current_date().alias("date"),current_timestamp().alias("timestamp")).show()
df1.select(to_date(lit("2022-04-13"),"yyyy-MM-dd").alias("DATE")).show()