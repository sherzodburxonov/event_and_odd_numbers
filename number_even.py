#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
a=1234
#Print the number of even digits in the variable "var_int".
first=a//1000
second=a%1000//100
third=a%100//10
four=a%10
print((first+1)%2+(second+1)%2+(third+1)%2+(four+1)%2)
