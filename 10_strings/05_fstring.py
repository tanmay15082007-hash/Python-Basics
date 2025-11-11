template = "Dear {}, you are so awesome. Take this {}$ bag."
a = "Bittu"
a1 = 1000
b = "Vansh"
b1 = 100
c = "Tanmay Khandelwal"
c1 = 10000
print(template.format(a,a1))
print(template.format(b,b1))
#     print(template.format(c,c1))
print(f"{c} are awesome. Take this {c1}$ bag.")   # f-string

print(ord('A'))  # convert the value of 'A' into ASCII
print(chr(65))   # just the opp of above
print(chr(1))   # in output no character is seen as it decodes character from its ASCII value