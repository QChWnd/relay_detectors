# only for ehco **default** ws/wss/mwss
import requests
import argparse
import warnings
import os
import ssl
import OpenSSL
import datetime
from Lib.jarm import jarm
warnings.filterwarnings('ignore')
parser = argparse.ArgumentParser()
parser.add_argument('--host', required=True)
parser.add_argument('--port', required=True)
parser.add_argument('--tls', action='store_true')
args = parser.parse_args()
if args.tls:
    if jarm(args.host, int(args.port)) == '3fd21b20d3fd3fd21c43d21b21b43d1ec49a4b64df0a9e9f328abd60285841':
        print('Go jarm matched')
    else:
        print('Go jarm mismatched')
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, ssl.get_server_certificate((args.host, args.port)))
    if cert.get_version() == 2 and cert.get_signature_algorithm() == b'sha256WithRSAEncryption' and cert.get_pubkey().bits() == 2048 and datetime.datetime.strptime(cert.get_notAfter().decode("ascii"), '%Y%m%d%H%M%SZ').timestamp() - datetime.datetime.strptime(cert.get_notBefore().decode("ascii"), '%Y%m%d%H%M%SZ').timestamp() == 31536000:
        print('certificate matched')
    else:
        print('certificate mismatched')
    certIssue = cert.get_issuer()
    if certIssue.commonName == None:
        print('certificate issue matched')
    else:
        print('certificate issue mismatched')
    r = requests.get('http://' + args.host + ':' + args.port)
    if r.status_code == 400 and r.content == b'Client sent an HTTP request to an HTTPS server.\n':
        print('http matched')
    addr = 'https://' + args.host + ':' + args.port
    r = requests.get(addr, verify=False)
    if r.status_code == 200 and r.content.decode('utf-8')[:12] == 'access from ':
        print('route / matched')
    else:
        print('route / mismatched')
    r = requests.get(addr + '/' + os.urandom(8).hex(), verify=False)
    if r.status_code == 404 and r.content == b'404 page not found\n':
        print('route /[random] matched')
    else:
        print('route /[random] mismatched')
    r = requests.get(addr + '/wss/', verify=False)
    if r.status_code == 400 and r.content == b'handshake error: bad "Upgrade" header':
        print('route /wss/ matched')
    else:
        print('route /wss/ mismatched')
    r = requests.get(addr + '/mwss/', verify=False)
    if r.status_code == 400 and r.content == b'handshake error: bad "Upgrade" header':
        print('route /mwss/ matched')
    else:
        print('route /mwss/ mismatched')
else:
    addr = 'http://' + args.host + ':' + args.port
    r = requests.get(addr)
    if r.status_code == 200 and r.content.decode('utf-8')[:12] == 'access from ':
        print('route / matched')
    else:
        print('route / mismatched')
    r = requests.get(addr + '/' + os.urandom(8).hex())
    if r.status_code == 404 and r.content == b'404 page not found\n':
        print('route /[random] matched')
    else:
        print('route /[random] mismatched')
    r = requests.get(addr + '/ws/')
    if r.status_code == 400 and r.content == b'handshake error: bad "Upgrade" header':
        print('route /ws/ matched')
    else:
        print('route /ws/ mismatched')
