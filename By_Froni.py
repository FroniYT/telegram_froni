
#добовления телеграм api
import telebot, random,time


#Цифры и буквы для автризиции
symbols = 'qwrtyuiopasdfghjklzxcvbnm123456789'

#токен бота в telegrame
bot = telebot.TeleBot('1647547683:AAFlv55U1oL96lkrKiipCDFCinKr3zOjveE')


#системма авторизаци

login = input('Ваш логин >>> ')
passworld = input('Ваш пароль >>> ')

#система проверки логина и пороля
if login == 'Froni' and passworld == 'Froni':
    for q in range(1):
        bot_say = ''

        for i in range(5):
            bot_say += random.choice(symbols)
    #Сам бот
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text == '!авторизация':
            bot.send_message(message.chat.id, bot_say)

            #Продолжения аунтификации
            lde = input('двояная автоизации >>> ')

            if lde == bot_say:
                print('Вы авторизированны')

            elif lde != bot_say:
                print('Вы не авторизованны')
        

    
    #Run
    bot.polling()
