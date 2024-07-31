import telebot
from telebot import types
import time

menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
buy = types.KeyboardButton(text="💳 Купить")
otz = types.KeyboardButton(text="📋 Отзывы")
write_otz = types.KeyboardButton(text="📝 Написать отзыв")
moder = types.KeyboardButton(text="📞 Оператор")
menu_markup.add(buy, otz, write_otz, moder)

#with open("wallet.txt", "r") as file1:
#    for line in file1:
#        bitcoin = line.strip()

bitcoin = 'bc1qsgu0nsquze6zq6flxw76xhmq8j3h4lvch883av'

quantity = 0
price = 0

product = False
offer = ''

chanel_id = -1002151212470

delete = ''

def pattern(quantity, price):
    global offer
    offer = f"Кол-во {quantity} грамм. Цена: {price} RUB"
    return types.KeyboardButton(text = offer)

alpha = 1880 # 0.5 грамм
amfe = 2050 # 1 грамм
gash = 1800 # 1 грамм
xtc = 1900 # 0.5 грамм
mef = 2700 # 0.5 таблетка
kok94 = 5000 # 0.5 грамм
kok98 = 7200 # 0.5 грамм 
metadon = 3000 # 0,25 грамм 


bot = telebot.TeleBot('6522202616:AAHNx-jS_LiZyWdimmWkGOFkE6QZ4xMWTIM')

@bot.message_handler(commands = ['start'])
def menu(message):

    bot.send_message(message.from_user.id, "Дᵒбᵖᵒ пᵒжᵃлᵒᵇᵃть! \n\nY ʜᴀᴄ бᴏльᴡᴏй ᴀᴄᴄᴏᴘтиMᴇʜт, 3 гᴏᴘᴏда ʙ ʜᴀличии, десятки довольных клиентов \n\n𝕄ы ℍ𝕖д𝕒𝕓ℍ𝕠 ℍ𝕒 𝕡ыℍ𝕜𝕖, п𝕠эт𝕠𝕄𝕪 𝕪 ℍ𝕒𝕔 𝕠дℍи из 𝕔𝕒𝕄ы𝕩 ℍиз𝕜и𝕩 ц𝕖ℍ\n\nY ʜᴀᴄ ᴘᴀбᴏтᴀют тᴏльᴋᴏ пᴘᴏȹи ᴋᴏтᴏᴘыᴇ лᴏжᴀт ʙᴄё ʙ дᴏᴄтʏпʜыᴇ и ʙ тᴏжᴇ ʙᴘᴇMя бᴇзᴏпᴀᴄтʜыᴇ Mᴇᴄтᴀ")
    bot.send_message(message.from_user.id, "Выберите пункт меню", reply_markup = menu_markup)
@bot.message_handler(content_types=["text"])
def text(message):
    global tovar
    global product
    global quantity
    global offer
    global delete
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
    elif message.text == "📞 Оператор":
        bot.send_message(message.from_user.id, "По всем вопросом обращаться к оператору @timuroperator228")
    elif message.text == "Отменить заказ":
        bot.send_message(message.from_user.id, "Заказ отменен", reply_markup = menu_markup)
        product = False
    if product == True:
        markup_buy = types.ReplyKeyboardMarkup()
        quantity = 0.5
        if message.text == '⚪️A-PVP Белая':
            tovar = "⚪️A-PVP Белая"
            gramm = [pattern(quantity, alpha),pattern((int(quantity*2)), (alpha*1.6)),pattern(int(quantity * 4), (alpha*1.6*1.6)), pattern(int(quantity * 10), (alpha*7.71))]
            markup_buy.add(gramm[0], gramm[1], gramm[2], gramm[3], delete)
        elif message.text == '💭Аmфетамин сульфат':
            tovar = '💭Аmфетамин сульфат'
            gramm = [pattern(int(quantity*2), (amfe*1.6)),pattern(int(quantity * 4), (amfe*1.6*1.6)),pattern(int(quantity * 10), (amfe*4.7))]
            markup_buy.add(gramm[0], gramm[1], gramm[2], delete)
        elif message.text == '🌿Гaшиш':
            tovar = '🌿Гaшиш'
            gramm = [pattern(int(quantity*2), (gash*1.6)),pattern(int(quantity * 4), (gash*1.6*1.6)),pattern(int(quantity * 10), (gash*4.71)), pattern(int(quantity * 20), (gash*9.6))]
            markup_buy.add(gramm[0], gramm[1], gramm[2], gramm[3], delete)
        elif message.text == '⚪️Mефeдрон [HQ Мука]':
            tovar = '⚪️Mефeдрон [HQ Мука]'
            gramm = [pattern(quantity, mef),pattern(int(quantity*2), (mef*1.6)),pattern(int(quantity * 4), (mef*1.6*1.6)),pattern(int(quantity) * 10, (mef*7.71))]
            markup_buy.add(gramm[0], gramm[1], gramm[2], gramm[3], delete)  
        elif message.text == '💊XTC':
            tovar = '💊XTC'
            gramm = [pattern(int(quantity*2), xtc),pattern(int(quantity*4), (xtc*1.6)),pattern(int(quantity*10), (xtc*4.7))]
            markup_buy.add(gramm[0], gramm[1], gramm[2], delete)
        elif message.text == '🥥Kокс [HQ 94,5 %]':
            tovar = '🥥Kокс [HQ 94,5 %]'
            gramm = [pattern(quantity, kok94),pattern(int(quantity*2), (kok94*1.6)),pattern(int(quantity * 4), (kok94*1.6*1.6)),pattern(int(quantity * 10), (kok94*7.71))]
            markup_buy.add(gramm[0], gramm[1], gramm[2], gramm[3], delete)
        elif message.text == '🥥Кокс [VHQ 98 %]':
            tovar = '🥥Кокс [VHQ 98 %]'
            gramm = [pattern(quantity, kok98),pattern(int(quantity*2), (kok98*1.6)),pattern(int(quantity * 4), (kok98*1.6*1.6)),pattern(int(quantity * 10), (kok98*7.71))]
            markup_buy.add(gramm[0], gramm[1], gramm[2], gramm[3], delete)
        elif message.text == '🍯Mеtадон [VHQ]':
            tovar = '🍯Mеtадон [VHQ]'
            gramm = [pattern(quantity, metadon),pattern(int(quantity*2), (metadon*1.6)),pattern(int(quantity * 4), (metadon*1.6*1.6)),pattern(int(quantity * 10), (metadon*7.71))]
            markup_buy.add(gramm[0], gramm[1], gramm[2], gramm[3], delete)
        global city
        global region
        global quanity
        global price
        
        msg = bot.send_message(message.from_user.id, f"📍Город: {city}\n📬Примерный адрес: {region}\nВыбраный товар: {tovar}\nВыберите количество. Далее идёт оформление заказа", reply_markup = markup_buy)
        bot.register_next_step_handler(msg, order)
        product = False
        
