# 📲 Zabbix WhatsApp Alerts

Envio de alertas do Zabbix via WhatsApp utilizando [`whatsapp-web.js`](https://github.com/pedroslopez/whatsapp-web.js).

> 💡 Testado no **Debian 12**

---

## 📁 Estrutura de Diretórios

Crie o diretório onde o projeto será instalado:

```bash
mkdir -p /opt/whatsapp
cd /opt/whatsapp
```

---

## 🧰 Pré-requisitos

Instale os pacotes necessários:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential curl libgbm-dev libvulkan1 gnupg ca-certificates
```

---

## 🌐 Instalação do Google Chrome

O `whatsapp-web.js` requer um navegador para funcionar corretamente. Instale o Google Chrome com os comandos abaixo:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

---

## ⚙️ Instalação do Node.js e NPM

Use o repositório oficial do NodeSource:

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo bash -
sudo apt install -y nodejs
```

Verifique as versões:

```bash
node -v
npm -v
```

---

## 📦 Instalação de dependências do projeto

```bash
npm install -g pm2
npm install -g n         # Gerenciador de versões do Node.js
n latest                 # Atualiza para a última versão do Node.js

npm init -y

npm install whatsapp-web.js express qrcode-terminal multer moment-timezone
```

---

## 🧾 Configuração do Projeto

1. Copie os arquivos `index.js` e `whatsapp-service.js` para o diretório `/opt/whatsapp`.

2. Altere a fonte do pacote `whatsapp-web.js` para a versão mais recente no GitHub:

```bash
vi package.json
```

Substitua:

```json
"whatsapp-web.js": "^..."
```

Por:

```json
"whatsapp-web.js": "github:pedroslopez/whatsapp-web.js"
```

3. Atualize o pacote:

```bash
npm update whatsapp-web.js
```

4. Edite o arquivo de constantes:

```bash
vi /opt/whatsapp/node_modules/whatsapp-web.js/src/util/Constants.js
```

Altere o trecho:

```js
webVersionCache: {
  type: 'local',
},
```

Para:

```js
webVersionCache: {
  type: 'remote',
  remotePath: 'https://raw.githubusercontent.com/wppconnect-team/wa-version/main/html/2.2412.54.html',
},
```

---

## 🔐 Login no WhatsApp

Execute:

```bash
node index.js
```

Escaneie o QR Code com o WhatsApp e aguarde até que o login seja concluído. Aperte ctrl+c e Repita o processo, se necessário, até não solicitar mais o QR Code.

---

## 🚀 Executando a API em segundo plano

Use o `pm2` para manter o serviço ativo:

```bash
pm2 start whatsapp-service.js
pm2 status
pm2 logs
```

---

## 🧪 Teste de Envio de Mensagens

Faça um teste via navegador ou ferramenta HTTP:

```
http://<ip-do-servidor>:4000/api/message?number=<numero-ou-id-do-grupo>&message=Bee
```

---

## 🛠️ Integração com o Zabbix

1. Importe o tipo de mídia `alertas_WhatsApp.xml` no Zabbix.

2. Copie o script de alerta:

```bash
cp whatsapp-script.sh /usr/lib/zabbix/alertscripts/
chmod +x /usr/lib/zabbix/alertscripts/whatsapp-script.sh
```

3. Ou Importe o xml webhook-mediatype-whatsapp.xml, no media type, para ter um media type do tipo webhook

3. Crie uma action no Zabbix para envio de alertas via WhatsApp utilizando o novo tipo de mídia.

---

## 🙌 Créditos

- [whatsapp-web.js (pedroslopez)](https://github.com/pedroslopez/whatsapp-web.js)
- [jorgevideira](https://github.com/jorgevideira)
