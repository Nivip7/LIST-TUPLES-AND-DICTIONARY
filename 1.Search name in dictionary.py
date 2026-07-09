d={}
n=int(input("enter number of contacts:"))
for i in range(n):
    name=input("enter name:")
    num=input("PHONE NUMBER:")
    d[name]=num
print("TELEPHONE DIRECTORY")
for i in d:
    print(i,";",d[i])
    s=input("enter name to search...")
if s in d:
   print("phone number is...",d[s])
else:
   print("contact not found")
