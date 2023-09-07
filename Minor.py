class Classroom(object):                    # Creating a class to access the attributes using students as objects
    def __init__(self):
        self.Name = ""
        self.First = 0
        self.Second = 0
        self.Math= 0
        self.Science = 0
        self.Social = 0
        self.Total = 0

dict_Students = {}                          # Creating a dictionary to store the objects as values

print("\n")
Class = input("Enter Class: ")
n =int(input("Enter total number of students: "))

i = -1                                      # Initializing loop counter as i = -1 and decrementing n 
n -=1                                       # because of the continue keyword used in lines 35, 44, 53, 62, 71
while(i<n):
    i+=1                                    # Incrementing i because of decrement in lines 34, 43, 52, 61, 70
    print("\n")
    print("Getting the details of student",i+1)
    print("- - - - - - - - - - - - - - - - - - - - - -")
    dict_Students[i] = Classroom()                                                 # Using the value of i as keys and objects as values
    dict_Students[i].Name = input("Enter the name of the student:  ")               # Accessing the class attributes and storing values from input

    F = int(input("Enter the First Language marks of the student (0-100):  "))
    if(0<F<100):                                                                   # If condition to store the value only between (0-100)
        dict_Students[i].First = F
    else:
        print("\n")
        print("!!! Please enter a number between 0 to 100 !!!")                
        i-=1                                                                       # Decrementing i to match the index
        continue                                                                   # Continue keyword to repeat the loop

    S = int(input("Enter the Second Language marks of the student (0-100):  "))   
    if(0<S<100):
        dict_Students[i].Second = S
    else:
        print("\n")
        print("!!! Please enter a number between 0 to 100 !!!")
        i-=1
        continue
                
    M = int(input("Enter the mathematics marks of the student (0-100):  "))
    if(0<M<100):
        dict_Students[i].Mathematics = M
    else:
        print("\n")
        print("!!! Please enter a number between 0 to 100 !!!")
        i-=1
        continue
                
    Sc = int(input("Enter the Science marks of the student (0-100):  "))
    if(0<Sc<100):    
        dict_Students[i].Science = Sc
    else:
        print("\n")
        print("!!! Please enter a number between 0 to 100 !!!")
        i-=1
        continue
                       
    So = int(input("Enter the Social marks of the student (0-100):  ")) 
    if(0<So<100):   
        dict_Students[i].Social = So
    else:
        print("\n")
        print("!!! Please enter a number between 0 to 100 !!!")
        i-=1
        continue

    To =  dict_Students[i].First+dict_Students[i].Second+dict_Students[i].Mathematics+dict_Students[i].Science+dict_Students[i].Social          
    dict_Students[i].Total = To

n+=1                   # Incrementing n because of decrement in line 18
print("\n")
print("- - - - - - - Evaluating the results - - - - - - -")
print("\n")

def sort_dict(sorted_dict,dict):                              # Defining a function to sort the elements of dict_Students = {}
                                                              # and store them in a new dictionary
    Result_list = []                                                    
    for j in range(n):
        Result_list.append(dict[j].Total)                     # Storing the values of dict_Students[i].Total into a list Result_list = []

    final_list = []
    final_list = Result_list.copy()                           # Sorting the elements of Result_list = [] in
    final_list.sort(reverse=True)                             # new list final_list = []
    
    for k in range(n):
        dict_key = Result_list.index(final_list[k])           # Index of final_list values in Result_list
        sorted_dict[k] = dict[dict_key]                       # Storing the sorted elements in the new dictionary

Final_dict = {}                                               # New dictionary       
sort_dict(Final_dict,dict_Students)


printscreen = input("Do you want to print results on the screen ? (y/n) ")
printscreen.lower()
if(printscreen == 'y'):
    print("\n")
    print("Students' results of class: ",Class)
    print("- - - - - - - - - - - - - - - - - - - - - -")
    for l in Final_dict:
        roll = l+1
        print("\n")
        print("Roll no: ",roll)
        print("- - - - - - - - -")
        print("Name of the Student: ",Final_dict[l].Name)     # Printing the values of the attributes for the objects in dictionary Final_dict = {}
        print("First Language Marks: ",Final_dict[l].First)
        print("Second Language Marks: ",Final_dict[l].Second)
        print("Mathematics Marks: ",Final_dict[l].Mathematics)
        print("Science Marks: ",Final_dict[l].Science)
        print("Social Marks: ",Final_dict[l].Social)
        print("Total Marks: ",Final_dict[l].Total)


print("\n")
printdoc = input("Do you want to print results in the Result.txt file ? (y/n) ")
if(printdoc=='y'):
    document = open('Result.txt','w')                         # Opening a .txt file to write the outputs

    document.writelines("\n")
    document.writelines("Students' results of class: ")
    document.write(str(Class))
    document.writelines("\n")
    document.writelines("- - - - - - - - - - - - - - - - - - - - - -")
    document.writelines("\n")
    for m in Final_dict:
        roll = m+1
        document.writelines("\n")
        document.writelines("Roll no: ")
        document.write(str(roll))
        document.writelines("\n")
        document.writelines("- - - - - - - - -")
        document.writelines("\n")
        document.writelines("Name of the Student: ")
        document.write(str(Final_dict[m].Name))
        document.writelines("\n")
        document.writelines("First Language Marks: ")       # Writing the values of the attributes for
        document.write(str(Final_dict[m].First))            # the objects of dictionary Final_dict = {} 
        document.writelines("\n")                           # in the Result.txt file 
        document.writelines("Second Language Marks: ")
        document.write(str(Final_dict[m].Second))
        document.writelines("\n")
        document.writelines("Mathematics Marks: ")
        document.write(str(Final_dict[m].Mathematics))
        document.writelines("\n")
        document.writelines("Science Marks: ")
        document.write(str(Final_dict[m].Science))
        document.writelines("\n")
        document.writelines("Social Marks: ")
        document.write(str(Final_dict[m].Social))
        document.writelines("\n")
        document.writelines("Total Marks: ")
        document.write(str(Final_dict[m].Total))
        document.writelines("\n")
    document.close()                                        # Closing the Result.txt file
    print("\n")
    print("- - - - - - - - - Thank You - - - - - - - - - - -")
    print("\n")
else:
    print("\n")
    print("- - - - - - - - - Thank You - - - - - - - - - - -")
    print("\n")