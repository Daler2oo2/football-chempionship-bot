from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# Список туров
tours_list = ["Турsdffsfdfsdfsf 1", "Турdfsffdfdfsf 2", "Турsdfsdfdfsdfsdff 3"]

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = KeyboardButton("📋 Тур")
    item2 = KeyboardButton("👥 Команды")
    markup.row(item1, item2)

    await message.answer("Выберите действие:", reply_markup=markup)

@dp.message_handler(lambda message: message.text == "📋 Тур")
async def send_tours(message: types.Message):
    # Создаем клавиатуру с кнопками внутри сообщения
    inline_markup = InlineKeyboardMarkup(row_width=4)

    for tour in tours_list:
        inline_markup.add(
            InlineKeyboardButton( "📋" + tour, callback_data=f"show_tour_{tour}"),
        )
        inline_markup.add(
            InlineKeyboardButton("Изменить", callback_data=f"edit_tour_{tour}"),
            InlineKeyboardButton("Удалить", callback_data=f"delete_tour_{tour}"),
        )

    # Добавляем кнопку "Добавить"
    inline_markup.add(InlineKeyboardButton("Добавить", callback_data="add_tour"))

    await message.answer("Список туров:", reply_markup=inline_markup)

# Обработчик для нажатий на кнопки внутри сообщения
@dp.callback_query_handler(lambda query: query.data.startswith(('show_tour_', 'edit_tour_', 'delete_tour_')))
async def handle_tour_buttons(callback_query: types.CallbackQuery):
    action, tour = callback_query.data.split('_')[0], callback_query.data.split('_')[2]

    if action == 'show':
        await bot.send_message(callback_query.from_user.id, f"Выбран тур: {tour}")
    elif action == 'edit':
        await bot.send_message(callback_query.from_user.id, f"Вы выбрали изменение тура: {tour}")
    elif action == 'delete':
        await bot.send_message(callback_query.from_user.id, f"Вы выбрали удаление тура: {tour}")
    elif action == 'back':
        await send_welcome(callback_query.message)

    await bot.answer_callback_query(callback_query.id)

# Обработчик для кнопки "Добавить"
@dp.callback_query_handler(lambda query: query.data == 'add_tour')
async def add_tour(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Добавление нового тура")

    # Ваш код для добавления нового тура

    await bot.answer_callback_query(callback_query.id)

# Запускаем бота
executor.start_polling(dp, skip_updates=True)
