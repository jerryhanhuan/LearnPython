#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_svr.py
#Created Time:2019-07-20 14:17:19




import socket


def main():
    port = int(input('Please Input port:'))
    addr = '0.0.0.0'
    ADDR =(addr,port)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # bind
    s.bind(ADDR)
    # listen
    s.listen(10)

    while True:
        print('Waiting for connection......')
        sock,cli_addr = s.accept()
        print('New Client addr:',cli_addr)
        while True:
            data = sock.recv(1024)
            if not data:
                break
            else:
                print('recv data %s'%data.decode('utf-8'))
            sock.send(b'Welcome to Python Server\n')
        sock.close()
    s.close()


if __name__ == '__main__':
    main()
