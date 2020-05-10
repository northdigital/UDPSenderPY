import socket
import time
import sys

UDP_IP_ADDRESS = "192.168.1.202"
UDP_PORT_NO = 7777

def main():
  clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  clientSock.sendto(sys.argv[1].encode("utf8"), (UDP_IP_ADDRESS, UDP_PORT_NO))
  time.sleep(1)
  answer = clientSock.recvfrom(4096)[0].decode("utf8")
  print(answer)

if __name__ == "__main__":
  main()
