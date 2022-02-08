##var="india is rich history"
##for x in var:
##    if x=="i":
##        print(x,"hello")
##        elif x=="z":
##            print(x,"hi")
##            break
##        else:
##            print("else for loop")



##for x in range(10):
##    print(x)

##for x in range(2,10):
##    print(x)

##for x in range(0,10,2):
##    print(x)

##for x in range(1,10,2):
##    print(x)

##for x in range(10):
##    if x%2==0:
##        print(x)

##for x in range(10,1,-5):
##    print(x)

##var="dhoni"
##for x in var:
##    var="dhoniDHONI"
##    print(var)
##

##var={"name":"dhoni","age":33}
##for x in var.iteams():
##    print(x)

##my_list=[]
##for x in range(10):
##    if x%2==0:
##        my_list.append(x)
##        print(my_list)

##my_list=[x for x in range(10) if x%2==0]
##print(my_list)
##

##output={}
##for x in range(5):
##    output[x]=x*x
##    print(output)

##out={x:x* x for x in range(5)}
##print(output)
##
##var=["a","b","c"]
##new=[]
##for x in var:
##    output=x.upper()
##    new.append(output)
##print(new)

##var="abc"
##for x in var:
##    var=var+x.upper()
##    print(var)
##

##var=["a" ,"b","c"]
##for x in  range(len(var)):
##    output=var[x].upper()
##    var.append(output)
##    print(var)
##
##
##


##var=[x+4 if x%2==0 else x+2 for x in range(10)]
##print(var)
##

##def reverse_string(str):
##    str1="dhoni"
##    for i in str:
##        str1=i+str1
##        return str1
##    var=["dhoni","kohli","ashwin",4,5,3,1,2]
##    print(var)
##    print(var)
    
##var=["dhoni"]
##var.reverse()
##print(var)

##def reverse_str(s):
##    str=""
##    for x in s:
##        str=x+str
##    return str
##s=["dhoni","kohli","ashwin","4","5","3","1","2"]
##print("The original string is:",s)
##print("The reverse string is:",reverse_str(s))
##
##

##
##
##
##
##var=["dhoni","ind","cat","buffalo","an"]
##longest_string=max(var,key=len)
##print(longest_string)
##
##
##
##var={"name":"dhoni","age":33,"team":"india","country":"australia"}
##output=sorted(var.items())
##print(output)

##def mars_funcion(name,country):
##    if isinstance(name,str)and isinstance(country,str):
##        print("hello",name,"from",country)
##        print("welcome to hdfc")
##
##mars_funcion(country="india",name="kohli")
##

##var=100
##def fun():
##    global var
##    var=10
##    print(var)
##print(var)
##fun()


##var=100
##def fun():
##    var=10
##    print(var)
##print(var)
##fun()
##print(var)
##

##var=100
##def fun():
##    print(var)
##print(var)
##fun()
##print(var)

##var=1000
##def fun():
##    
##    var=100
##def new():
##        var=10
##        print(var)
##        new()
##        fun()

##def fun ():
##    print("hello\n"*100)
##    fun()
##fun()


##var=[2,4,6,8]
##def double(x):
##    return x*x
##output=list(map(double,var))
##print(output)

def myfunc(text, num):
    while num > 0:
        print(text)
        num = num - 1

myfunc('Hello', 4)

















































