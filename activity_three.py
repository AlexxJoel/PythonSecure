# simple if function that compares two values and print the results

# Dictionaries
# It hqs key and value, uses quotes
dictionary = {"Value 1": "1000", "value 2": 30, "Value 3": True}
print(type(dictionary))
print(dictionary)
print('value specific', dictionary['Value 1'])
dictionary['Value 3'] = False
dictionary['Value 4'] = 'It was added'

dictionary = {'name': 'Joel', 'age': 30, 'hobbies': ['play', 'read', 'run']}

for key in dictionary:  # iterate the keys
    print(key, '->', dictionary[key])

keys = dictionary.keys()  # return the keys
print(keys)

values = dictionary.values()  # return the values
print(values)

dictionary.clear()  # delete all elements44
print(dictionary)

print(dictionary.get('name'))  # return the value of the key
dictionary.setdefault('name', 'Joel')  # return the value of the key
print(dictionary.setdefault('name'))  # it's the same that get

del(dictionary['name'])  # delete the key and value
dictionary.setdefault('name', 'Joel')
dictionary.pop('name')  # delete the key and value

dictionary.update({'name': 'Alexx'})  # add a new key and value
dictionary.update({'name': 'Joel'})  # update the value of the key

# conditional if
if 'la' in 'hola':
    print('exists')
elif 'ul' in 'ulises':
    print('exists')
else:
    print('aaaaa! ')





