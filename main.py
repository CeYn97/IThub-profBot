import telebot
from telebot import types

# Создаем экземпляр бота
bot = telebot.TeleBot("7071388054:AAGstnlSwGQY4vPdYgeZ0EyDBpSYpqayiw8")

# Список вопросов и вариантов ответов
questions = [
   {
        "question": "Вопрос 1: Какие предметы тебе нравится изучать?",
        "options": ["Математика", "Физика", "Литература"]
    },
    {
        "question": "Вопрос 2: Какие навыки тебе интересно развивать?",
        "options": ["Программирование", "Графический дизайн", "Музыка"]
    }, 
    {
        "question": "Вопрос 3: Какое ваше любимое время года?",
        "options": ["Весна", "Лето", "Зима", "Осень"]
    },
    {
        "question": "Вопрос 4: Какие виды спорта вам нравятся?",
        "options": ["Футбол", "Хоккей", "Басткетбол"]
    },
    {
        "question": "Вопрос 5: Какое ваше любимое блюдо?",
        "options": ["Пицца", "Паста", "Суши"]
    },
    {
        "question": "Вопрос 6: Какие язык программирования вы знаете?",
        "options": ["Python", "Java", "Js"]
    },
    {
        "question": "Вопрос 7: Какие книги вам нравится читать?",
        "options": ["Фантастические романы", "Детективы", "Классическая литература"]
    },
    {
        "question": "Вопрос 8: Какие музыкальные жанры вы предпочитаете?",
        "options": ["Рок", "Поп-музыка", "Джаз"]
    },
    {
        "question": "Вопрос 9: Какое ваше любимое место для отдыха?",
        "options": ["Горы", "Море", "Кемпинг"]
    },
    {
        "question": "Вопрос 10: Какие фильмы вам нравится смотреть?",
        "options": ["Комедии", "Драмы", "Фантастика"]
    },
]

# Словарь для хранения ответов пользователей
user_answers = {}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Отправляем приветственное сообщение
    bot.send_message(message.chat.id, "Привет! Я бот для прохождения теста. Я задам тебе несколько вопросов.")

    # Начинаем тест
    ask_question(message.chat.id, 0)

# Функция для задания вопросов
def ask_question(chat_id, question_index):
    # Проверяем, все ли вопросы заданы
    if question_index >= len(questions):
        # Если все вопросы заданы, вычисляем результат
        result = calculate_result()
        bot.send_message(chat_id, f"Тест завершен! Результат: {result}")
        return

    # Отправляем очередной вопрос и кнопки с вариантами ответов
    question = questions[question_index]["question"]
    options = questions[question_index]["options"]

    # Создаем объект ReplyKeyboardMarkup для кнопок
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    # Добавляем кнопки с вариантами ответов
    for option in options:
        button = types.KeyboardButton(text=option)
        keyboard.add(button)

    # Отправляем вопрос и кнопки пользователю
    bot.send_message(chat_id, question, reply_markup=keyboard)

# Обработчик ответов пользователя
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Получаем ответ пользователя
    answer = message.text

    # Получаем текущий индекс вопроса для данного пользователя
    question_index = user_answers.get(message.chat.id, 0)

    # Сохраняем ответ пользователя
    user_answers[message.chat.id] = answer
    
    # Переходим к следующему вопросу
    ask_question(message.chat.id, question_index + 1)

# Функция для вычисления результата
def calculate_result():
    # Здесь можно использовать сохраненные ответы пользователя в словаре user_answers
    # и на основе них вычислить результат, отражающий подходящую специальность

    # Возвращаем простой заглушечный результат
    return "Результат"

# Запускаем бота
bot.polling()