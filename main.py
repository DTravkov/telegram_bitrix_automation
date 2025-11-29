import asyncio
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from calls import fetch_leads_list

load_dotenv(".venv/envar.env")
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")


async def get_leads(update: Update, context: ContextTypes.DEFAULT_TYPE):

    leads_list = await fetch_leads_list(True)

    for lead in leads_list:
        await lead.send_message(update)


if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_API_KEY).build()

    app.add_handler(CommandHandler('get_leads', get_leads))

    app.run_polling()