import telebot
from telebot import types
import os
from dotenv import load_dotenv
load_dotenv()

bot = telebot.TeleBot(os.getenv("Tocken"))

user_data = {}





@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, f"""
Hi {message.from_user.first_name}
Hop you are fine. MD Maruf Mursalin made me
for help you to play bdt game . This bot is free for a few days.
bdt game link :- https://hgzy.in/#/register?invitationCode=54282264400


""")
	markup = types.ReplyKeyboardMarkup(row_width=1)
	bdt1 = types.KeyboardButton("/bdt_game")
	markup.add(bdt1)
	bot.send_message(chat_id=message.chat.id, text="click one button ", reply_markup=markup)
	

@bot.message_handler(commands=["bdt_game"])
def bdt_game(mass):
	# markup = types.ReplyKeyboardRemove(selective=False)
	mock = types.ReplyKeyboardMarkup(row_width=1)
	bdt1 = types.KeyboardButton("/big_smell")
	bdt2 = types.KeyboardButton("/color_game")
	back = types.KeyboardButton("/start")
	mock.add(bdt1,bdt2,back)
	bot.send_message(chat_id=mass.chat.id, text="click one button ", reply_markup=mock)

@bot.message_handler(commands=['big_smell'])
def big_smell(mass):
	color_moc = types.ReplyKeyboardMarkup(row_width=1)
	red = types.InlineKeyboardButton("red")
	green = types.InlineKeyboardButton("green")
	color_moc.add(red,green)
	bot.send_message(chat_id=mass.chat.id,text="click on color",reply_markup=color_moc)
	bot.register_next_step_handler(mass,get_color)

def get_color(mass):
	user_id = mass.from_user.id
	user_data[user_id] = {"name":mass.text}
	mock = types.ReplyKeyboardMarkup(row_width=1)
	bdt1 = types.KeyboardButton('1')
	bdt2 = types.KeyboardButton('2')
	bdt3 = types.KeyboardButton('3')
	bdt4 = types.KeyboardButton('4')
	bdt5 = types.KeyboardButton('5')
	bdt6 = types.KeyboardButton('6')
	bdt7 = types.KeyboardButton('7')
	bdt8 = types.KeyboardButton('8')
	bdt9 = types.KeyboardButton('9')
	mock.add(bdt1,bdt2,bdt3,bdt4,bdt5,bdt6,bdt7,bdt8,bdt9)
	bot.send_message(chat_id=mass.chat.id,text=f"Input [1~9] number:",reply_markup=mock)
	bot.register_next_step_handler(mass,get_number)

def get_number(mass):
	user_id = mass.from_user.id
	number1 = int(mass.text)
	user_data[user_id]["number"] = number1
	mock = types.ReplyKeyboardMarkup(row_width=1)
	bdt1 = types.KeyboardButton('big')
	bdt2 = types.KeyboardButton('small')
	mock.add(bdt1,bdt2)
	bot.send_message(chat_id=mass.chat.id,text="input big or smell:",reply_markup=mock)
	bot.register_next_step_handler(mass,get_big_or_smmell)


def get_big_or_smmell(mass):
	user_id = mass.from_user.id
	slt = mass.text
	user_data[user_id]['slt'] = slt
	bot.send_message(chat_id=mass.chat.id,text=f"your color id {user_data[user_id]['name']} your number is {user_data[user_id]["number"]} your slt is {user_data[user_id]["slt"]}")
	bot.send_message(chat_id=mass.chat.id,text="coming soon")











@bot.message_handler(commands=['color_game'])
def color_game(mass):
	bot.send_message(chat_id=mass.chat.id,text="coming soon")









bot.infinity_polling()