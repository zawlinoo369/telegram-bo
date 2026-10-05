import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = "8838268089:AAFx0PGzpuSGGECQPjZbbh9wdSQtS4Asb94"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("မင်္ဂလာပါ။ ဒီ Bot က Group ထဲမှာ Link ပို့ရင် အလိုအလျောက် ဖျက်ပေးပါမည်။")

async def delete_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or update.message.caption or ""
    
    if "http://" in text or "https://" in text or "t.me/" in text:
        try:
            await update.message.delete()
            user = update.message.from_user.first_name
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"⚠️ {user}၊ Group ထဲတွင် Link ပို့ခွင့်မရှိပါ။"
            )
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_links))
    
    print("Link Auto Delete Bot စတင်အလုပ်လုပ်နေပါပြီ...")
    app.run_polling()
