chairs = '15'
nails = 4
total_nails = chairs * nails
message = "I need to buy {}nails".format(total_nails)
print("You need to buy {}nails".format(message))

chairs = "15"
nails = 4
total_nails = chairs * nails
message = "You need to buy (total_nails)"
print(f"You need to buy {total_nails} nails")


my_name = "Penelope"
my_age = 29
message = f'My name is {my_name} and I am {my_age} years old'
print(message)


full_box_of_eggs = 6
omelette_recipe = 4
one_box_of_eggs = 1.5
quantity_of_omelettes = (full_box_of_eggs) /(omelette_recipe)
quantity_box_of_eggs = (quantity_of_omelettes) // (one_box_of_eggs)
#message = "You can make (quantity_of_omelettes) omelettes with (quantity_of_omelettes) // 1.5
print(f"You can make {quantity_of_omelettes} omelettes with {quantity_box_of_eggs} boxes of eggs")


boxes_of_eggs = 45
total_omelettes = int((boxes_of_eggs) * 1.5)
print(f"You can make {total_omelettes} omelettes with {boxes_of_eggs} boxes of eggs")