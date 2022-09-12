import  pandas as pd
l=[(1,"ram"),(2,"sham"),(3, "pavan"),(4, "aman")]

column=["id","name"]

DF=pd.DataFrame(l, columns=column)
print(DF.reindex([3,4,1,2]))

ind=["name","id"]

print(DF.reindex([ind], axis="columns"))



