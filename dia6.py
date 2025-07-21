empty_tuple = ()
brothers = ("Luis", "Juan")
sisters = ("Ana", "Sofía")
siblings = brothers + sisters
print("Tengo", len(siblings), "hermanos/as.")
family_members = siblings + ("Mamá", "Papá")
siblings = family_members[:-2]
parents = family_members[-2:]
fruits = ("manzana", "plátano")
vegetables = ("zanahoria", "brócoli")
animal_products = ("leche", "queso")

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
middle_index = len(food_stuff_lt) // 2
middle_items = food_stuff_lt[middle_index-1:middle_index+1] if len(food_stuff_lt) % 2 == 0 else [food_stuff_lt[middle_index]]
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
del food_stuff_tp
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

print("Estonia" in nordic_countries)  # False
print("Iceland" in nordic_countries)  # True
