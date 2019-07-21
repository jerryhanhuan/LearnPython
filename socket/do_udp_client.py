#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#File Name:do_udp_client.py
#Created Time:2019-07-21 04:37:59


import socket,sys


def main():
    ip = sys.argv[1]
    port = int(sys.argv[2])
    addr = (ip,port)
    while True:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        while True:
            data = input('send:')
            sock.sendto(data.encode(),addr)
            recv_data,cli_addr = sock.recvfrom(1024)
            if not recv_data:
                break
            else:
                print('recv data:%s'%recv_data.decode())
        sock.close()

if __name__ == '__main__':
    main()


