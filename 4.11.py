pizzas = ['margerita', 'fungi', 'salami']
for pizza in pizzas:
	print(f"Lubie pizze {pizza.title()}.")
print('Naprawde przepadam za pizza')	
friend_pizzas = pizzas[:]
pizzas.append('vesuvio')
friend_pizzas.append('farmerska')
print('Moje ulubione pizze to:')
print(pizzas)
print('\nUlubione rodzaje pizzy mojego przyjaciela to:')
print(friend_pizzas)