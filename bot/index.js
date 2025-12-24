const TelegramBot = require('node-telegram-bot-api');
const TOKEN = "8535059336:AAGKtDypCIPi_XPQldquNlSNRu7KZb4HwJM";
const bot = new TelegramBot(TOKEN, { polling: true });

bot.on('message', (msg) => {
  bot.sendMessage(msg.chat.id, 'سڵاو 👋 بۆت کاردەکات');
});
