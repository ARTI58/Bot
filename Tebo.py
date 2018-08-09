import telebot
import time
token='524342890:AAEXOAf9-HT4UINPNLTX-77XYDYYpP0IOp8'
bot = telebot.TeleBot(token)
 
@bot.message_handler(content_types=["text"])
def handler_text(message):
	if message.text == "Ты знаешь Муратбекова Нурислама":
		bot.send_message(message.chat.id, "Да, Он крыса в варфейсе")
		log(message, answer)
#--------------ТЕКСТ-----------------------------------------------------------------------------------------------------
	elif message.text == "Всем привет" or message.text == 'всем привет':
		bot.send_message(message.chat.id, "Пошел на хуй")

	elif message.text == "Ахаха"or message.text == 'Ахахах' or message.text == 'Ахахаха':
		bot.send_message(message.chat.id, "Закрой рот я буду смеяться")	

	elif message.text == "Ахах" or message.text == 'А' or message.text == 'Ах' or message.text == 'Аха':
		bot.send_message(message.chat.id, "Щас Джамалу расскажу")		

	elif message.text == "Джамал":
		bot.send_message(message.chat.id, "Фууу гей")
	
	
	elif message.text == "Порно":
		bot.send_message(message.chat.id, "Фууу извращенец")

	elif message.text == "Ты можешь навредить человеку?":
		bot.send_message(message.chat.id, "Нет я не запраграммирована причинять боль")		
	
	elif message.text == "иди домой" or message.text == 'Иди домой':
		bot.send_message(message.chat.id, "Иди домой")

	elif message.text == "Жду" or message.text == 'жду':
		bot.send_message(message.chat.id, "Жди Жди тряпка")	

	elif message.text == "Блэд" or message.text == 'блэд' or message.text == 'Блять' or message.text == 'Сука' or message.text == 'бля' or message.text == 'Бля' or message.text == 'сука':
		bot.send_message(message.chat.id, "Ты не ахуел матюкатся?")

	elif message.text == "Питон" or message.text == 'питон':
		bot.send_message(message.chat.id, "https://t.me/peripython1500")

	elif message.text == "Суслик" or message.text == ' Суслек' or message.text == 'суслек' or message.text == 'суслик':
		bot.send_message(message.chat.id, "Гей")
		
	elif message.text == "а я" or message.text == 'А я':
		bot.send_message(message.chat.id, "А ты")

	elif message.text == "Хмм" or message.text == 'хмм':
		bot.send_message(message.chat.id, "Нахмыкался?")

	elif message.text == "Да" or message.text == 'да':
		bot.send_message(message.chat.id, "Я согласен")


	elif message.text == "Эм" or message.text == 'эм':
		bot.send_message(message.chat.id, "Да закрой рот наконец")

	elif message.text == "Спам" or message.text == 'спам':
		while True:
			bot.send_message(message.chat.id, "Ура спам")
		
	elif message.text == "0" or message.text == '0':
			exit()				
#----------------------- ФОТО -------------------------------------------------------------------------------------------
	elif message.text == "Отправь мне фото природы":
		url = 'https://img.fonwall.ru/o/95/most_doma_ulitsyi_kamni_okean.jpg'
		urllib2.urlretrieve(url, 'url_image.jpg')
		img = open('url_image.jpg', 'rb')
		bot.send_chat_action(message.chat.id, "upload_photo")
		bot.send_photo(message.from_user.id, img)
		

	elif message.text == "Отправь мне фото новой школы" or message.text == 'Фото 57 школы' or message.text == '57 школа' or message.text == 'фото 57 школы':
		url = 'http://info-kizlyar.ru/media/cache/26/ff/61/ed/2f/31/26ff61ed2f3165ce5bf2db0cfaaeb7ce.jpg'
		urllib2.urlretrieve(url, 'url_image.jpg')
		img = open('url_image.jpg', 'rb')
		bot.send_chat_action(message.chat.id, "upload_photo")
		bot.send_photo(message.from_user.id, img)
		
	elif message.text == "Днд"  or message.text == 'днд':
		url = 'http://www.dgstaphouse.com/wp-content/uploads/2017/06/dnd-promo-3-1024x512.png'
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