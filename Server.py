# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 19:20:24 2019

@author: PIYUSH BHOI
"""


import socket  
import sys
from _thread import *
import threading 
  
count = 1

thread_lock = threading.Lock() 
def threaded(c):
    global count 
    data = ''
    buf = b''
    while True: 
        #print('Server: ')
        data = str(c.recv(4096).decode('ascii')) 
        print('Client ',count,':', data)
        if not data: 
            print('No Connection ',count) 
            thread_lock.release() 
            break

        if data == 'fail':
            count += 1
            c.close()
            print('Connection failed')
            thread_lock.release()
            break
        data = input('Server : ')
        c.send(data.encode('ascii')) 
  
    # connection closed 
    c.close() 
  
  
def Main(): 
    host = "" 
    port = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("Socket binded to the port:", port) 
  
    s.listen(5) 
    print("Connection Established") 
   
    while True: 
        c, addr = s.accept() 

        thread_lock.acquire() 
        # print('Connected to :', addr[0], ':', addr[1]) 

        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 