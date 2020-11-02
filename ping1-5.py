import os


results_file = open("results2.txt", "w")


with open('source-ip') as file:
	source = file.read()
	source = source.splitlines()
#	print (source)

with open('destination-ip') as file:
       des = file.read()
       des = des.splitlines()
#       print (des)

for x in range (2):
#	print('********************************************************************** loop Num = ' , x)
#	print('********************************************************************** Loop Num = ' , x)
	for ip in source :
		print('                                                                                  ')
		print('********************************* new source  *************************************')
		print('                              '+ ip +" Loop num:",x+1 )
		print('********************************* new source  *************************************')
		print('                                                                                  ')

		results_file.write(f"********************************* *********************************** " + "\n")
		results_file.write(f"            source from  {ip}  loop Num: {x}                       " + "\n")
		results_file.write(f"********************************* *********************************** " + "\n")

		for ipd in des :
			response = os.popen(f"ping -c 1 -I {ip} {ipd}").read()
#			print (response)
			if " 1 received" in response:
				print(f"UP  Ping from {ip} to {ipd} Successful")
				results_file.write(f"UP  Ping from {ip} to {ipd} Successful" + "\n")
			else:
				print(f"Down  Ping Ping from {ip} to {ipd} Unsuccessful")
				results_file.write(f"Down  Ping from {ip} to {ipd} Unsuccessful" + "\n")


results_file.close()

