# 
# 	Author: Ruby Abrams
# 	Description:	
# 			This will be used as a list of reminders 
#			that can be accessed through terminal
# 

import sys

def write(todo, filename):
	target = open(filename, 'a')
	target.write("-"+todo)
	print("added to todo list: "+todo)
	target.close()

def read(filename):
	with open(filename, 'r') as f:
		for line in f:
			print(line)

if __name__ == '__main__':
	filename = "todo.txt"
	option = sys.argv[1]
	if option == 'add':
		write(sys.argv[2], filename)
	elif option == 'print':
		read(filename)
	# elif option == 'clear':			# to be added	
	else:
		print("Did not recognize command")