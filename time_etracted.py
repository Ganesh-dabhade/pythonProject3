from pyspark.sql.functions import year, month, weekofyear,hour,dayofmonth,dayofyear,second,current_date
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
df1.withColumn("year", year(current_date())). \
    withColumn("month", month(current_date())). \
    withColumn("weekof year", weekofyear(current_date())). \
    withColumn("day_year", dayofyear(current_date())).show()