import telebot
from telebot import types
import datetime
import re
import os

API_TOKEN = 'token'
bot = telebot.TeleBot(API_TOKEN)

user_data = {}


def add_minutes(start_time_str, minutes):
    start_time = datetime.datetime.strptime(start_time_str, "%H:%M")
    new_time = start_time + datetime.timedelta(minutes=minutes)
    return new_time.strftime("%H:%M")


# Генерация тайминга на основе выбора пользователя
def generate_timing(user_data):
    start_time = user_data['time']
    place = user_data['place']
    hall = user_data['hall']
    timing = user_data['timing']
    lead_program = user_data.get('program', '')
    show = user_data.get('show', '')
    game = user_data.get('game', '')
    food = user_data['food']

    timing_text = f"Здравствуйте! Это развлекательный центр «{place}» 😊.\n"
    timing_text += f"Приходим без опозданий минут за 10-15 до начала мероприятия. В {start_time} начнется ваше время! Кто опоздает может присоединиться в процессе ❗️❗️❗️\n\n"

    if food == "Еда в начале":
        timing_text += f"{start_time} - {add_minutes(start_time, 15)} Кушаем в банкетном зале 🍕\n"
        start_time = add_minutes(start_time, 15)

    # Логика для Большого Зала
    if hall == "Большой зал":
        if timing == "Минимальный БЗ":
            if place == "Крейзи Хаус":
                timing_text += f"{start_time} - {add_minutes(start_time, 45)} 8 квест-аттракционов 👾\n"
                start_time = add_minutes(start_time, 45)
            else:
                timing_text += f"{start_time} - {add_minutes(start_time, 45)} Игра на арене: {game} 👽\n"
                start_time = add_minutes(start_time, 45)
            if food == "Еда после игры":
                timing_text += f"{start_time} - {add_minutes(start_time, 15)} Кушаем в банкетном зале 🍕\n"
                start_time = add_minutes(start_time, 15)
            timing_text += f"{start_time} - {add_minutes(start_time, 45)} Программа с ведущим: {lead_program} 💥\n"
            start_time = add_minutes(start_time, 45)
            timing_text += f"{start_time} - {add_minutes(start_time, 20)} Кушаем тортик 🎂\n"
            start_time = add_minutes(start_time, 20)

        elif timing == "Стандарт БЗ":
            if place == "Крейзи Хаус":
                timing_text += f"{start_time} - {add_minutes(start_time, 45)} 8 квест-аттракционов 👾\n"
                start_time = add_minutes(start_time, 45)
            else:
                timing_text += f"{start_time} - {add_minutes(start_time, 45)} Игра на арене: {game} 👽\n"
                start_time = add_minutes(start_time, 45)
            if food == "Еда после игры":
                timing_text += f"{start_time} - {add_minutes(start_time, 15)} Кушаем в банкетном зале 🍕\n"
                start_time = add_minutes(start_time, 15)
            timing_text += f"{start_time} - {add_minutes(start_time, 45)} Программа с ведущим: {lead_program} 💥\n"
            start_time = add_minutes(start_time, 45)
            timing_text += f"{start_time} - {add_minutes(start_time, 20)} {show} ✨\n"
            start_time = add_minutes(start_time, 20)
            timing_text += f"{start_time} - {add_minutes(start_time, 15)} Кушаем тортик 🎂\n"
            start_time = add_minutes(start_time, 15)

        elif timing == "Максимальный БЗ":
            if place == "Крейзи Хаус":
                timing_text += f"{start_time} - {add_minutes(start_time, 45)} 8 квест-аттракционов 👾\n"
                start_time = add_minutes(start_time, 45)
            else:
                timing_text += f"{start_time} - {add_minutes(start_time, 45)} Игра на арене: {game} 👽\n"
                start_time = add_minutes(start_time, 45)
            if food == "Еда после игры":
                timing_text += f"{start_time} - {add_minutes(start_time, 15)} Кушаем в банкетном зале 🍕\n"
                start_time = add_minutes(start_time, 15)
            timing_text += f"{start_time} - {add_minutes(start_time, 45)} Программа с ведущим: {lead_program} 💥\n"
            start_time = add_minutes(start_time, 45)
            timing_text += f"{start_time} - {add_minutes(start_time, 20)} Шоу блеск-диско 🎊\n"
            start_time = add_minutes(start_time, 20)
            timing_text += f"{start_time} - {add_minutes(start_time, 20)} {show} ✨\n"
            start_time = add_minutes(start_time, 20)
            timing_text += f"{start_time} - {add_minutes(start_time, 25)} Кушаем тортик 🎂\n"
            start_time = add_minutes(start_time, 25)

        elif timing == "Мега БЗ":
            timing_text += f"{start_time} - {add_minutes(start_time, 45)} 8 квест-аттракционов 👾\n"
            start_time = add_minutes(start_time, 45)
            timing_text += f"{start_time} - {add_minutes(start_time, 45)} Игра на арене: {game} 👽\n"
            start_time = add_minutes(start_time, 45)
            if food == "Еда после игры":
                timing_text += f"{start_time} - {add_minutes(start_time, 15)} Кушаем в банкетном зале 🍕\n"
                start_time = add_minutes(start_time, 15)
            timing_text += f"{start_time} - {add_minutes(start_time, 45)} Программа с ведущим: {lead_program} 💥\n"
            start_time = add_minutes(start_time, 45)
            timing_text += f"{start_time} - {add_minutes(start_time, 20)} Шоу блеск-диско 🎊\n"
            start_time = add_minutes(start_time, 20)
            timing_text += f"{start_time} - {add_minutes(start_time, 20)} {show} ✨\n"
            start_time = add_minutes(start_time, 20)
            timing_text += f"{start_time} - {add_minutes(start_time, 25)} Кушаем тортик 🎂\n"
            start_time = add_minutes(start_time, 25)

    # Логика для Малого Зала
    elif hall == "Малый зал":
        if timing == "Минимальный МЗ":
            if place == "Крейзи Хаус":
                timing_text += f"{start_time} - {add_minutes(start_time, 45)} 8 квест-аттракционов 👾\n"
                start_time = add_minutes(start_time, 45)
            else:
                timing_text += f"{start_time} - {add_minutes(start_time, 45)} Игра на арене: {game} 👽\n"
                start_time = add_minutes(start_time, 45)
            if food == "Еда после игры":
                timing_text += f"{start_time} - {add_minutes(start_time, 15)} Кушаем в банкетном зале 🍕\n"
                start_time = add_minutes(start_time, 15)
            timing_text += f"{start_time} - {add_minutes(start_time, 30)} {show} ✨\n"
            start_time = add_minutes(start_time, 30)
            timing_text += f"{start_time} - {add_minutes(start_time, 20)} Кушаем тортик 🎂\n"
            start_time = add_minutes(start_time, 20)

        elif timing == "Стандарт МЗ":
            if place == "Крейзи Хаус":
                timing_text += f"{start_time} - {add_minutes(start_time, 45)} 8 квест-аттракционов 👾\n"
                start_time = add_minutes(start_time, 45)
            else:
                timing_text += f"{start_time} - {add_minutes(start_time, 45)} Игра на арене: {game} 👽\n"
                start_time = add_minutes(start_time, 45)
            if food == "Еда после игры":
                timing_text += f"{start_time} - {add_minutes(start_time, 15)} Кушаем в банкетном зале 🍕\n"
                start_time = add_minutes(start_time, 15)
            timing_text += f"{start_time} - {add_minutes(start_time, 45)} Программа с ведущим: {lead_program} 💥\n"
            start_time = add_minutes(start_time, 45)
            timing_text += f"{start_time} - {add_minutes(start_time, 20)} Кушаем тортик 🎂\n"
            start_time = add_minutes(start_time, 20)

        elif timing == "Максимальный МЗ":
            if place == "Крейзи Хаус":
                timing_text += f"{start_time} - {add_minutes(start_time, 45)} 8 квест-аттракционов 👾\n"
                start_time = add_minutes(start_time, 45)
            else:
                timing_text += f"{start_time} - {add_minutes(start_time, 45)} Игра на арене: {game} 👽\n"
                start_time = add_minutes(start_time, 45)
            if food == "Еда после игры":
                timing_text += f"{start_time} - {add_minutes(start_time, 15)} Кушаем в банкетном зале 🍕\n"
                start_time = add_minutes(start_time, 15)
            timing_text += f"{start_time} - {add_minutes(start_time, 45)} Программа с ведущим: {lead_program} 💥\n"
            start_time = add_minutes(start_time, 45)
            timing_text += f"{start_time} - {add_minutes(start_time, 20)} {show} ✨\n"  # Добавлен вывод мастер-класса или шоу
            start_time = add_minutes(start_time, 20)
            timing_text += f"{start_time} - {add_minutes(start_time, 15)} Кушаем тортик 🎂\n"
            start_time = add_minutes(start_time, 15)

    timing_text += f"{start_time} - {add_minutes(start_time, 10)} Время на сборы 🎒\n\n"
    end_time = add_minutes(start_time, 10)
    timing_text += f"Домой в {end_time} 🥳\n\n"
    timing_text += f"Всем с собой сменную обувь и хорошее настроение. Ждем вас по адресу Ленина 130/1 вход со стороны Ленина этаж {3 if place == 'Крейзи Хаус' else 4} 🎉🎉🎉"

    return timing_text


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Создать новый тайминг")
    markup.add(item)
    bot.send_message(message.chat.id, "Привет! Нажми 'Создать новый тайминг' чтобы начать.", reply_markup=markup)


