from webbrowser import get
import telebot
import get_data as gd
import tester as ts


bot = telebot.TeleBot('5965716543:AAHfWBc1H3ZlwtHh24FbrZcafozzHrd1b0M')
cur_cat = test_num = mark = desc = 0
cur_theme = ''

categories = gd.load_data()
test_data = ts.load_data()



@bot.message_handler(commands=['start'], content_types=['text'])
def drive_message(message):
    bot.send_message(message.from_user.id, "Для информации введите /help.")


@bot.message_handler(commands=['help'], content_types=['text'])
def help_message(message):
    help_message = "Pro Avto бот позволит вам узнать новое об легендарных автомобилях. Чтобы выбрать раздел нажмите на слово или впишите цифру. Для повторного запуска напишите /help" \
                   " \n Для того, чтобы узнать новое об автомобилях /drive." \
                   " \n Для того, чтобы пройти небольшой тестик и проверить свои знания введите слово /test."
    bot.send_message(
        message.from_user.id, help_message)

@bot.message_handler(commands=['test'], content_types=['text'])
def message_test(message):
    global cur_theme, test_num
    cur_theme = 'test'
    str1 = ts.get_question(test_data, test_num)
    bot.send_message(
        message.from_user.id, str1)
    test_num += 1

@bot.message_handler(commands=['drive'], content_types=['text'])
def drive_message(message):
    global cur_cat, cur_theme, desc
    cur_cat = desc = 0
    cur_theme = 'drive'
    str1 = gd.get_categories(categories)
    bot.send_message(
        message.from_user.id, str1)


def wrong_cat(message):
    bot.send_message(
        message.from_user.id, "не верно введен номер раздела")


@bot.message_handler(content_types=['text'])
def message_get(message):
    global categories, test_data, test_num, mark, cur_cat, cur_theme, desc

    if cur_theme == 'test':
        if str(message.text).isdigit():
            mark += ts.check_answer(test_data, test_num - 1, int(message.text))
            if test_num < len(test_data):
                str1 = ts.get_question(test_data, test_num)
                bot.send_message(
                    message.from_user.id, str1)
                test_num += 1
            else:
                cur_theme = ''
                test_num = 0
                str1 = f"Вы ответили на {mark} вопросов из {len(test_data)} \n"
                bot.send_message(
                    message.from_user.id, str1)
        else:
            bot.send_message(
                message.from_user.id, "не верно введен ответ на вопрос (должна быть цифра)")

    elif cur_theme == 'drive' and desc == 0:
        if str(message.text).isdigit():
            cur_cat = int(message.text)
            str1 = gd.get_sub_categories(categories, cur_cat)
            if str1 != "Выберите интересующую тему: \n":
                desc = 1
                bot.send_message(
                    message.from_user.id, str1)
            else:
                wrong_cat(message)
        else:
            wrong_cat(message)

    elif cur_theme == 'drive' and desc == 1:
        if str(message.text).isdigit():
            cur_theme = int(message.text)
            data, img = gd.get_desc(categories, cur_cat, cur_theme)
            if data is not None:
                cur_cat = 0
                cur_theme = ''
                str1 = f"{data} \n"
                bot.send_photo(chat_id=message.from_user.id, photo=open(img, 'rb'))
                bot.send_message(
                    message.from_user.id, str1)

            else:
                wrong_cat(message)
                cur_theme = 'drive'
        else:
            wrong_cat(message)

    elif str(message.text).lower() == 'привет':
        bot.send_message(
            message.from_user.id, "Привет, чем я могу тебе помочь? Для информации введите /help.")

    else:
        bot.send_message(message.from_user.id, "Для информации введите /help.")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)