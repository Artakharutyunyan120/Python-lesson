
import random

res = random.choice('up')
point = 0
if res == 'u':
	while True:
		end = 3
		while True:
			if point > 18:
				end = 21 - point
			user = input(f'1 - {end} ')
			if user.isdigit():
				user = int(user)
				if user >= 1 and user <= end:
					print(f'User: {point} + {user} = {user + point}')
					point += user
					break
				else:
					print(f'Please enter between (1 - {end})')
			else:
				print('Only numbers')
		if point >= 21:
			print('You Lose')
			break

		pc = 4 - point % 4
		print(f'Pc: {point} + {pc} = {pc + point}')
		point += pc

else:
	print('Start PC')
	while True:
		if point %4==0:
			pc = random.randint(1,3)
		else:
			pc=4-point%4
		print(f'{point} + {pc} = {pc + point}')
		point += pc
		if point >= 21:
			print('You Win')
			break

		end = 3
		while True:
			if point > 18:
				end = 21 - point
			user = input(f'1 - {end} ')
			if user.isdigit():
				user = int(user)
				if user >= 1 and user <= end:
					print(f'User: {point} + {user} = {user + point}')
					point += user
					break
				else:
					print(f'Please enter between (1 - {end})')
			else:
				print('Only numbers')
		if point >= 21:
			print('You Lose')
			break