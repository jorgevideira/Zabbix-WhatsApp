# Zabbix-WhatsApp
Envio de alertas do Zabbix via WhatsApp 


# Criar um diretório

mkdir /opt/beezap2

cd /opt/beezap2

# Instalar build-essential e curl

apt-get install -y build-essential curl

# Instalar a lib libgbm-dev

apt-get install -y libgbm-dev

# Instalar o google Chrome

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

apt install -y pacote baixado

dpkg -i pacote_baixado

# Instalar NPM e dependencias

apt install npm

npm install -g pm2

npm install -g n --> Instalar o node

n latest --> Atualizar o node

npm init -y

npm install whatsapp-web.js

npm install express

npm install qrcode-terminal

npm install multer

npm install moment-timezone

# --------fora da imagem--------

copiar o arquivo index.js para /opt/zap

copiar o arquivo beezap2.js para /opt/zap

importar no zabbix um tipo de midia --> alertas whatsapp - xml

# Iniciar o qrcode 

node index.js 

# testar node beezap2.js --> 25 minutos
node  beezap2.js

Esperar o serviço subir e dar a mensagem de autenticado.


Vincular o numero do cel ou do grupo ao usuário escolhendo o tipo de midia como alertas Whatsapp


# criar uma action 

no diretorio de scripts do zabbix /usr/lib/zabbix/alertscripts copiar o script beezap2.sh e dar permissão de execução chmod +x

Teste o envio de mensagem

http://ip-onde-esta-rodando-o-node:4000/api/message?number=numero-ou-id-do-grupo&message=Bee


# Altere a fonte da API para direto do Github
nano package.json
"whatsapp-web.js": "github:pedroslopez/whatsapp-web.js"

# Atualizando o whatsapp-web.js
npm update whatsapp-web-js

# Faça o login no WhatsApp
node index.js


# Rodar em segundo plano 

pm2 start beezap2.js

pm2 status 

pm2 logs
-----------------------------------------------------------------------------------------------------------------------

## centos

# Criar um diretório
mkdir /opt/beezap2
cd /opt/beezap2

# Instalar as ferramentas de desenvolvimento e curl
yum groupinstall -y "Development Tools"
yum install -y curl

# Instalar a lib libgbm-dev
yum install -y mesa-libgbm mesa-libgbm-devel

# Instalar o google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
yum localinstall -y google-chrome-stable_current_x86_64.rpm

# Instalar npm
curl -sL https://rpm.nodesource.com/setup_14.x | bash -
yum install -y nodejs

# Instalar pm2 e n globalmente
npm install -g pm2 n

# Atualizar o node
n latest

# Inicializar o projeto Node.js e instalar as dependências necessárias
npm init -y
npm install whatsapp-web.js express qrcode-terminal multer moment-timezone

# Copiar os arquivos index.js e beezap2.js para /opt/zap (você precisa ter esses arquivos disponíveis)
cp index.js /opt/zap
cp beezap2.js /opt/zap

# Iniciar o qrcode 
node index.js 

# Testar node beezap2.js --> 25 minutos
node beezap2.js 

# Alterar a fonte da API para direto do Github no arquivo package.json
sed -i 's/"whatsapp-web.js": ".*"/"whatsapp-web.js": "github:pedroslopez/whatsapp-web.js"/' package.json

# Atualizar o whatsapp-web.js
npm update whatsapp-web-js

# Fazer login no WhatsApp novamente
node index.js 


