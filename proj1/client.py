#!/usr/bin/python
import sys
import socket


def countEmUp(str, char):
    count = 0
    for i in str:
        if i == char:
            count = count + 1
    return count


def checkHost(host):
    if host[0].isdigit():
        period_count = 0;
        for c in host:
            if (c.isalpha()):
                return False;
            if (c == '.'):
                period_count = period_count + 1
        if period_count == 3:
            return True;
    else:
        if '.' in host:
            return True
        else:
            return False


def checkNUID(s_num):
    return len(s_num) == 9


def main():
    TCP_IP = 'cbw.sh'
    TCP_PORT = 27993
    NU_ID = '001706409'
    print('Argument List:', str(sys.argv))
    if len(sys.argv) < 3:
        print("not enough arguments")
        print(RESP)
	
    elif len(sys.argv) == 3:
        if checkHost(sys.argv[1]) and checkNUID(sys.argv[2]):
            TCP_IP = sys.argv[1]
            NU_ID = sys.argv[2]
        else:
            print("either the host or the NUID was enterred incorrectly, please try again")
        print("Host: ", sys.argv[1])
        print("NUID: ", sys.argv[2])
    elif len(sys.argv) == 4:
        if checkHost(sys.argv[2]) and checkNUID(sys.argv[3]):
            TCP_IP = sys.argv[2]
            NU_ID = sys.argv[3]
            TCP_PORT = sys.argv[1]
        else:
            print("either the host or the NUID was enterred incorrectly, please try again")
        print("Port: ", sys.argv[1])
        print("Host: ", sys.argv[2])
        print("NUID: ", sys.argv[3])

    BUFFER_SIZE = 41024
    MESSAGE = ('cs3700spring2019 HELLO ' + NU_ID + '\n').encode('utf-8')
    COUNT_MESSAGE = 'cs3700spring2019 COUNT '
    RESP = bytearray()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    # print('connection successful')

    s.sendall(MESSAGE)
    while True:
        data = s.recv(BUFFER_SIZE)
        RESP = bytearray(data)
#	print("pre: ", RESP)
#	RESP = RESP.decode()
      #  if RESP[len(RESP) - 1] != '\n':
       #     print("response was ill-formatted")
        #    print(RESP)
    	 #   break;
        if RESP[:22] == 'cs3700spring2019 FIND ' and RESP[23] == 32 and len(RESP) > 24:
            # print("is find")
            toSend = COUNT_MESSAGE + str(countEmUp(RESP[24:], RESP[22])) + "\n"
            # print(toSend)
            s.sendall(toSend.encode())
        elif RESP[:21] == 'cs3700spring2019 BYE ' and len(RESP[22:]) == 64:
            print(RESP[21:])
            break;
        else:
            print("there was an issue, error in response codes")
	    print("basic tests:")
	    print(RESP[0:20]);
	    print("bool checks: ")
            print("FIND CHECK 1: ", RESP[:22] == 'cs3700spring2019 FIND ', "||", RESP[:22])
	    print("FIND CHECK 2: ", RESP[23] == 32, RESP[23])
	    print("FIND CHECK 3: ", len(RESP) > 24)
	    print("BYE CHECK 1: ", RESP[:21] == 'cs3700spring2019 BYE ', RESP[:21])
	    print("BYE CHECK 2: ", len(RESP[22:]) == 64, len(RESP[22:])) 
  	    break;

    s.close()


main()

