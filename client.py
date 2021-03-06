import socket
import _thread
import os
import alphabet


os.system('')

def main():
	host = '172.20.10.3'
	port = 5555

	for x in range(70):
		print('')

	try:
		file = open('config.txt', 'r+')
		write = False
	except:
		file = open('config.txt', 'w')
		write = True

	if not write:
		lines = file.readlines()
		un = lines[0][:-1]
		colour = lines[1]
	else:
		un = input('\033[2;32;40mPlease pick a username:\033[0m ')
		file.write(un + '\n')
		while True:
			try:
				print("""Pick a colour:
\033[1;30;40m30 - Black
\033[1;31;40m31 - Red
\033[1;32;40m32 - Green
\033[1;33;40m33 - Yellow
\033[1;34;40m34 - Blue
\033[1;35;40m35 - Purple
\033[1;36;40m36 - Cyan
\033[1;37;40m37 - White\033[0m""")
				colour = int(input())
				if colour:
					break
			except:
				print('\033[2;31;40mERROR: Colour must be an integer between 30 and 37\033[0m')
		file.write(str(colour))
	file.close()

	s = socket.socket()
	s.connect((host, port))

	def getMessages():
		while True:
			data = s.recv(1024).decode('utf-8')
			print(data)
	def sendMessage():
		while True:

			encrypt = input(" ")
			key = 3
			encrypted = ""
			for letter in encrypt:
				if letter in alphabet.latin:
					position = alphabet.latin.find(letter)
					newposition = position + key
					if letter in alphabet.latin:
						encrypted = encrypted + alphabet.latin[newposition]
					else:
						continue
				elif letter in alphabet.kyrylica:
					position = alphabet.kyrylica.find(letter)
					newposition = position + key
					if letter in alphabet.kyrylica:
						encrypted = encrypted + alphabet.kyrylica[newposition]
					else:
						continue

				elif letter in alphabet.numbers:
					position = alphabet.numbers.find(letter)
					newposition = position + key
					if letter in alphabet.numbers:
						encrypted = encrypted + alphabet.numbers[newposition]
					else:
						continue
				else:
					encrypted = encrypted + letter
			s.send(('\033[1;' + str(colour) + ';40m' + un + ':\033[0m '  + encrypted).encode('utf-8'))

	_thread.start_new_thread(getMessages, ())
	_thread.start_new_thread(sendMessage, ())

	while True:
		pass

if __name__ == "__main__":
	main()