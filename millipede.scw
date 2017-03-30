#!/bin/bash

set -e

echo "[+] Creating your millipede server..."
SERVER=$(scw create --name="millipede" ubuntu-trusty)
echo "[+] Server created: ${SERVER}"

echo "[+] Booting..."
scw start --wait --timeout=600 "${SERVER}" >/dev/null
echo "[+] Server is booted"

echo "[+] Installing millipede..."
scw exec "${SERVER}" 'apt-get -q update && apt-get --force-yes -y -qq upgrade && apt-get install -y -qq python-pip  && pip install millipede'
echo "[+] Running millipede"
scw exec "${SERVER}" 'millipede 20 "My millipede is magnificent"'

echo "[+] Stopping the server"
scw stop "${SERVER}" >/dev/null
scw wait "${SERVER}"
echo "[+] Server stopped"

echo "[+] Deleting server"
scw rm "${SERVER}" >/dev/null
echo "[+] Server deleted"
