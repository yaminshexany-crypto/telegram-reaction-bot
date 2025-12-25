import os
import logging
import random
import asyncio
from telegram import ReactionTypeEmoji
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    logger.error('TELEGRAM_BOT_TOKEN environment variable is not set')
    raise SystemExit('TELEGRAM_BOT_TOKEN environment variable is required')

REACTION_EMOJIS = ["🔥", "❤️", "👍", "🎉", "👏", "🤩", "🏆", "⭐", "💯", "❤️‍🔥"]

async def start(update, context):
    user = update.effective_user
    welcome_message = (
        f"👋 سڵاو @{user.username or user.first_name}\n"
        f"بەخێربێیت بۆ بۆتەکەم\n\n"
        f"🔗 ئەم بۆتە لە توانای داهەیە ڕیاکت بۆ پۆستەکانی کەناڵ زیاد بکات\n"
        f"👌 ئێستا ئەتوانی بۆتەکە بەکار بهێنی\n\n"
        f"📌 پێویستە بۆت بکەیت بە ئەدمین لە کەناڵەکەدا.\n"
        f"🎭 بۆت خۆکارانە ڕیاکت زیاد دەکات بۆ پۆستەکانت\n"
        f"❤️‍🔥 بەهیوای کاتێکی خۆش بۆ تۆ 🙂"
    )
    await update.message.reply_text(welcome_message)
    logger.info(f"User @{user.username or user.first_name} started the bot")

async def handle_channel_post(update, context):
    if update.channel_post:
        msg = update.channel_post
    elif update.edited_channel_post:
        msg = update.edited_channel_post
    else:
        return

    try:
        chat_title = msg.chat.title or f"ID: {msg.chat.id}"
        logger.info(f"Channel post in: {chat_title}")

        selected_emoji = random.choice(REACTION_EMOJIS)
        logger.info(f"Selected emoji: {selected_emoji}")

        await asyncio.sleep(5)

        await context.bot.set_message_reaction(
            chat_id=msg.chat.id,
            message_id=msg.message_id,
            reaction=[ReactionTypeEmoji(selected_emoji)],
            is_big=False
        )

        logger.info(f"Added reaction '{selected_emoji}'")

    except Exception as e:
        logger.error(f"Failed to add reaction: {e}")
        try:
            await asyncio.sleep(1)
            await context.bot.set_message_reaction(
                chat_id=msg.chat.id,
                message_id=msg.message_id,
                reaction=[ReactionTypeEmoji("❤️‍🔥")],
                is_big=False
            )
            logger.info("Added fallback reaction")
        except Exception as e2:
            logger.error(f"Fallback reaction failed: {e2}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ChatType.CHANNEL, handle_channel_post))

    logger.info("Starting bot (polling). Make sure TELEGRAM_BOT_TOKEN is set in environment.")
    # run_polling blocks and handles startup/shutdown gracefully
    app.run_polling(poll_interval=0.5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
