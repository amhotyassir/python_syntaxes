import re
#################################
#initializing variables to not have errors
string=''
substring=''
#################################
# MORE INFO IN THE DOCUMENTARY (see Favorites)
re.search(substring,string) # this returns an object which can be used in an IF statement

re.split(substring,string) # returns a list of substrings of the string and removes the 'substing'

re.findall(substring,string) # returns a list [substring,...,substring] (EXP:['Amy,'Amy']) which length is equal to the number of occurence of the 'ubstring' in the string
re.findall("?=<text>.*",string)
re.findall("?P<text>.*",string)# see documentation
re.findall("?P<text>.*",string,re.VERBOSE)
re.finditer("?P<text>.*",string,re.VERBOSE)
