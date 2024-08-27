""""def cul_sum(n):
    if(n==0):
      return 0
    return cul_sum(n-1)+n

print(cul_sum(5))"""

    #2

def print_list(list, idx=0):
   if (idx== len(list)):
      return 
   print(list,[idx])
   print_list (list,idx+1)
fruits = ["mamgo","banana","litchi","apple"]
print_list(fruits)

      
   