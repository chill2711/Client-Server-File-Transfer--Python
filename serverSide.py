import socket
 
from datetime import datetime

import filecmp

#initializing host, port
HOST = '192.168.0.212'
PORT = 9000
#starting the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
totalTime = 0
print('I am ready for any client side request \n')
#list to store times
l = []
totalFilesCount = 1
#to stop at 100
d = 101 
i=1;
#number of errors counted for files not matching
errorCount = 0

#original file used for comparison
fileName = 'CompareStandard.txt';
      
for i in range(1,d):
    #start time
    start_time = datetime.now()
    conn, addr = s.accept()
    #file received name
    file = 'receive'+str(i)+'.txt';

    print('I am starting receiving file ', file, 'for the ',i,'th time')
    #opening the file to write
    f = open(file, 'wb')
    #data = conn.recv(1024)
    data = conn.recv(1024)
    while (data):
        f.write(data)
        data = conn.recv(1024)
    f.close()
    conn.close()

    print('I am finishing receiving file ', file, 'for the ',i,'th time ')
    #end time
    end_time = datetime.now()
    #getting difference between start time and end time
    time_difference = (end_time - start_time)
    #converting time to milliseconds
    execution_time = time_difference.total_seconds() * 1000
    print('The time used in milliseconds to receive ', file, 'for the ', i, 'th time is : ', execution_time, '\n')
    #adding time to list
    l.append(execution_time)
    # add the code to verify each received file here
    # use function "filecmp.cmp('received.txt", fileName, ...)"
    #if the two files do not match it will return false and increase errorCount by 1
    comp = filecmp.cmp(fileName,file)
    if comp == False:
        errorCount+=1
#getting average time
average_time = sum(l) / len(l)
#getting total time
list_sum = sum(l)
print('The average time to receive ', file, ' in milliseconds is : ', average_time)
print('The total time to receive ', file, '100 times in milliseconds is : ' , list_sum,'\n')
print(errorCount, ' Times out of 100 are not correct!')
#finished
print('I am done')



s.close()


    


