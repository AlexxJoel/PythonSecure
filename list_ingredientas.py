# activity
# Create a software in python that has  a dictionary with the name's ingredients (minimum 3) and the price of each one,
# and says the discount depends on
# 15% if the total is more than 100
# 10% if the total is more than 50 and less than 100
# 5% if the total is less than 50 and more than 25
# 0% if the total is less than 25

ingredients = {}
total = 0
discount = 0

for i in range(3):
    name = str(input('Add the name of the ingredient \n->\t'))
    price = int(input('Add the price of the ingredient \n->\t'))
    ingredients[name] = price
    total += price

if total >= 100:
    discount = 0.15
elif 50 <= total < 100:
    discount = 0.10
elif 25 <= total < 50:
    discount = 0.05
else:
    discount = 0

print(type(ingredients))
print(ingredients)
print(f'The total is {total} and the discount is {discount * 100}%')
print(f'The total to pay is {total - (total * discount)}')



