my_foods = ['pizza', 'tiramisu', 'spagetti', 'schabowy', 'mizeria']
my_friend_foods = my_foods[:]
my_foods.append('pomidorowa')
my_friend_foods.append('gofry')
print("Moje ulubione potrawy to:")
for food in my_foods:
	print('-' + food.title())
print('Ulubione potrawy mojego przyjaciela to:')
for food in my_friend_foods:
	print('-' + food.title())