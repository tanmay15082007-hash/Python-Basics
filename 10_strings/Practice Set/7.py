# METHOD-1
a = input("enter the word for which its vowel is counted:\n")
b = a.lower()
c = int(b.count("a"))
d = int(b.count("e"))
e = int(b.count("i"))
f = int(b.count("o"))
g = int(b.count("u"))
print(c+d+e+f+g)

# METHOD-2
vowels = ['a','e','i','o','u']
sum = 0
for char in b:
    if(char in vowels):
        sum+=1

print(f"There are {sum} vowels in",a)

# METHOD - 3 [Most slick]
a = input("Enter a word:\n").lower()
vowels = 'aeiou'
count = sum(1 for char in a if char in vowels)
print(f"There are {count} vowels in {a}")