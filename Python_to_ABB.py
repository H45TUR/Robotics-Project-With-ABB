#fetch data from arduino components
import numpy as np
x=1
While x=1:
  #get the rotational and displacement data from the gyro
  X=
  Y=
  Z=
  XYR=
  XZR=
  YZR=
  Dis= np.array([X,Y,Z,XYR,XZR,YZR])



#sent data to the ABB server copied by Lab3
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1' #Loopback adresse, bruk adressen til robotene når dere tester
der
port = 2222
msg = ''
client.connect((host,port)) #Socket oppkobling
print('Send command til roboten, skriv exit for å avslutte programmet')
while(msg != 'exit'):
 msg = Dis
 client.send(bytes(msg,'utf-8')) #Sender data til robotstudio

client.close()