def go_back(message):
    start(message)


@bot.message_handler(func=lambda message: message.text == "Назад")
def back_button(message):
    go_back(message)


@bot.message_handler(func=lambda message: message.text == "Создать новый тайминг")
def start_timing_creation(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Крейзи Хаус")
    item2 = types.KeyboardButton("Космобаза")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Выберите место:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["Крейзи Хаус", "Космобаза"])
def choose_hall(message):
    user_data[message.chat.id] = {"place": message.text}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Большой зал")
    item2 = types.KeyboardButton("Малый зал")
    markup.add(item1, item2)
    markup.add(types.KeyboardButton("Назад"))
    bot.send_message(message.chat.id, "Выберите зал:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["Большой зал", "Малый зал"])
def choose_timing(message):
    user_data[message.chat.id]["hall"] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == "Большой зал":
        item1 = types.KeyboardButton("Минимальный БЗ")
        item2 = types.KeyboardButton("Стандарт БЗ")
        item3 = types.KeyboardButton("Максимальный БЗ")
        item4 = types.KeyboardButton("Мега БЗ")
        markup.add(item1, item2, item3, item4)
    else:
        item1 = types.KeyboardButton("Минимальный МЗ")
        item2 = types.KeyboardButton("Стандарт МЗ")
        item3 = types.KeyboardButton("Максимальный МЗ")
        markup.add(item1, item2, item3)
    markup.add(types.KeyboardButton("Назад"))
    bot.send_message(message.chat.id, "Выберите пакет:", reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ["Минимальный БЗ", "Стандарт БЗ", "Максимальный БЗ", "Мега БЗ",
                                          "Минимальный МЗ", "Стандарт МЗ", "Максимальный МЗ"])
def choose_food_or_game(message):
    user_data[message.chat.id]["timing"] = message.text
    if user_data[message.chat.id]["place"] == "Космобаза" or user_data[message.chat.id]["timing"] == "Мега БЗ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Лазертаг")
        item2 = types.KeyboardButton("Амонг Ас")
        item3 = types.KeyboardButton("Прятки в темноте")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Выберите игру на арене:", reply_markup=markup)
        bot.register_next_step_handler(message, set_game)
    else:
        choose_food(message)


