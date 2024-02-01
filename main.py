

# code from Vasyl Hohol
# GitHub: https://github.com/tr1Ggereo

import os, ctypes

user_id = { 'admin':1, 'vasyl':2, 'bogdan':3 }

passwords = { 1:'admin', 2:'vasiliy', 3:'bodgi' }

def is_admin():
	try:
		return os.getuid() == 0
	except AttributeError:
		return ctypes.windll.shell32.IsUserAnAdmin() != 0

def printer(text):
	return print(f'\n{text}\n')

def login():
	InlineUser.login()

class Client:

	def __init__(self):
		self.client_version = '\033[32m0.1a\033[0m'
		self.commands = ['help', 'su', 'version', 'quit', 'user', 'exit', 'getuser', 'changepassword', 'clear', 'getusers', ]
		self.help_text = '\033[33msu\033[0m - check if you start programm from super-user\n\033[33mversion\033[0m - check version programm\n\033[33mexit\033[0m - exit with programm \
		\n\033[33muser\033[0m - check you account\n\033[33mexit\033[0m - log-out\n\033[33mgetuser \033[34m[username]\033[0m - check if user registered \
		\n\033[33mchangepassword \033[34m[old password] \033[34m[new password]\033[0m - change your password\n\033[33mclear\033[0m - clear a terminal\n\033[33mgetusers\033[0m - check all users \
		\n\033[33mregister \033[34m[username] [user password]\033[0m - register new user'

	def start(self):
		while True:
			command = input('Enter command: ')
			match command.split():
				case 'help', :
					printer(self.help_text)
				case 'su', :
					if is_admin() == True:
						printer('You super-user!')
					else:
						printer('You don\'t have permissions!\n\nFor using super-user permissions get administrator profile or root in your OS.')
				case 'version', :
					printer(f'You current version: {self.client_version}')
				case 'quit', :
					printer('Good-bye!')
					break
				case 'user', :
					printer(f'Your logged from:\033[34m {InlineUser.get_user()}\033[0m')
				case 'exit', :
					printer('Your exit from this account!')
					login()
				case 'getuser', value:
					if len(value) >= 0: 
						if value in user_id:
							printer(f'User: \033[34m{value}\033[0m, ID: \033[34m{user_id[value]}\033[0m')
						else:
							printer(f'User "\033[34m{value}\033[0m" is not registered!')
					else:
						printer('You don\'t type username!')
				case 'changepassword', value1, value2:
					self.user = InlineUser.get_user()
					self.userid = user_id[self.user]
					if passwords[self.userid] != value1:
						printer('Your type wrong password!')
					elif len(value2) <=5:
						printer('Password to small!')
					elif len(value2) >=37:
						printer('Password to long!')
					else:
						passwords[self.userid] = value2
						printer('Password change success!')
				case 'clear', :
					x = 0
					while True:
						if x < 2000:
							x = x + 1
							print('\n')
						else: break
				case 'getusers', :
					for i in user_id.keys():
						print(f'User: \033[34m{i}\033[0m, ID: \033[34m{user_id[i]}\033[0m')
				case 'register', value1, value2:
					for i in user_id.keys():
						if i == value1:
							return printer('This user registered!')
					if len(value2) <=5:
						printer('Password to small!')
					elif len(value2) >=37:
						printer('Password to long!')
					else:
						user_id[value1] = len(user_id) + 1
						passwords[len(user_id)] = value2
						print(passwords)
						printer('User registered success!')

	def get_version(self):
		return self.client_version

class Users:

	def __init__(self):
		pass

	def get_user(self):
		return self.username

	def login(self):
		self.username = input('You username: ')
		if len(self.username) != 0:
			if self.username in user_id:
				self.userpass = input('Enter your password: ')
				if passwords[user_id[self.username]] == self.userpass:
					print('Your are logged!')
					print(f'\nCurrent version: {Client.get_version()}\nEnter "help" if your need help.\n')
					Client.start()
				else:
					print('Bad pass!')
					login()
			else:
				print('This user is not a registered!')
				login()
		else:
			print('Please, enter the username!') 
			login()

if __name__ == '__main__':
	Client = Client()
	InlineUser = Users()
	login()
