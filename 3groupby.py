from pyspark.sql.functions import col,lit, upper, lower, concat
from pyspark.sql import SparkSession
spark = SparkSession.builder. \
        master("local").  \
        appName("practical2").  \
        getOrCreate()

l = [("ram","pawar", 22, "male"),("sana","mulik",23,"female"),
     ("pavan","Yadav",17,"male"),("shreya","pardesi", 18,"female"),
     ("anuj","Yadav",19,"male")]

df1=spark.createDataFrame(l,schema ="""std_fName STRING,std_lName STRING,
                                        std_Age INT, Gender STRING""")

df1.groupby("Gender").count().show()
df1.orderBy("std_Age").show()
df1.orderBy(col("std_Age").desc()).show()
df1.groupby("Gender").count().orderBy(col("count").desc()).show()
df1.withColumn("full_name", concat(col("std_fName"),lit(" "), col("std_lName"))).show()

