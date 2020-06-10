from netmiko import ConnectHandler

user = "impsac"
clave = "$4c1mp.19"
secreto = "cisco"
host = "10.6.0.8"
comando = input("\nComando a validar:")
n = 0

h = open("host.txt", "r")

for x in h:

	print("********************")

	print("EQUIPO "+str(x))

	print("********************")
	

	try:
		net_connectSh = ConnectHandler(ip= x, device_type="cisco_ios", username= user, password= clave)

		#net_connectSh.enable()

		output = net_connectSh.send_command("show run | in hostname\n")
		print(output)

		print(comando +"\n")
		output = net_connectSh.send_command(comando)
		print(output)



		net_connectSh.disconnect()

	except Exception as e:

		print (e)

		print ("TELNET PARA :"+x)
		
		net_connect = ConnectHandler(ip= x, device_type="cisco_ios_telnet", username= user, password= clave, port=23)

		#net_connect.enable()

		
		
		
		output = net_connect.send_command("show run | in hostname\n")
		print(output)

		print(comando +"\n")
		output = net_connect.send_command(comando)
		print(output)
		net_connect.disconnect()

	
	n = n + 1


	print("\n \n" )

print("Equipos configurados: "+str(n))


h.close()
