import telebot

bot_token = '7071388054:AAGstnlSwGQY4vPdYgeZ0EyDBpSYpqayiw8'  # Укажите здесь токен вашего бота

# Вопросы и варианты ответов
questions = [
    "Вопрос 1: Какие предметы тебе нравится изучать?",
    "Вопрос 2: Какие навыки тебе интересно развивать?",
    "Вопрос 3: Какое ваше любимое время года?",
    "Вопрос 4: Какие виды спорта вам нравятся?",
    "Вопрос 5: Какое ваше любимое блюдо?",
    "Вопрос 6: Какие язык программирования вы знаете?",
    "Вопрос 7: Какие книги вам нравится читать?",
    "Вопрос 8: Какие музыкальные жанры вы предпочитаете?",
    "Вопрос 9: Какое ваше любимое место для отдыха?",
    "Вопрос 10: Какие фильмы вам нравится смотреть?",
    # Добавьте остальные вопросы здесь
]

answers = [
    ["Математика", "Физика", "Литература"],
    ["Программирование", "Графический дизайн", "Музыка"],
    ["Весна", "Лето", "Зима", "Осень"],
    ["Футбол", "Хоккей", "Басткетбол"],
    ["Пицца", "Паста", "Суши"],
    ["Python", "Java", "Js"],
    ["Фантастические романы", "Детективы", "Классическая литература"],
    ["Рок", "Поп-музыка", "Джаз"],
    ["Горы", "Море", "Кемпинг"],
    ["Комедии", "Драмы", "Фантастика"]
    # Добавьте варианты ответов для остальных вопросов здесь
]

user_answers = {}  # Словарь для сохранения ответов пользователя

# Создание бота
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start_test(message):
    user_id = message.chat.id
    user_answers[user_id] = []  # Создаем пустой список для ответов пользователя
    send_question(user_id, 0)  # Отправляем первый вопрос


def send_question(user_id, question_index):
    question = questions[question_index]
    options = answers[question_index]

    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for option in options:
        markup.add(telebot.types.KeyboardButton(option))

    bot.send_message(user_id, question, reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    user_id = message.chat.id
    user_answers[user_id].append(message.text)  # Сохраняем ответ пользователя

    if len(user_answers[user_id]) < len(questions):
        send_question(user_id, len(user_answers[user_id]))  # Отправляем следующий вопрос
    else:
        show_result(user_id)  # Показываем результат


def show_result(user_id):
    # Здесь вы можете написать логику для определения результата на основе ответов пользователя
    # В данном примере просто отправляем сообщение с ответами пользователя
    result = "Результат:\n"
    for i, answer in enumerate(user_answers[user_id]):
        result += f"Вопрос {i + 1}: {answer}\n"

    bot.send_message(user_id, result)


bot.polling()