from numpy.ma.extras import average


def greehello(name,ending):
    print("hello world "+name)
    print(ending)
print("executing function")
greehello("somya","thankyou")
greehello("shivam","thanks")
print("done")

def lettergenerator(name,date):
    st=f"Hi mam \n this is {name} and i will not come yo school on {date}"
    print(st)

print("executing function")
lettergenerator("somya","5 october")
lettergenerator("rahul","26 october")
print("done")


def average(a,b):
    return(a+b)/2
print("printing average")
print(average(3,5))