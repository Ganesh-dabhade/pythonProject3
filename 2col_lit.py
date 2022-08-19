from pyspark.sql.functions import col,lit, upper, lower
from pyspark.sql import SparkSession
spark = SparkSession.builder. \
        master("local").  \
        appName("practical2").  \
        getOrCreate()

l = [("ram","pawar", 13, "male"),("sana","mulik",23,"female"),("pavan","Yadav",17,"male"),("shreya","pardesi", 18,"female")]

df1=spark.createDataFrame(l,schema ="""std_fName STRING,std_lName STRING,
                                        std_Age INT, Gender STRING""")
df1.show()
df1.groupby("Gender").count().show()
df1.orderBy("std_Age").show()
df1.select(upper(col("std_fName")),lower(col("std_lName")),"std_Age", upper(col("Gender"))).show()
