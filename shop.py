import telebot
from telebot import types

user_input = ""

bot = telebot.TeleBot('6522202616:AAHNx-jS_LiZyWdimmWkGOFkE6QZ4xMWTIM')

@bot.message_handler(commands = ['start'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buy = types.KeyboardButton(text="💳 Купить")
    otz = types.KeyboardButton(text="📋 Отзывы")
    write_otz = types.KeyboardButton(text="📝 Написать отзыв")
    moder = types.KeyboardButton(text="📞 Тех. Поддержка")
    markup.add(buy, otz, write_otz, moder)
    bot.send_message(message.from_user.id, "Дᵒбᵖᵒ пᵒжᵃлᵒᵇᵃть! \n\nY ʜᴀᴄ бᴏльᴡᴏй ᴀᴄᴄᴏᴘтиMᴇʜт, 2 гᴏᴘᴏда ʙ ʜᴀличии, бᴏлᴇᴇ 1000 ʏᴄпᴇᴡʜыx ᴄдᴇлᴏᴋ \n\n𝕄ы ℍ𝕖д𝕒𝕓ℍ𝕠 ℍ𝕒 𝕡ыℍ𝕜𝕖, п𝕠эт𝕠𝕄𝕪 𝕪 ℍ𝕒𝕔 𝕠дℍи из 𝕔𝕒𝕄ы𝕩 ℍиз𝕜и𝕩 ц𝕖ℍ\n\nY ʜᴀᴄ ᴘᴀбᴏтᴀют тᴏльᴋᴏ пᴘᴏȹи ᴋᴏтᴏᴘыᴇ лᴏжᴀт ʙᴄё ʙ дᴏᴄтʏпʜыᴇ и ʙ тᴏжᴇ ʙᴘᴇMя бᴇзᴏпᴀᴄтʜыᴇ Mᴇᴄтᴀ")
    bot.send_message(message.from_user.id, "Выберите пункт меню", reply_markup = markup)
@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == "💳 Купить":
        types.ReplyKeyboardRemove()
        markup_inline = types.InlineKeyboardMarkup()
        moscow = types.InlineKeyboardButton(text='Москва', callback_data='moscow')
        ekb = types.InlineKeyboardButton(text='Екатеринбург', callback_data='ekb')
        piter = types.InlineKeyboardButton(text='Санкт-Петербург', callback_data='piter')
        markup_inline.add(moscow, ekb, piter)
        bot.send_message(message.chat.id, 'Выберите город', reply_markup=markup_inline)
    elif message.text == "📋 Отзывы":
        bot.send_message(message.from_user.id, "Канал с отзывами\nhttps://t.me/+t3LTVJXoqXlmNGJl")
    elif message.text == "📝 Написать отзыв":
        bot.send_message(message.from_user.id, "Написать отзыв\nhttps://t.me/heisenbergshopreviewsbot")
    elif message.text == "📞 Тех. Поддержка":
        bot.send_message(message.from_user.id, "По всем вопросом обращаться к оператору @timuroperator228")     

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
     if call.message:
        if call.data == "moscow":
            city = "Москва"
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Город: {city}\n\n📍 1.Укажите свой примерный адрес. Например район, улица или станция метро\n\n📬2.Адрес пишется в свободной форме (БЕЗ ОШИБОК!).")
            bot.register_next_step_handler(msg, input_message)
        elif call.data == "ekb":
            city = "Екатеринбург"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Город: {city}\n\n📍 1.Укажите свой примерный адрес. Например район, улица или станция метро\n\n📬2.Адрес пишется в свободной форме (БЕЗ ОШИБОК!).")
            bot.register_next_step_handler(msg, input_message)
        elif call.data == "piter":
            city = 'Санкт-Петербург'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Город: {city}\n\n📍 1.Укажите свой примерный адрес. Например район, улица или станция метро\n\n📬2.Адрес пишется в свободной форме (БЕЗ ОШИБОК!).")
            bot.register_next_step_handler(msg, input_message)
def input_message(message):
    region = message.text
    bot.send_message(message.chat.id, )
bot.polling(none_stop=True, interval=0)
