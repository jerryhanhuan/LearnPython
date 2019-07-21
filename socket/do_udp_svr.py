#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_udp_svr.py
#Created Time:2019-07-21 03:44:33


import socket,sys,threading



def udp_server(port):
    while True:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sock.bind(('0.0.0.0',port))
        while True:
            data,addr = sock.recvfrom(1024)
            print('recvfrom %s:%s'%addr)
            if not data:
                break
            else:
                print('recv:%s'%data.decode())
            send_data = input('send:')
            sock.sendto(send_data.encode(),addr)
        sock.close()


def main():
    port = int(sys.argv[1])
    t = threading.Thread(target = udp_server,args = (port,))
    t.start()
    t.join()



if __name__ == '__main__':
    main()



