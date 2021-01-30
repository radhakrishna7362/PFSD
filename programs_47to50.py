# Program 47
"""
test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
  
res = [] 
for i in test_list: 
    if i not in res: 
        res.append(i) 
  
print(res)
"""

# Program 48
"""
arr = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]

elements_count = {}

for element in arr:
   if element in elements_count:
      elements_count[element] += 1
   else:
      elements_count[element] = 1
for key, value in elements_count.items():
   print(f"{key}: {value}")
"""

# Program 49
"""
vcount = 0;  
ccount = 0;  
str = "This is a really simple sentence";  
     
str = str.lower();  
for i in range(0,len(str)):    
    if str[i] in ('a',"e","i","o","u"):  
        vcount = vcount + 1;  
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        ccount = ccount + 1;  
print("Total number of vowel and consonant are" );  
print(vcount);  
print(ccount)
"""

# Program 50
"""
def rem_vowel(string): 
    vowels = ('a', 'e', 'i', 'o', 'u')  
    for x in string.lower(): 
        if x in vowels: 
            string = string.replace(x, "")  
    print(string) 
  

string = "A Computer Science Portal"
rem_vowel(string)
"""
