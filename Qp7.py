"""with open("veer.txt","w") as f:
    f.write("Hii Veer \n i am well\n")
    f.write("and who are you \n also good"\n)
    f.write("Where are you from\n I am from uttar pardesh")"""
    

"""#Q2 replase
with open("veer.txt","r") as f:
    data= f.read()
new_data= data.replace("well","bed")
print(new_data)
with open("veer.txt","w") as f:
    f.write(new_data)"""


def check_for_word():
   word = "pardesh"
   with open("veer.txt","r") as f:
    data=f.read()
    if(word in data):
        print("founds")
    else:
     print("not found")
#Q3

   
def check_for_line():
    word = "pardesh"  # Specify the word you are searching for
    line_no = 1
    with open("veer.txt", "r") as f:
        for line in f:
            if word in line:
                print(f"Word found at line {line_no}")
                return line_no
            line_no += 1
    return -1

print(check_for_line())


    
     
