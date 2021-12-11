from flask import Flask, render_template
import socket
import datetime
import random
import os
import time
import requests

import dns.resolver
from dns.exception import DNSException

app = Flask(__name__)

def nsresolve(hostname, ns=None, qtype='a'):
    ips = list()
    my_resolver = dns.resolver.Resolver()
    if ns:
        my_resolver.nameservers = [ns]
    try:
        answer = my_resolver.query(hostname, qtype)
        for rr in answer.rrset:
            ips.append(rr.to_text())
        return ips
    except DNSException:
        return None

def myip():
    # url = 'https://diagnostic.opendns.com/myip'
    url = 'https://ifconfig.me/'

    while True:
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException:
            time.sleep(1)
            pass
        if r.status_code == 200:
            return r.text
        else:
            time.sleep(5)


@app.route('/')
def index():
    domain = os.getenv("DOMAIN", "he.okerr.com")
    fqdn = os.getenv("FQDN", "cat.he.okerr.com")
    role = os.getenv('ROLE', 'main')
    host = socket.gethostname()
    status = 'OK'
    local_ip = os.getenv('MYIP', myip())
    failstart = os.getenv('FAILSTART', None)

    if failstart is not None:
        failstart = int(failstart)

    #
    # Resolve
    # 

    # get list of auth NS servers    
    nslist = None
    while nslist is None:
        nslist = nsresolve(domain, qtype='ns')
        if nslist is None:
            # tmp failure
            time.sleep(1)

    # get random NS
    ns = None
    while ns is None:
        nsname = random.choice(nslist)
        try:
            ns = nsresolve(nsname)[0]
        except TypeError:
            # nsresolve returned None
            time.sleep(1)
            pass

    # resolve cat.he.okerr.com
    nsip_struct = nsresolve(fqdn, ns)
    if nsip_struct:
        catip = nsip_struct[0]
    else:
        catip = '<not resolved>'

    # decide status
    now = datetime.datetime.now()
    if failstart is None:
        status = 'OK'
        left = None
    else:
        if now.minute >= failstart:
            status = 'ERR'
            left = 60 - now.minute
        else:
            status = 'OK'
            left = failstart - now.minute

    return render_template('index.html',
        role=role,
        host=host,
        nsname = nsname,
        catip = catip,
        status=status,
        left=left,
        timestr=now.strftime('%H:%M:%S'),
        local_ip=local_ip
    )
