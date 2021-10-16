import socket
from datetime import datetime
#initializing host, port, filename, total time and number of times to send the file
host = '192.168.0.212'
port = 9000
fileName = "send.txt"
 

print('I am connecting to server side: ', host,'\n')
 
#starting at 1
x=1
#ending at 100
y= 101
#creating list to store send times for each file
l = []

for x in range(1,101):
    #start time
    start_time = datetime.now()
    s = socket.socket()
    s.connect((host, port))
    print('I am sending file', fileName,' for the ',x,'th  time')
    #opening file to read
    file_to_send = open(fileName, 'rb')    
    #reading the first 1024 bytes
    data = file_to_send.read(1024)
    while data:
        s.send(data)
        #reading the next 1024 bits
        data = file_to_send.read(1024)
    print('I am finishing sending file', fileName,' for the ',x,'th  time')
    #end time
    end_time = datetime.now()

    #getting the difference between start and end time    
    time_difference = (end_time - start_time)
    #converting time to milliseconds
    execution_time = time_difference.total_seconds() * 1000
    print('The time used in milliseconds to send send.txt for the ', x, 'th time is : ', execution_time, '\n')

    #adding the time to the list
    l.append(execution_time)

    s.close()
    file_to_send.close()
#getting average time
average_time = sum(l) / len(l)
#getting total time
list_sum = sum(l)
print('The average time to send send.txt in milliseconds is : ', average_time)
print('The total time to send send.txt 100 times in milliseconds is : ' , list_sum)
#s.close()

#finished
print('I am done')
