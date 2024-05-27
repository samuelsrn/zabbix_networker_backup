#!/usr/bin/env python3

import paramiko
from datetime import datetime, timedelta
import json
import os

# Informação da conexão SSH
hostname = ""
username = ""
password = ""

# Buscar hora do sistema
buscar_hora = datetime.now()
buscar_hora = buscar_hora - timedelta(hours=1)
hora = buscar_hora.strftime('%m/%d/%y %H')

# Diretorio do arquivo de log
diretorio_log = ""

# Comando de Busca
commands = [
    f"cat {diretorio_log} | grep -i 'workflow name:' | grep -i failed | grep -i '{hora}'"
]

# Conexão SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Não é possível conectar-se ao servidor SSH")
    exit()

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    # Recebe os dados de retorno out grava na variavel
    saida = (stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)

# Divide por linha
linhas = saida.strip().split("\n")

dados = []

# Divide por ','
for linha in linhas:
    partes = linha.split(", ")
    linha_dados = {}
    # Divide pelo primeiro ':'
    for parte in partes:
        chave, valor = parte.split(":", 1)
        chave = chave.strip()
        linha_dados[chave] = valor
    # armazena no objeto
    dados.append(linha_dados)
# converte em json
saida_json = json.dumps(dados, indent=4)

# Diretorio do json
diretorio_json = ""

arquivo_json = os.path.join(diretorio_json, 'jobs.json')
with open(arquivo_json, 'w') as f:
    f.write(saida_json)
