name = "Tanmay" # Here we can change name inside the str and it will make a new string but we cant change the position or the value of str like in 3 position.Strings are immutable
#  name[0]= "R"  We cant do this as this is not acceptable to change a char 
print(len(name))  # LEN is a function which tells us length of string that is name has 6 characters
print(name.upper())   # Here we are not making changes to name we create a new 

a = " i am Tanmay Khandelwal "
print(len(a))  # Even the gaps bw I and a is counted as a char
print(a.upper(), a) # A new str which will make all the characters in capital letters
print(a.lower(), a) # A new str which will make all the characters in lower case letters
print(a.lower(), a) # A new str which will make all the characters in lower case letters
print(a.capitalize(), a) # A new str which will capitalise the first letter that is I
print(a.title(), a)  # Title means that i am tanmay khandelwal all first letter that is i a t k will be in capital letters
print(a.strip(), a)  # it strips all the new lines and gaps
print(a.lstrip(), a) # it strips the left part
print(a.rstrip(), a) # it strips the right part
print(a.find("am")) # it find a specific word in a str and it returns index of first occurence 
print(a.replace("i","I"))  

b = "Apples,Bananas,Cherries"
print(b.split()) # convert str into lists
print(b.join(['Apples,Bananas,Cherries']))  # convert lists into str

t = "Tanmay15082007"
print(t.isalpha()) # tells us that if all the characters are letters or not in true and false
print(t.isdigit()) # tells us that if all the characters are numbers or not in true and false
print(t.isalnum()) # tells us that if all the characters are a mixture of letters and numbers or not in true and false
print(t.isspace()) # tells us that if it has a space char or not