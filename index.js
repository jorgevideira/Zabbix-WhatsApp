// Desenvoldo por: Bee Solutions //
// Autor: Fernando Almondes //
// Data: 07/07/2023 //
// Inicie primeiro o index para salvar a sessao | Leia o qrcode gerado //

const qrcode = require('qrcode-terminal');
const { Client, LocalAuth } = require('whatsapp-web.js');

//const client = new Client();
const client = new Client({
        authStrategy: new LocalAuth(),
        puppeteer: { args: ['--no-sandbox'] }
});

client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});


client.initialize();

client.on('loading_screen', (percent, message) => {
    console.log('Carregando', percent, message);
});

client.on('authenticated', () => {
    console.log('Autenticado');
});

client.on('auth_failure', msg => {
    // Fired if session restore was unsuccessful
    console.error('Falha na autenticacao', msg);
});

client.on('ready', () => {
    console.log('Cliente iniciado e pronto para uso!');
});