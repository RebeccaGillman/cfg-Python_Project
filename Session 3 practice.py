
# print('~' * 0)
# print('~' * 1)
# print('~' * 2)
# print('~' * 3)
# print('~' * 4)
# print('~' * 5)
# print('~' * 6)
# print('~' * 7)
# print('~' * 8)

# for number in range(9):
#     print('~' * number)

# today = input('What day is it? ')
# is_monday = today == 'Monday'
# print('Today is Monday: {}'.format(is_monday))

# temperature = input('What is the temperature? ')
# is_freezing = float(temperature) <= 0.0
# print('The temperature is freezing: {}'.format(is_freezing))

# price = input("How much is the burger? ")
# budget = float(price) <= 10.0
# vegetarian_option = input("Does the restaurant have a vegetarian option? y/n ")
# yes_vegetarian = vegetarian_option == "y"
# should_visit_restaurant = budget and yes_vegetarian
# print("You should visit the restaurant: {}".format(should_visit_restaurant))

# mars_choice = input('Would you like to visit Mars? y/n ')
# is_willing = mars_choice == 'y'
# affordable = input('Can you afford to visit Mars? y/n ')
# can_afford = affordable == 'y'
# should_visit_mars = is_willing and can_afford
# print('You should visit Mars: {}'.format(should_visit_mars))
#
# password = input('password: ')
# if password == 'jumanji':
#     print('Success!')


# name = input("What is your name? ")
# is_admin = name == 'admin'
# password = input("What is your password? ")
# is_password_correct = password == 'dinosaurs'
# if is_admin and is_password_correct:
#     print('Welcome')
# if not is_admin or not is_password_correct:
#     print('Go away')

# price = input("How much is the burger? ")
# budget = float(price) <= 10.0
# vegetarian_option = input("Does the restaurant have a vegetarian option? y/n ")
# yes_vegetarian = vegetarian_option == "y"
# if budget and yes_vegetarian:
#     print("This restaurant is a great choice")
# if not budget or not yes_vegetarian:
#     print("Probably not a good idea")

#

# temperature = float(input("What is the oven temperature? "))
# if temperature > 200:
#     print("The oven is too hot")
# elif temperature < 150:
#     print("The oven is too cold")
# elif temperature == 180:
#     print("The oven is at the perfect temperature")
# else:
#     print("The temperature is close enough")


# import random
# random_integer = random.randint(1, 100)
# print(random_integer)

# import random
# sides = int(input('How many sides does the die have? '))
# random_integer = random.randint(1, sides)
# print('You rolled a {}'.format(random_integer))


# import random
# def flip_coin():
#     random_number = random.randint(1, 2)
#     if random_number == 1:
#         side = 'heads'
#     else:
#         side = 'tails'
#     return side
# choice = input('heads or tails: ')
# result = flip_coin()
# print('The coin landed on {}'.format(result))
#
# if choice == result:
#     print("You win")
#
# else:
#     print("You lose")

#
# HOMEWORK

# is_it_raining = input("Is it raining today? y/n ")
# raining = is_it_raining == "y"
# if raining:
#     print("Take an umbrella")
# else:
#     print("You don't need an umbrella")


# my_money = int(input('How much money do you have? ')) #make it an int
# boat_cost = 20 + 5
# if my_money >= boat_cost: #make this more than or equal to
#    print('You can afford the boat hire')
# else:
#     print('You cannot afford the board hire')

year = int(input("What year was the book written? "))
if year in range(1800,1809):
    print("Nineteenth century, first decade")
elif year in range(1810,1819):
    print("Nineteenth century, second decade")
elif year in range(1820,1829):
    print("Nineteenth century, third decade")
elif year in range(1830,1839):
    print("Nineteenth century, fourth decade") #etc etc





