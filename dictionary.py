a={}
b=set()
print(a,type(a))
print(b,type(b))

dict1={"good":"something pleasant","fetch":"to brong"}
print(dict1["good"])

marks={"rahul":34,"somya":99,"shivani":56,"naina":85}
print(marks["rahul"])
# to add
marks["priyanak"]=34
print(marks)

# will give none even if no priyanka chopra it will not give error
print(marks.get("priyanka chopra"))
# this will give error
# print(marks["priyanka chopra"])

print(marks.keys())
print(marks.values())