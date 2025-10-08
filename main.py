import telebot
from telebot import types

TOKEN = "8190454358:AAGh4mYcZJc0kNs1EVw3qS8WDt2MgpPd8ko"
CHANNEL_ID = "-1002862443425"  # ID du canal
bot = telebot.TeleBot(TOKEN)

def check_membership(chat_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, chat_id)
        if member.status in ["member", "administrator", "creator"]:
            return True
        else:
            return False
    except:
        return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if check_membership(message.chat.id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("INFO")
        btn2 = types.KeyboardButton("STATISTIQUE")
        btn3 = types.KeyboardButton("Nos bots")
        markup.add(btn1, btn2)
        markup.add(btn3)
        bot.send_message(message.chat.id, "Bienvenue ! Vous pouvez maintenant utiliser notre bot", reply_markup=markup)
    else:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Rejoindre le canal", url="https://t.me/darkgptsup")
        btn_contact = types.InlineKeyboardButton("Contacter nous", url="https://t.me/kinganonymous224")
        markup.add(btn)
        markup.add(btn_contact)
        bot.send_message(message.chat.id, "Vous devez rejoindre notre canal pour utiliser le bot. Puis taper '/start' à nouveau", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["INFO", "STATISTIQUE", "Nos bots"])
def button(message):
    if check_membership(message.chat.id):
        if message.text == "INFO":
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("Info sur le proprio", callback_data="inline1")
            btn2 = types.InlineKeyboardButton("Info sur le bot", callback_data="inline2")
            btn_contact = types.InlineKeyboardButton("Contacter nous", url="https://t.me/kinganonymous224")
            markup.add(btn1, btn2)
            markup.add(btn_contact)
            bot.send_message(message.chat.id, "Choisissez une option :", reply_markup=markup)
        elif message.text == "STATISTIQUE":
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("Enregistrer", callback_data="enregistrer")
            btn2 = types.InlineKeyboardButton("Annuler", callback_data="annuler")
            btn_contact = types.InlineKeyboardButton("Contacter nous", url="https://t.me/kinganonymous224")
            markup.add(btn1, btn2)
            markup.add(btn_contact)
            bot.send_message(message.chat.id, "Voulez-vous enregistrer ou annuler votre interraction avec le bot ?", reply_markup=markup)
        elif message.text == "Nos bots":
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("Bot 1", url="https://t.me/autoaccepteur_bot")
            btn2 = types.InlineKeyboardButton("Bot 2", url="https://t.me/kingdarkgpt_bot")
            btn3 = types.InlineKeyboardButton("Bot 3", url="https://t.me/notest1233_bot")
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)
            bot.send_message(message.chat.id, "Nos bots :", reply_markup=markup)
    else:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Rejoindre le canal", url="https://t.me/darkgptsup")
        btn_contact = types.InlineKeyboardButton("Contacter nous", url="https://t.me/kinganonymous224")
        markup.add(btn)
        markup.add(btn_contact)
        bot.send_message(message.chat.id, "Vous devez rejoindre notre canal pour utiliser le bot. Puis taper '/start' à nouveau.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["inline1", "inline2", "enregistrer", "annuler"])
def callback_query(call):
    if check_membership(call.message.chat.id):
        bot.answer_callback_query(call.id)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        if call.data == "inline1":
            bot.send_message(call.message.chat.id, "Ce bot à été par 亗K͜͡ɪɴɢウ 🅰🅽🅾🅽🆈🅼🅾🆄🆂︎")
        elif call.data == "inline2":
            bot.send_message(call.message.chat.id, "Ce ci est notre bot d'accueil.")
        elif call.data == "enregistrer":
            bot.send_message(call.message.chat.id, "Enregistré avec succès !")
        elif call.data == "annuler":
            bot.send_message(call.message.chat.id, "Action annulée.")
    else:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Rejoindre le canal", url="https://t.me/darkgptsup")
        btn_contact = types.InlineKeyboardButton("Contacter nous", url="https://t.me/kinganonymous224")
        markup.add(btn)
        markup.add(btn_contact)
        bot.send_message(call.message.chat.id, "Vous devez rejoindre notre canal pour utiliser le bot. Puis taper '/start' à nouveau", reply_markup=markup)

bot.polling()
