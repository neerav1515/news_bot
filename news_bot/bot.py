import logging
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,Dispatcher
from telegram import Bot,Update,ReplyKeyboardMarkup
from utils import get_reply,fetch_news,topics_keyboard,intro,helpo

logging.basicConfig(format='%(asctime)s - :%(name)s - %(levelname)s - %(messages)s-',level=logging.INFO)
logger=logging.getLogger(__name__)

TOKEN="ENTER YOUR BOT API HERE"

 
def start(bot,update):
	print(update)
	author=update.message.from_user.first_name
	reply="this is a news bot created by neerav(NIT hamirpur)"
	bot.send_message(chat_id=update.message.chat_id,text=intro)

def helpp(bot,update):
	print(update)
	author=update.message.from_user.first_name
	reply="some tabs might not work in that case enter 'news_category,countryname'"
	bot.send_message(chat_id=update.message.chat_id,text=helpo)

def news(bot,update):
    bot.send_message(chat_id=update.message.chat_id,text="choose a category",
    	 reply_markup=ReplyKeyboardMarkup(keyboard=topics_keyboard,one_time_keyboard=True))	

def echo_text(bot,update):
	intent,reply=get_reply(update.message.text,update.message.chat_id)
	if intent== "get_news":
	   articles=fetch_news(reply)
	   for article in articles:
	      bot.send_message(chat_id=update.message.chat_id,text=article['link'])
	else:	
	   bot.send_message(chat_id=update.message.chat_id,text=reply)

def echo_sticker(bot,update):
	bot.send_sticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)

def error(bot,update):
	logger.error("update '%s' lead to '%s'",update,update.error)
   
def main():

   updater=Updater(TOKEN)
   dp=updater.dispatcher	

   dp.add_handler(CommandHandler("start",start))
   dp.add_handler(CommandHandler("help",helpp))
   dp.add_handler(CommandHandler("news",news))
   dp.add_handler(MessageHandler(Filters.text,echo_text))
   dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
   dp.add_error_handler(error)

   updater.start_polling()
   updater.idle()
  

if __name__=="__main__":
	main()
 
  
  
