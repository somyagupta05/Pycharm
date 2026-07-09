# s="i am good"

# writing to a file
# with open("test.txt ","w") as f:
#     f.write(s)

# another long way
# fp=open("test.txt","w")
# fp.write(s)
# fp.close()

# reading a file

# with open("som.txt","r") as f:
#     s=f.read()
#     print(s)

#appending to a file
with open("som.txt","a") as f:
    f.write("hello appened")


