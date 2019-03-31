#from socket import * 
import json
import os

os.system('clear')

script_name = '>>> '

print("Enter path your file:")

while True:
	path = input(script_name)

	try:
		f = open(path)
		break
	except:
		print('ERROR')
		print(' File Not Found')

while True:
	command = input(script_name)

	if (command == 'exit'):
		os.system('clear')
		break

	elif (command == ''):
		pass

	elif (command == 'view'):
		with open(path) as f:
			tmp = json.load(f)
			print(json.dumps(tmp, indent=4, sort_keys=True))

	elif (command == 'add'):
		param = str(input('Enter parameter: '))
		value = str(input('Enter value of '+param+': '))
		with open(path) as f:
			tmp = json.load(f)
		tmp[param] = value
		with open(path,'w') as f:
			json.dump(tmp, f, indent=4, sort_keys=True)

	elif (command == 'del'):
		param = input('Enter parameter: ')
		with open(path) as f:
			tmp = json.load(f)
		del tmp[param]
		with open(path,'w') as f:
			json.dump(tmp, f, indent=4, sort_keys=True)

	elif (command == 'edit'):
		param = input('Enter parameter: ')
		value = input('Enter value: ')
		with open(path) as f:
			tmp = json.load(f)
		del tmp[param]
		tmp[param] = value
		with open(path,'w') as f:
			json.dump(tmp, f, indent=4, sort_keys=True)

	elif (command == 'give'):
		param = input('Enter parameter: ')
		with open(path) as f:
			tmp = json.load(f)
		print('Value of '+param+' : '+str(tmp[param]))

	else:
		print('===============================================')
		print('                   Help list                   ')
		print('===============================================')
		print('view\t\tViews json file content')
		print('add\t\tAdds parameter in json file')
		print('del\t\tDelete parameter from json file')
		print('edit\t\tEdit value of parameter')
		print('give\t\tGives value of parameter')
		print('===============================================')
		print()
		print('===============================================')