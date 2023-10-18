// Desenvoldo por: Bee Solutions //
// Autor: Fernando Almondes //
// Data: 07/07/2023 //
// Aqui voce pega a lista de grupos e ids //

const { Client, LocalAuth } = require('whatsapp-web.js');

//const client = new Client();

const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: { args: ['--no-sandbox'] }
});

client.on('ready', async () => {
  console.log('Cliente está pronto!');

  try {
    // Obter lista de chats
    const chats = await client.getChats();

    // Filtrar apenas grupos
    const groupChats = chats.filter(chat => chat.isGroup);

    // Obter lista de IDs e nomes de grupos
    const groupInfo = groupChats.map(chat => ({ id: chat.id._serialized, name: chat.name }));

    console.log('Lista de IDs e nomes de grupos:', groupInfo);
  } catch (error) {
    console.error('Erro ao obter a lista de IDs e nomes de grupos:', error);
  }

  // Encerrar a sessão após obter os IDs e nomes dos grupos
  client.destroy();
});

client.initialize();