def order(message):
    x = message.text
    lst = x.split()
    quantity = float(lst[1])
    price = float(lst[4])
    markup_inline = types.InlineKeyboardMarkup()
    operator = types.InlineKeyboardButton(text='Я ОПЛАТИЛ', url='https://t.me/timuroperator228')
    markup_inline.add(operator)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(delete)
    bot.send_message(message.from_user.id, f"✔ОФОРМЛЕНИЕ ЗАКАЗА✔\n\n📍Город: {city}\n📬Примерный адрес: {region}\n🛒Выбраный товар: {tovar}\n📌Выбранное количество: {quantity} \n💳Цена: {price}\n⚠ПЕРЕД ОПЛАТОЙ УДОСТОВЕРЬТЕСЬ ЧТО ВСЕ ДАННЫЕ УКАЗАНЫ ВЕРНО⚠\nПлатежный метод - 🉑Bitcoin(BTC) \n\nПереведите {price} all на реквизиты:\n\n{bitcoin}\n\n", reply_markup=markup)
    time.sleep(1)
    bot.send_message(message.from_user.id, 'ПОСЛЕ ОПЛАТЫ СВЯЖИТЕСЬ С ОПЕРАТОРОМ И ОТПРАВЬТЕ ЕМУ ЧЕК', reply_markup = markup_inline)
    time.sleep(1)
    mamont = message.from_user.username
    bot.send_message(chat_id = chanel_id, text = f"Мамонт: @{mamont}\n\n✔ОФОРМЛЕНИЕ ЗАКАЗА✔\n\n📍Город: {city}\n📬Примерный адрес: {region}\n🛒Выбраный товар: {tovar}\n📌Выбранное количество: {quantity} \n💳Цена: {price}\n⚠ПЕРЕД ОПЛАТОЙ УДОСТОВЕРЬТЕСЬ ЧТО ВСЕ ДАННЫЕ УКАЗАНЫ ВЕРНО⚠\nПлатежный метод - 🉑Bitcoin(BTC) \n\nПереведите {price} all на реквизиты:\n\n{bitcoin}")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global city
    if call.message:
        if call.data == "moscow":
            city = "Москва"
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Город: {city}\n\n📍 1.Укажите свой примерный адрес. Например район, улица или станция метро\n\n📬2.Адрес пишется в свободной форме (БЕЗ ОШИБОК!).")
            bot.register_next_step_handler(msg, input_message)
        elif call.data == "ekb":
            city = "Екатеринбург"
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Город: {city}\n\n📍 1.Укажите свой примерный адрес. Например район, улица или станция метро\n\n📬2.Адрес пишется в свободной форме (БЕЗ ОШИБОК!).")
            bot.register_next_step_handler(msg, input_message)
        elif call.data == "piter":
            city = 'Санкт-Петербург'
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Город: {city}\n\n📍 1.Укажите свой примерный адрес. Например район, улица или станция метро\n\n📬2.Адрес пишется в свободной форме (БЕЗ ОШИБОК!).")
            bot.register_next_step_handler(msg, input_message)
 
def input_message(message):
    global product
    global delete
    global region
    product = True
    region = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    delete = types.KeyboardButton(text="Отменить заказ")
    bot.send_message(message.chat.id, f"📍Город: {city}\n📬Примерный адрес: {region}\n", reply_markup = markup)
    alpha = types.KeyboardButton(text='⚪️A-PVP Белая')
    amfe = types.InlineKeyboardButton(text='💭Аmфетамин сульфат')
    gash = types.InlineKeyboardButton(text='🌿Гaшиш')
    mef = types.InlineKeyboardButton(text='⚪️Mефeдрон [HQ Мука]')
    xtc = types.InlineKeyboardButton(text='💊XTC')
    kok94 = types.InlineKeyboardButton(text='🥥Kокс [HQ 94,5 %]')
    kok98 = types.InlineKeyboardButton(text='🥥Кокс [VHQ 98 %]')
    metadon = types.InlineKeyboardButton(text='🍯Mеtадон [VHQ]')
    markup.add(alpha, amfe,gash,mef,xtc,kok94,kok98,metadon, delete)
    bot.send_message(message.chat.id, "Выберите интересующий вас товар", reply_markup = markup) 
bot.polling(none_stop=True, interval=0)

