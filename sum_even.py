#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=4568
#Create a variable "sum_even" and assign it 0.
first=var_int//1000
second=var_int%1000//100
third=var_int%100//10
four=var_int%10
sum_even=((first+1)%2*first+(second+1)%2*second+(third+1)%2*third+(four+1)%2*four)
#Find the sum of the even digits in the variable "var_int".
print(sum_even)