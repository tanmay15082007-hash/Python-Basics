marks = {"Tanmay":98,"Vansh":89,"Naitik":56,"Betra":45}
print(marks,type(marks))

print(marks.keys())
print(marks.values())
# marks.clear # clears a dictionary nothing present inside it
marks.pop("Betra")
print(marks)