#Declare a=60 , b=13 and  perform all the bitwise 
#operation where c will be storing the result on the interpreter showing the output.
#  AND ,OR & NOT Operator 
a = 60
b = 13
c = 0

c = a&b
print("a and b is:",c)
c = a|b
print("a or b is:",c)
c =a^b
print("a XOR b is:",c)
c =a<<2
print("a left shift is:",c)
c = a>>2
print("a right shift is:",c)

Output:
     a and b is: 12
     a or b is: 61
     a XOR b is: 49
     a left shift is: 240
     a right shift is: 15
