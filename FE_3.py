# Final Exam - Question#3 (7 pts)
# - Implement 2 recursive function, findOccurrencesR(), and str_to_num(), in FE_3.py
# -++ findOccurrencesR() - (3pts)
# -++ str_to_num() - (4pts)
# - In FE_3.py, it has "TODO" comment, which require you to complete it.
# - Detailed description of findOccurrencesR() is in FE_3.py
# - Please submit ONLY FE_3.py
# - Hint: find() method from string.  
# - Expected output is also defined as comment in FE_3.py


##
# findOccurrencesR
# - Recursive function to take into 2 parameters: szSrc and szToken
# - Returns the total number of occurrences of "szToken" from the string, "szSrc"
# - Hint: Use find() method from String.   Search on the Internet for more details
#   >> str = "abcd"
#   >> str.find("bc") 
#   >> 1  (index of the first occurrence of the substring "bc")
##
## TODO: Implement this recrusive function

##
# str_to_num
# - Recursive function to convert the parameter, szStr, (String) to integer
# - Returns the integer representation of the "szStr"
# - Assume that the string, szStr, has all digit values between '0' and '9'
# - MUST not use int() 
# - Hint: Use ord() and ord("0") accordingly
##
## TODO: Implement this recrusive function

##
## Please do NOT change the following code
## You must implement the recursive function, findOccurrencesR(), and str_to_num(), in order to run the following code without error
##
print(4==findOccurrencesR("HellohiHellohihihi", "hi"))     #4
print(2==findOccurrencesR("catcowcat","cat"))              #2
print(1==findOccurrencesR("catcowcat","cow"))              #1
print(2==findOccurrencesR("cccatcowcatxx","cat"))          #2
print(3==findOccurrencesR("abccatcowcatcatxyz","cat"))     #3
print(2==findOccurrencesR("xyx","x"))                      #2
print(1==findOccurrencesR("xyx","y"))                      #1
print(0==findOccurrencesR("xyx","z"))                      #0
print(1==findOccurrencesR("z", "z"))                       #1
print(0==findOccurrencesR("x","z"))                        #0
print(0==findOccurrencesR("","z"))                         #0
print(4==findOccurrencesR("hiHellohihihi","hi"))           #4
print(1==findOccurrencesR("hiHellohihihi","hih"))          #1
print(1==findOccurrencesR("hiHellohihihi","o"))            #1
print(1==findOccurrencesR("hiHellohihihi","ll"))           #1
print()

val = str_to_num("8")
print("{} is type of {}".format(val, type(val)))
val = str_to_num("12")
print("{} is type of {}".format(val, type(val)))
val = str_to_num("23480")
print("{} is type of {}".format(val, type(val)))

# Expected Output
#True
#True
#True
#True
#True
#True
#True
#True
#True
#True
#True
#True
#True
#True
#True
#
#8 is type of <class 'int'>
#12 is type of <class 'int'>
#23480 is type of <class 'int'>