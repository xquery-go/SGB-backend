#!/usr/bin/env python
import glob
import os.path
import socket
import subprocess
import sys

SERVERS = (
    # ('[::]', 50051, 'iam', 'rungrpcserver'),
    ('0.0.0.0', 8001, 'iam', 'runserver'),
    ('0.0.0.0', 8002, 'sgb', 'runserver'),
)

PORT_START = 8000

cwd = os.path.abspath(os.path.dirname(__file__))

servers_clean = []
last_port = PORT_START
for server in SERVERS:
    ip = server[0] or '0.0.0.0'
    if server[1]:
        port = server[1]
    else:
        while True:
            try:
                s = socket.socket()
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((ip, last_port))
                s.close()
                break
            except OSError:
                last_port += 1
        port = last_port
        last_port += 1
    path = server[2]
    manage_py = glob.glob(cwd + f'/{path}/manage.py')
    cmd = server[3:]
    try:
        subprocess.Popen(
            (
                manage_py[0],
                *cmd,
                '{}:{}'.format(ip, port),
            ), cwd=cwd,
        )
    except IndexError:
        print('Cannot find manage.py')
        sys.exit(1)

try:
    while True:
        pass
except KeyboardInterrupt:
    print('All %d servers terminated' % len(SERVERS))
