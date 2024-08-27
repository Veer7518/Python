"""def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
'show(n)'
n= int(input("Enter the number:"))
show(n)"""

#2 
def fact(n):
 if (n==1 or n==0):
  return 1
 return(fact(n-1))*n
n= int(input("Enter the number:"))
print(fact(n))

    