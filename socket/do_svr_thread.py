#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_svr_thread.py
#Created Time:2019-07-20 14:59:07


import socket,threading
import os,signal



def tcp_handle(sock,addr):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        else:
            print('threading %s recv data:%s'%(threading.current_thread().name,data.decode('utf-8')))
        sock.send(b'Welcome to Python\n')
    sock.close()
    print('connection from %s:%s closed.'%addr)

def tcp_listen_thread(args):
        sock = args
        print('Waiting for New connection...')
        while True:
            new_sock,cli_addr = sock.accept()
            print('threading %s accetp from: %s:%d'%(threading.current_thread().name,cli_addr[0],cli_addr[1]))
            t = threading.Thread(target = tcp_handle,args = (new_sock,cli_addr))
            t.start()



def tcp_bind(ip,port):
    addr = (ip,port)    
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # reuse addrress
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind(addr)
    return sock


def main():
#    signal.signal(signal.SIGINT,signal.SIG_IGN)
    ip = '0.0.0.0'
    port = int(input('请输入端口:'))
    sock = tcp_bind(ip,port)
    sock.listen(10)
    t = threading.Thread(target = tcp_listen_thread, args = (sock,))
    t.start()
    t.join()


if __name__ == '__main__':
    main()











