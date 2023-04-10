#A four-digit integer is given. Find the number of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=7874
#Print the number of odd digits in the variable "var_int".
first=var_int//1000
second=var_int%1000//100
third=var_int%100//10
four=var_int%10
print((first)%2+(second)%2+(third)%2+(four)%2)