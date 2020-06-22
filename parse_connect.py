import socket

import sys

import argparse


def ploadconnect(websiteN, portN):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created successfully")
    except socket.error as err:
        print("Socket creation failed with error %s" % (err))

    port = portN

    try:
        host_ip = socket.gethostbyname(websiteN)
    except socket.gaierror:
        print("There is a problem resolving theh ost")
        sys.exit()

    s.connect((host_ip.port));
    print("Successfully connected to the website given %s.%s" % (host_ip.port));


parser = argparse.ArgumentParser(description="Learn to connect to a website with port number");

parser.add_argument("-H", "--host", required=True, help="specify the hostname or website name");

parser.add_argument("-p", "--port", type=int, default=80, help="specify the port number eg.80 for website");

args= parser.parse_args();
ploadconnect(args.host, args.port);