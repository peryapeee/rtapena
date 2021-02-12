import telebot 
import configure
import sqlite3
from sqlite3 import Error
from telebot import types

bot = telebot.TeleBot(configure.config['token'])

	
	#работа со стартом  
	
@bot.message_handler(commands=['start'])
def start(message):


	send_mess = f"<b>Привет {message.from_user.first_name}, классный ник!\nА теперь давай найдем тебе классную одежду</b>"
		
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item_catalog = types.KeyboardButton('📂 Каталог')
	item_basket = types.KeyboardButton('🛒 Корзина')
	item_orders = types.KeyboardButton('📦 Заказы')
	item_news = types.KeyboardButton('📡 Новости')
	item_settings = types.KeyboardButton('⚙️ Настройки')
	item_help = types.KeyboardButton('❓ Помощь')
	
	markup.row(item_catalog, item_basket)
	markup.row(item_orders, item_news)
	markup.row(item_settings, item_help)
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
	
	#работа с текстом (этаж 1)
	
@bot.message_handler(content_types = ['text'])
def get_button(message):


	if message.text == '📂 Каталог':
		markup_reply1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item_catalog1 = types.KeyboardButton('👕 Верхняя одежда 👚')
		item_catalog2 = types.KeyboardButton('👖 Штаны/Юбки/Шорты 🩳')
    
		markup_reply1.row(item_catalog1)
		markup_reply1.row(item_catalog2)
		bot.send_message(message.chat.id, 'Выберите раздел:', reply_markup = markup_reply1)

	elif message.text == '🛒 Корзина':
		bot.send_message(message.chat.id, 'Выберите раздел:')

	elif message.text == '📦 Заказы':
		bot.send_message(message.chat.id, 'Выберите раздел:')

	elif message.text == '📡 Новости':
		bot.send_message(message.chat.id, 'К сожалению, пока что новостей нет 😢')

	elif message.text == '⚙️ Настройки':
		bot.send_message(message.chat.id, 'Выберите раздел:')

	elif message.text == '❓ Помощь':
		bot.send_message(message.chat.id, 'Выберите раздел:')

	elif message.text == 'Купить':
		bot.send_message(message.chat.id, 'Ваш заказ принят\nМожете забрать когда будет удобно 😌')

	#этаж 2 

	elif message.text == '👕 Верхняя одежда 👚':	
		markup_inline = types.InlineKeyboardMarkup()
		markup_inline.add(*[types.InlineKeyboardButton(text=name, callback_data=name)
				for name in ['Куртки', 'Кофты', 'Свитера']])
		bot.send_message(message.chat.id, 'Выберите товар:', reply_markup = markup_inline)

	elif message.text == "👖 Штаны/Юбки/Шорты 🩳":
		markup_inline1 = types.InlineKeyboardMarkup()
		markup_inline1.add(*[types.InlineKeyboardButton(text=name, callback_data=name)
				for name in ['Штаны', 'Юбки', 'Шорты']])
		bot.send_message(message.chat.id, 'Выберите товар:', reply_markup = markup_inline1)

	else:  
		bot.send_message(message.chat.id, 'Сейчас не понял 😒')

	#работа с инлайновой клавиатурой (этаж 3) 
		 
@bot.callback_query_handler(func = lambda call: True)	
def back_menu(call):
	
	cid = call.message.chat.id

	sqlite_connection = sqlite3.connect('database.db')
	cursor = sqlite_connection.cursor()

				
	if call.data == 'Куртки':
		markup_reply3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item_menu = types.KeyboardButton('🤷‍♀️ Главное меню')
		item_buy = types.KeyboardButton('Купить')

		markup_reply3.add(item_menu, item_buy)
		sqlite_insert_blob_query = "SELECT photo, description, price from bd where id = 1"
		cursor.execute(sqlite_insert_blob_query)
		bot.send_photo(cid, photo=open("product/jacket_kappa.jpg", 'rb'))
		bot.send_message(cid, str(cursor.fetchone()[1]) + '\nЦена: 1750 грн.', reply_markup = markup_reply3)

	elif call.data == 'Кофты':
		markup_reply4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item_menu = types.KeyboardButton('🤷‍♀️ Главное меню')
		item_buy = types.KeyboardButton('Купить')

		markup_reply4.add(item_menu, item_buy)
		sqlite_insert_blob_query2 = "SELECT photo, description, price from bd where id = 2"
		cursor.execute(sqlite_insert_blob_query2)
		bot.send_photo(cid, photo=open("product/blose_tnf.jpg", 'rb'))
		bot.send_message(cid, str(cursor.fetchone()[1]) + '\nЦена: 1175 грн.', reply_markup = markup_reply4)

	elif call.data == 'Свитера':
		markup_reply5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item_menu = types.KeyboardButton('🤷‍♀️ Главное меню')
		item_buy = types.KeyboardButton('Купить')

		markup_reply5.add(item_menu, item_buy)
		sqlite_insert_blob_query3 = "SELECT photo, description, price from bd where id = 3"
		cursor.execute(sqlite_insert_blob_query3)
		bot.send_photo(cid, photo=open("product/sweater_ripndip.jpg", 'rb'))
		bot.send_message(cid, str(cursor.fetchone()[1]) + '\nЦена: 1050 грн.', reply_markup = markup_reply5)
		

	elif call.data == 'Штаны':
		markup_reply6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item_menu = types.KeyboardButton('🤷‍♀️ Главное меню')
		item_buy = types.KeyboardButton('Купить')

		markup_reply6.add(item_menu, item_buy)
		sqlite_insert_blob_query4 = "SELECT photo, description, price from bd where id = 4"
		cursor.execute(sqlite_insert_blob_query4)
		bot.send_photo(cid, photo=open("product/trousers_nasa.jpg", 'rb'))
		bot.send_message(cid, str(cursor.fetchone()[1]) + '\nЦена: 1200 грн.', reply_markup = markup_reply6)
	

	elif call.data == 'Юбки':
		markup_reply7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item_menu = types.KeyboardButton('🤷‍♀️ Главное меню')
		item_buy = types.KeyboardButton('Купить')

		markup_reply7.add(item_menu, item_buy)
		sqlite_insert_blob_query5 = "SELECT photo, description, price from bd where id = 5"
		cursor.execute(sqlite_insert_blob_query5)
		bot.send_photo(cid, photo=open("product/skirt_nike.jpg", 'rb'))
		bot.send_message(cid, str(cursor.fetchone()[1]) + '\nЦена: 850 грн.', reply_markup = markup_reply7)
		

	elif call.data == 'Шорты':
		markup_reply8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item_menu = types.KeyboardButton('🤷‍♀️ Главное меню')
		item_buy = types.KeyboardButton('Купить')

		markup_reply8.add(item_menu, item_buy)
		sqlite_insert_blob_query6 = "SELECT photo, description, price from bd where id = 6"
		cursor.execute(sqlite_insert_blob_query6)
		bot.send_photo(cid, photo=open("product/shorts_ripndip.jpg", 'rb'))
		bot.send_message(cid, str(cursor.fetchone()[1]) + '\nЦена: 1000 грн.', reply_markup = markup_reply8)
		
	

bot.polling(none_stop=True)