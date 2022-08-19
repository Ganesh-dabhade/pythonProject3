from pyspark.sql.functions import col,lit, current_date, current_timestamp,date_add, date_sub,datediff,next_day,add_months
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
df1.withColumn("date_add",date_add(current_date(),5)). \
    withColumn("date_sub",date_sub(current_date(),7)).  \
    withColumn("add_month",add_months(current_date(),3)).show()
Rd=df1.rdd
Rd.count()