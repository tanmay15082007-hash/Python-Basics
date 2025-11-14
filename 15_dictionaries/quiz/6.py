a = input("Enter the numbers:\n").split()
print(a)
print(list(set(a)))


def most_expen(products):
    return max(products.items(), key = lambda x: x[1])

products = {"Pen":10,"Pencil":15,"Coffee":12}
product, price = most_expen(products)
print(f"The most expensive product is '{product}' with price {price}.")

'''
🧪 Example that shows why key is necessary

Imagine the dict:

products = {"Zebra": 10, "Apple": 50}


Without key:

max(products.items())


Compares:

("Zebra",10) vs ("Apple",50)


Since "Zebra" > "Apple" alphabetically,
max() will wrongly return:

("Zebra", 10)


But with key:

max(products.items(), key=lambda x: x[1])


It compares:

10 vs 50


Returns:

("Apple", 50)
'''


# There are 2 solutions as discussed in the video
# Solution 1 
def merge_dicts(dict1, dict2):
    '''
    Merge two dictionaries into one.

    Parameters:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: A new dictionary with combined key-value pairs
    '''
    return {**dict1, **dict2}

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = merge_dicts(d1, d2)
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Solution 2
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update(d2)
print(d1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}