def set_game(message):
    if message.text not in ["Лазертаг", "Амонг Ас", "Прятки в темноте"]:
        bot.send_message(message.chat.id, "Пожалуйста выберите игру из меню.")
        choose_food_or_game(message)
    else:
        user_data[message.chat.id]["game"] = message.text
        bot.send_message(message.chat.id, "Вы выбрали игру: " + message.text)
        choose_food(message)


def choose_food(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Еда в начале")
    item2 = types.KeyboardButton("Еда после игры")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Выберите когда будет еда:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["Еда в начале", "Еда после игры"])
def set_food(message):
    user_data[message.chat.id]["food"] = message.text
    markup = types.ReplyKeyboardRemove()  # Убираем меню после выбора еды
    bot.send_message(message.chat.id, "Введите время начала мероприятия (в формате 00:00):", reply_markup=markup)


@bot.message_handler(func=lambda message: re.match(r'^\d{2}:\d{2}$', message.text))
def set_time(message):
    # Проверка на корректность времени (в пределах 00:00 - 23:59)
    time_str = message.text
    try:
        time_obj = datetime.datetime.strptime(time_str, "%H:%M")
        user_data[message.chat.id]["time"] = time_str
        if user_data[message.chat.id]["hall"] == "Большой зал":
            bot.send_message(message.chat.id, "Введите программу с ведущим:")
            bot.register_next_step_handler(message, set_program)
        elif user_data[message.chat.id]["hall"] == "Малый зал" and user_data[message.chat.id]["timing"] in [
            "Стандарт МЗ", "Максимальный МЗ"]:
            bot.send_message(message.chat.id, "Введите программу с ведущим:")
            bot.register_next_step_handler(message, set_program)
        else:
            bot.send_message(message.chat.id, "Введите мастер-класс или шоу:")
            bot.register_next_step_handler(message,
                                           set_show)  # Исправлено: теперь спрашивает о шоу или мастер-классе для всех залов
    except ValueError:
        bot.send_message(message.chat.id, "Неверный формат, выбери из меню или напиши корректные данные:")


