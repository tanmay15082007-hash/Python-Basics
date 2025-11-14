t = (15,23,15,56,23,98)
print(t.count(15))
print(t.count(23))
print(t.index(15))
print(t.index(23))
print(t.index(56))
print(t.index(98))

'''
Why Use Tuples?
- Faster than lists (since they are immutable)
- Used as dictionary keys (since they are hashable)
- Safe from unintended modifications
'''