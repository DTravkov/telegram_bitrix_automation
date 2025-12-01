import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from calls import fetch_leads_list, lead_add_comment_by_id, lead_add_task_by_id

load_dotenv(".venv/envar.env")
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")


async def get_leads(update: Update, context: ContextTypes.DEFAULT_TYPE):

    leads_list = await fetch_leads_list(True)

    for lead in leads_list:
        await lead.send_message(update)


async def button_handler(update : Update, context:ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()  
    
    data = query.data


    answer_text = ""
    comment_text = ""
    lead_id = data.split('_')[1]
    
    if data.startswith("called"):
        answer_text = "This lead is now commented as Called"
        comment_text = "Manager called"

        await lead_add_comment_by_id(lead_id, comment_text)

    elif data.startswith("wrote"):
        answer_text = "This lead is now commented as Wrote"
        comment_text = "Manager wrote"

        await lead_add_comment_by_id(lead_id, comment_text)

    elif data.startswith("postponed"):
        answer_text = "This lead is postponed for 2 hours"
        await lead_add_task_by_id(lead_id,"test text for the task")

    await query.edit_message_text(text=answer_text)
    

    



if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_API_KEY).build()

    app.add_handler(CommandHandler('get_leads', get_leads))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()