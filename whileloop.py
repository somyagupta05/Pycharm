i=0
while i<10:
    print(i)
    i=i+1

print("End of loop")

# infinite loop
# while(True):
#     print("not finished")

while(True):
    number=int(input("Enter a number"))
    print(number)
    if(number==0):
        break
print("End of loop")