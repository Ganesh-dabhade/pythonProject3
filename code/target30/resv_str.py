Name=input("enter string")
# reverse string using for loop
def rev_str(s):
    rstr=" "
    for i in s:
        rstr=i + rstr # logic concat string s+rstr =s, h+rstr=hs,...> mahs when name=sham

    return rstr

print("using for loop :" + rev_str(Name))

#revrse string using slice operator

name = Name[ : :-1] # slice operator [start : end : step] bydefult [0:len(str):1] and python has negative indexing.
print("using slice operator :" + name)

# using revrse function

print(list(reversed(Name))) # reversed function return reverse list of string element.

refun="".join(reversed(Name)) # join fun. is used for
print("using revrse function :" +refun)