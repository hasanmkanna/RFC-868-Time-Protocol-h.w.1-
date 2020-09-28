from RFC_868_time import Client

 
#server chosen:
port = 37
server1= "129.6.15.27"
server2= "132.163.97.6"

#output
#The IP address of each server
print("The IP address of each server")
print("[SERVER1 ID]: "+server1)
print("[SERVER2 ID]: "+server2)

#Time of each server in a human readable format.
print("\nTime of each server in a human readable format:")
response1 = Client(server1,port)
response2 = Client(server2,port)


#Time difference between the two times retrieved
response1= Client.request_time_from(server1,port)
response2 = Client.request_time_from(server2,port)
diff = abs(response1-response2)
print("\nTime difference between the two times retrieved: "+str(diff)+" SEC")


