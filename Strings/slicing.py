## String slicing 
String ='ASTRING'
  
# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2) 
s3 = slice(-1, -12, -2)
  
print("String slicing") 
print(String[s1]) 
print(String[s2]) 
print(String[s3])
  
# Using extended indexing 
print(String[:3])
print(String[1:5:2])
print(String[-1:-12:-2])
  
# Prints string in reverse 
print("\nReverse String")
print(String[::-1])