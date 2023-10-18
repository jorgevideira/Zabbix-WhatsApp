#!/bin/python3

#Desenvolvido por: Bee Solutions em parceria com o ChatGPT #
#Author: Fernando Almondes #
#Nome: beebot.py
#Data: 27/06/2023 3h30m #

#### INICIO DAS INTRUCOES ####

# Testado no Debian 11 e Ubuntu Server 20.04 ou 22.04
# Crie o diretorio padrao: mkdir /var/tmp/zabbix
# Deem permissao ao diretorio para o Zabbix: chown -R zabbix:zabbix /var/tmp/zabbix
# Deem permissao de execucao ao script: chmod +x /usr/lib/zabbix/alertscripts/beebot.py
# Instale as dependencias: apt install python3-pip && pip install requests
# Testando script beebot.py: python3 /usr/lib/zabbix/alertscripts/beebotzap.py "Bee Solutions Item ID: 12345" "Titulo da mensagem de Teste" "SEU-CHAT-ID-DO-WHATSAPP"
# Lembre-se de importar o tipo de midia para o Zabbix, criar a Trigger Action e incluir o seu CHAT-ID do WhatsApp em Media no Profile do usuario do Zabbix

#### FIM DAS INSTRUCOES ####

import os
import re
import sys
import json
import requests

# Obtém os argumentos da linha de comando
mensagem = sys.argv[1]
titulo = sys.argv[2]
chat_id = sys.argv[3]

#### Inicio Declaracao de variaveis ####

token = 'TOKEN-API-ZAP-CLIENTE'

# URL base do Zabbix e API
zabbix_url = 'http://127.0.0.1/zabbix'
api_url = 'http://127.0.0.1:4000/api/download'

# Informacoes do cliente
number = f'{chat_id}' # Chatid
caption = f'{titulo}\n\n{mensagem}' # Legenda da mensagem
destination = 'uploads/bee/' # Diretorio do cliente

# Credenciais de login
username = 'USUARIO-ZABBIX-COM-PERMISAO'
password = 'SENHA-ZABBIX'

graph_directory = '/var/tmp/zabbix/'

#### Fim da declaracao de variaveis ####

# Função para extrair o item_id da mensagem
def extract_item_id(mensagem):
    # Procura o padrão "Item ID: <item_id>" na mensagem
    match = re.search(r'Item ID:\s*(\d+)', mensagem)
    if match:
        # Extrai o valor do item_id
        item_id = match.group(1)
        return item_id
    else:
        return None

# Extrai o item_id da mensagem
item_id = extract_item_id(mensagem)

print('\n\n\nItem ID:', item_id)

# Verifica se o item_id foi encontrado na mensagem
#if item_id is None:
#    print('Item ID não encontrado na mensagem')
#    exit()

# URL do login
login_url = f'{zabbix_url}/index.php'

# Dados do formulário de login
login_data = {
    'name': username,
    'password': password,
    'enter': 'Sign in',
    'autologin': 1,
    'request': login_url
}

# Sessão do requests
session = requests.Session()

# Faz login
response = session.post(login_url, data=login_data)

# Verifica se o login foi bem-sucedido
if 'Falha no login' in response.text:
    print('Falha no login')
    exit()

# URL do gráfico específico
# Item
graph_url = f'{zabbix_url}/chart.php?from=now-1h&to=now&&itemids[0]={item_id}&type=0&profileIdx=web.charts.filter'

# Faz a requisição do gráfico
graph_response = session.get(graph_url)

# Verifica se a requisição foi bem-sucedida
if graph_response.status_code != 200:
    print('Falha ao obter o gráfico')
    exit()

# Caminho completo para salvar o arquivo do gráfico
graph_filename = os.path.join(graph_directory, f'graph_{item_id}.png')

with open(graph_filename, 'wb') as file:
    file.write(graph_response.content)

print(f'O gráfico foi salvo em {graph_filename}')

filepath = f'graph_{item_id}.png' # Nome do arquivo

data = {'number': number, 'caption': caption, 'filepath': filepath, 'destination': destination}

headers = {'Content-Type': 'application/json'}

# Arquivo a ser enviado
arquivo = f'{graph_filename}'

# Envia a requisição com o arquivo e os dados anexados
with open(arquivo, 'rb') as file:
    files = {'file': file}
    #headers = {'Authorization': 'Bearer ' + token}
    response = requests.post(api_url, data=data, files=files)

if response.status_code == 200:
    print('Arquivo enviado com sucesso')
else:
    print('Erro ao enviar o arquivo:', response.text)