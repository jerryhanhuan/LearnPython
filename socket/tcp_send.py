
import socket,sys



def main():
    ip,port = sys.argv[1],int(sys.argv[2])
    print('hsm ip:%s port:%d'%(ip,port))
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        sock.connect((ip,port))
        while True:
            cmdstr = input('send:')
            d_len = len(cmdstr)
            b_len = bytearray()
            b_len.append(d_len//256)
            b_len.append(d_len%256)
            data = bytes(b_len) + cmdstr.encode()
            sock.send(data)
            recv_len_b = sock.recv(2)
            r_len = recv_len_b[0]*256+recv_len_b[1]
            recv_data = sock.recv(r_len).decode()
            if not recv_data:
                break
            else:
                print('recv:%s'%recv_data)
        sock.close()

if __name__ == '__main__':
    main()
