from netmiko import ConnectHandler

user = "impsac"
clave = "$4c1mp.19"
secreto = "cisco"
host = "10.6.0.8"
n = 0

h = open("host.txt", "r")

for x in h:

	print("EQUIPO "+str(x))
	ciscoIOSSh = {
		"device_type": "cisco_ios",
		"ip": x,
		"username": user,
		"password": clave,
		"secret": secreto,
		}

	ciscoIOS = {
	"device_type": "cisco_ios_telnet",
	"ip": x,
	"username": user,
	"password": clave,
	"secret": secreto,
	"port": 23
	}

	try:
		net_connectSh = ConnectHandler(**ciscoIOSSh)

		#net_connectSh.enable()

	
		output2 = net_connectSh.send_config_set("no ip bootp server")
		print(output2)
		output2 = net_connectSh.send_config_set("ip dhcp bootp ignore")
		print(output2)

		output = net_connectSh.send_command("show run | in bootp")

		print(output)

		output = net_connectSh.send_command("wr")
		print(output)

		net_connectSh.disconnect()

	except Exception as e:

		print (e)

		print ("TELNET PARA :"+x)
	
		net_connect = ConnectHandler(**ciscoIOS)

		#net_connect.enable()

	
		
		output2 = net_connect.send_config_set("no ip bootp server")	
		print(output2)

		output2 = net_connect.send_config_set("ip dhcp bootp ignore")

		print(output2)

		output = net_connect.send_command("show run | in bootp")

		print(output)

		output = net_connect.send_command("wr")

		print(output)

		net_connect.disconnect()
	
	n = n + 1


	print("\n \n" )

print("Equipos configurados: "+str(n))


h.close()
