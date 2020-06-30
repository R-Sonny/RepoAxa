
###Loocking for a MAC ADDRESS

import telnetlib
import getpass


user = "cisco"
password = "cisco"

host = ["10.6.0.8","10.6.0.10"]
port = 23
time = 100


enable = "enable"
exit = "exit"
mac = input("MAC: ")
show = "show mac address-table | in "+ mac
showr = "show run | in "+ mac


for x in host:

	tn = telnetlib.Telnet(x, port, time)
	tn.read_until(b"Username:")
	tn.write(user.encode('ascii')+b"\n")

	if password:
		tn.read_until(b"Password:")
		tn.write(password.encode('ascii')+b"\n")

	tn.write(enable.encode('ascii')+b"\n")

	if password:
		tn.read_until(b"Password:")
		tn.write(password.encode('ascii')+b"\n")


	tn.write(show.encode('ascii')+b"\n")
	tn.write(showr.encode('ascii')+b"\n")
	

	tn.write(exit.encode('ascii')+b"\n")
	print(tn.read_all().decode('ascii'))
