#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_client.py
#Created Time:2019-07-21 02:24:28


import socket,sys



def main():
    ip,port = sys.argv[1],int(sys.argv[2])
    print('ip:%s port:%d'%(ip,port))
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        sock.connect((ip,port))
        while True:
            data = input('send:')
            sock.send(data.encode())
            recv_data = sock.recv(1024)
            if not recv_data:
                break
            else:
                print('recv:%s'%recv_data)
        sock.close()

if __name__ == '__main__':
    main()



