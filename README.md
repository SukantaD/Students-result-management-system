# Students-result-management-system
Python program to store the marks obtained  in different subjects and print result after calculating the total marks of some students  in a class.

Explanation:
To begin with the solution, I have created a class Classroom() because using a class I 
can make objects as students. Multiple objects can be made to access the same 
attributes for some students. 
After that I have created a dictionary dict_Students{} to store the objects as values. So 
that the objects can be accessed later easily. The loop counter was used as keys later 
in the loop. The dictionary was chosen because I tried with a list first but it did not 
work.
After that the while loop has been used to store the objects and to access the attributes 
using those objects. The loop counter is used to store the keys in the dictionary. In the 
loop there are some if-else statements used. The if conditions are used for to take 
integer between 0 to 100 as inputs. When the else block gets executed the continue 
keyword is executed and the loop will repeat from the beginning. So, the value of i is 
decremented and incremented in the next iteration. Initially, the value of i and the 
value of n was decremented earlier to match with the dict_Students{} keys. At the end 
of the loop the values are added and the total marks get stored in the self.Total 
attribute. Later the value of n is incremented to preserve the range of the loops.
Now this part was the hardest to implement and challenging to find a solution to sort 
the dictionary. The sort_dict(sorted_dict,dict) function was defined. This function takes 
two dictionaries as arguments one will be the sorted dictionary and the other one is 
the dictionary that is to be sorted. In that function I have created Result_list=[]. This 
list is used to store the value of self.Total for different objects of the dictionary. Using 
a for loop I have stored them. This list has the same indexes as the keys of the 
dictionary. Then a copy of that list is made using list.copy() function as final_list=[]. The 
list.sort(reverse=Ture) function is used on this list to sort the values in a descending 
order. Now the Total marks have been sorted, I had to store the objects into a new 
dictionary depending on those values. For that another for loop was created. In that 
loop I obtained the indexes of the Result_list=[] matching the value of final_list=[] in a 
regular manner. 
Used those indexes for the keys of a new dictionary and obtained the values from the 
dict_Student{} and stored in the new dictionary that is Final_dict{}.
Now the sorted dictionary has been made, I wanted to print the results. So, I took input 
from the user to know if they want to see the results on screen. Meeting the condition 
of the if statement the results are printed on the screen using a for loop. The results 
are printed according to the objects stored in the Final_dict{} in a regular manner.
After that I wanted to make a Result.txt file storing the result instead of printing them 
on screen. For that I have used File handling method. Meeting the condition of the if 
statement, document=open(‘Result.txt’,’w’) is executed to create or open the .txt file. 
Then all the values in the Final_dict{} will get printed in a .txt file named Result.txt using 
the file.writelines() function. At last the file will be closed using document.close() 
function.
Finally, a “Thank You” messege will be printed to let the user know that the program 
has executed successfully.

Conclusion:
Giving the valid inputs to the program it returns the correct outputs. The invalid inputs 
are returning the outputs as expected. A Type error can occur if done intentionally. The 
program is exited immediately when it occurs. But that can be solved using Exception 
handling in the program. So far, the program is running properly and giving us the 
outputs as expected and can be used to solve a daily life problem
