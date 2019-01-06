import telebot
import time
token='524342890:AAEXOAf9-HT4UINPNLTX-77XYDYYpP0IOp8'
bot = telebot.TeleBot(token)
 
@bot.message_handler(content_types=["text"])
def handler_text(message):
	if message.text == "Привет":
		bot.send_message(message.chat.id, "Хай")
		log(message, answer)
#--------------ТЕКСТ-----------------------------------------------------------------------------------------------------
	elif message.text == "Как дела?"
		bot.send_message(message.chat.id, "Хорошо, у тебя?")
	
	elif message.text == "Что делаешь?"
		bot.send_message(message.chat.id, "С тобой общаясь")
		
	elif message.text == "Кто ты?"
		bot.send_message(message.chat.id, "Я простая программа написанная одним мальчиком")
	
	elif message.text == "Пока"
		bot.send_message(message.chat.id, "Досвидание")

#----------------------- ФОТО -------------------------------------------------------------------------------------------
	elif message.text == "Фото природы":
		url = 'https://img.fonwall.ru/o/95/most_doma_ulitsyi_kamni_okean.jpg'
		urllib2.urlretrieve(url, 'url_image.jpg')
		img = open('url_image.jpg', 'rb')
		bot.send_chat_action(message.chat.id, "upload_photo")
		bot.send_photo(message.from_user.id, img)
#------------------------------------------------------------------------------------------------------------------
while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)

#в боте было намного больше всего, но я решил удалить многое по той причине того что там было много лишнего, ненужного и личного
#Это мой превый бот который я когда либо делал, поэтому тут нету нечего сверхъестественного, обычный простой бот который был сделан больше для теста
#Дальше будет только лучше)