@bot.message_handler(func=lambda message: not re.match(r'^\d{2}:\d{2}$', message.text))
def invalid_time(message):
    bot.send_message(message.chat.id, "Неверный формат, выбери из меню или напиши корректные данные:")


def set_program(message):
    user_data[message.chat.id]["program"] = message.text
    if user_data[message.chat.id]["hall"] == "Большой зал" and user_data[message.chat.id]["timing"] in ["Стандарт БЗ",
                                                                                                        "Максимальный БЗ",
                                                                                                        "Мега БЗ"]:
        bot.send_message(message.chat.id, "Введите мастер-класс или шоу:")
        bot.register_next_step_handler(message, set_show)
    elif user_data[message.chat.id]["hall"] == "Малый зал" and user_data[message.chat.id][
        "timing"] == "Максимальный МЗ":
        bot.send_message(message.chat.id, "Введите мастер-класс или шоу:")  # Исправлено для Максимального МЗ
        bot.register_next_step_handler(message, set_show)
    else:
        complete_timing_creation(message)


def set_show(message):
    user_data[message.chat.id]["show"] = message.text
    complete_timing_creation(message)


def complete_timing_creation(message):
    markup = types.ReplyKeyboardRemove()  # Убираем все клавиатуры
    timing_result = generate_timing(user_data[message.chat.id])
    bot.send_message(message.chat.id, timing_result, reply_markup=markup)
    show_new_timing_option(message)


def show_new_timing_option(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Создать новый тайминг")
    markup.add(item)
    bot.send_message(message.chat.id, "Нажми 'Создать новый тайминг' чтобы создать новый план.", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_any_text(message):
    bot.send_message(message.chat.id, "Ты написал что-то не то, начни заново /start")


bot.infinity_polling()
os.system('python main.py')
