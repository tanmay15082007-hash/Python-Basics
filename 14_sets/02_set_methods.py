s = {1,2,3,4,5,6}
print(s)
s.add(1)  # here we add 1 but output is still same as above it is because there is already 1 present and adding 1 which is not unique for example look at below code
print(s)
s.add(32)
print(s)
s.remove(2)
print(s)
# s.remove(78) # here in s there is no element 78 present so it will show error! but lets say if set is very big and we dont have time to actually see if it is presnt so to remove if that element is present we use
s.discard(78)
print(s)
# s.pop # in this it removes a random method not generally used

