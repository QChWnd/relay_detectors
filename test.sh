#!/bin/bash

apt install -y python3 python3-openssl

wget -O ehco_test "https://github.com/Ehco1996/ehco/releases/download/v1.1.2/ehco_1.1.2_linux_amd64"
chmod +x ehco_test

echo "Begin: ehco ws test"
./ehco_test -l "127.0.0.1:2333" -lt ws -r "127.0.0.1:2333" &> /dev/null &
sleep 3
python3 ehco.py --host "127.0.0.1" --port "2333"
pkill ehco_test
sleep 1
echo ""

echo "Begin: ehco wss test"
./ehco_test -l "127.0.0.1:2333" -lt wss -r "127.0.0.1:2333" &> /dev/null &
sleep 3
python3 ehco.py --host "127.0.0.1" --port "2333" --tls
pkill ehco_test
sleep 1
echo ""

echo "Begin: ehco mwss test"
./ehco_test -l "127.0.0.1:2333" -lt mwss -r "127.0.0.1:2333" &> /dev/null &
sleep 3
python3 ehco.py --host "127.0.0.1" --port "2333" --tls
pkill ehco_test
sleep 1
echo ""

rm -f ehco_test

wget -O gost_test.gz "https://github.com/ginuerzh/gost/releases/download/v2.11.5/gost-linux-amd64-2.11.5.gz"
gzip -d gost_test.gz
chmod +x gost_test

echo "Begin: gost ws test"
./gost_test -L "relay+ws://127.0.0.1:2333/127.0.0.1:2333" &> /dev/null &
sleep 3
python3 gost.py --host "127.0.0.1" --port "2333"
pkill gost_test
sleep 1
echo ""

echo "Begin: gost wss test"
./gost_test -L "relay+wss://127.0.0.1:2333/127.0.0.1:2333" &> /dev/null &
sleep 3
python3 gost.py --host "127.0.0.1" --port "2333" --tls
pkill gost_test
sleep 1
echo ""

echo "Begin: gost mws test"
./gost_test -L "relay+mws://127.0.0.1:2333/127.0.0.1:2333" &> /dev/null &
sleep 3
python3 gost.py --host "127.0.0.1" --port "2333"
pkill gost_test
sleep 1
echo ""

echo "Begin: gost mwss test"
./gost_test -L "relay+mwss://127.0.0.1:2333/127.0.0.1:2333" &> /dev/null &
sleep 3
python3 gost.py --host "127.0.0.1" --port "2333" --tls
pkill gost_test
sleep 1
echo ""
