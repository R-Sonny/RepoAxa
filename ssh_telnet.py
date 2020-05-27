#R.Sonny 
from netmiko import ConnectHandler

user = "cisco"
clave = "cisco"
secreto = "cisco"
host = "10.6.0.8"


ciscoIOS = {
"device_type": "cisco_ios_telnet",
"ip": host,
"username": user,
"password": clave,
"secret": secreto,
"port": 23
}

try:
	net_connect = ConnectHandler(**ciscoIOS)

	net_connect.enable()

	
	output2 = net_connect.send_config_set("interface vlan 40")

	print(output2)

	output = net_connect.send_command("show ip interface brief | in Vlan")

	print(output)

	net_connect.disconnect()

except Exception as e:

	print (e)
	ciscoIOSSh = {
	"device_type": "cisco_ios",
	"ip": host,
	"username": user,
	"password": clave,
	"secret": secreto,
	}

	net_connectSh = ConnectHandler(**ciscoIOSSh)

	net_connectSh.enable()

	
	output2 = net_connectSh.send_config_set("interface vlan 42")

	print(output2)

	output = net_connectSh.send_command("show ip interface brief | in Vlan")

	print(output)

	net_connectSh.disconnect()


