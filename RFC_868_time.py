#libraries:
import socket
import struct

class Client:

    def __init__(self,server,port):
        """
        Client for obtaining time in human readable format [hour:sec day month year]
        Example:
        Client(server,port)
        """
        response = Client.request_time_from(server,port)
        Client.human_readable_format(response)    

    #request time from server and obtain time in format specified at RFC 868
    def request_time_from(server,port):
        
        recieve_buffer_size = 4096

        #Create socket
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
        #connect to sever
        mySocket.connect((server,port))
        #send request
        #mySocket.send()
        #Reciece request
        response_string = mySocket.recv(recieve_buffer_size)
        # socket close
        mySocket.close

        response, = struct.unpack('!I', response_string) #convert bytes format to decimal
        return  response

    #convert RFC 868 format to human readable format [hour:sec day month year]
    def human_readable_format(response):
        
        #convert number of seconds from 1900 to [hour:sec day month year] format
        minutes = int(response/(60*60)%1*60)
        hours = int(response/(24*60*60)%1*24)
        year = int(1900+(response/(365.25*24*60*60)))
        #calculating day
        # adddditional days due to leap year system 
        add_days = 0
        for years in range(1900,year+1,100):
            if(years%400 == 0):
                add_days = add_days+1
        days = int(response/(365.25*24*60*60)%1*365.25)+add_days #number of days from current yeas
        #calculating current month and day 
        isday=False
        day = days
        month = 1 
        while(not isday):  
            if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
                if day <= 31:
                    isday = True
                else:
                    day = day -31
                    month =month+1    
            elif (month==4 or month==6 or month==9 or month==7 or month==11):
                if day <= 30:
                    isday = True               
                else:
                    day = day -30
                    month =month+1
            elif (month ==2):
                if (year%400==0):
                    if day <= 29:
                        isday = True                    
                    else:
                        day = day -29
                        month =month+1 
                else:
                    if day <= 28:
                        isday = True
                    else:
                        day = day -28
                        month =month+1   
            else:
                print("something is wrong, you exeed 12 months (are you from another planet?")                           
    
        #print time 
        print(str(hours) +":"+ str("{0:0=2d}".format(minutes))+" "+str(day)+" "+str("{0:0=2d}".format(month))+" "+str(year)+" GMT")
        





