import telebot
from telebot import types


bot = telebot.TeleBot('6522202616:AAHNx-jS_LiZyWdimmWkGOFkE6QZ4xMWTIM')


@bot.message_handler(commands = ['start'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buy = types.KeyboardButton(text="💳 Купить")
    otz = types.KeyboardButton(text="📋 Отзывы")
    write_otz = types.KeyboardButton(text="📝 Написать отзыв")
    moder = types.KeyboardButton(text="📞 Тех. Поддержка")
    markup.add(buy, otz, write_otz, moder)
    bot.send_message(message.from_user.id, "Дᵒбᵖᵒ пᵒжᵃлᵒᵇᵃть! \n\nY ʜᴀᴄ бᴏльᴡᴏй ᴀᴄᴄᴏᴘтиMᴇʜт, ʜᴇᴄᴋᴏльᴋᴏ гᴏᴘᴏдᴏʙ ʙ ʜᴀличии, бᴏлᴇᴇ 1000 ʏᴄпᴇᴡʜыx ᴄдᴇлᴏᴋ \n\n𝕄ы ℍ𝕖д𝕒𝕓ℍ𝕠 ℍ𝕒 𝕡ыℍ𝕜𝕖, п𝕠эт𝕠𝕄𝕪 𝕪 ℍ𝕒𝕔 𝕠дℍи из 𝕔𝕒𝕄ы𝕩 ℍиз𝕜и𝕩 ц𝕖ℍ\n\nY ʜᴀᴄ ᴘᴀбᴏтᴀют тᴏльᴋᴏ пᴘᴏȹи ᴋᴏтᴏᴘыᴇ лᴏжᴀт ʙᴄё ʙ дᴏᴄтʏпʜыᴇ и ʙ тᴏжᴇ ʙᴘᴇMя бᴇзᴏпᴀᴄтʜыᴇ Mᴇᴄтᴀ")
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

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
     if call.message:
        if call.data == "moscow":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ди наху")
        elif call.data == "ekb":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ди наху")
        elif call.data == "piter":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ди наху")            
bot.polling(none_stop=True, interval=0)
