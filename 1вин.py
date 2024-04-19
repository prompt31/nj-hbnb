from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

TOKEN = "6743604043:AAEXDyn2ZqUwGoFTk1j7ipucyPFIXTXihcQ"

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id  # Получаем ID пользователя
    context.bot.send_message(6658612764, f"Новый пользователь присоединился! ID: {user_id}")

    user_name = update.message.from_user.first_name
    message = f"👋 Привет, {user_name}!\n\n🚀 Это бесплатный бот с сигналами на Lucky Jet.\n\n📲 Для начала необходимо провести регистрацию на 1win (провайдер игры LuckyJet). Чтобы бот успешно выдавал верные коэффициенты, нужно соблюсти важные условия:\n\n1️⃣ Аккаунт обязательно должен быть НОВЫМ! Если у вас уже есть аккаунт и при нажатии на кнопку «РЕГИСТРАЦИЯ» вы попадаете на старый, необходимо выйти с него и заново нажать на кнопку «РЕГИСТРАЦИЯ», после чего по новой зарегистрироваться!\n\n 2️⃣ чтобы бот смог проверить вашу регистрацию, обязательно нужно ввести промокод exover1  при регистрации!\n\nПосле РЕГИСТРАЦИИ нажмите на кнопку '✅ Продолжить'."

    keyboard = [
        [InlineKeyboardButton("✅ Продолжить", callback_data='continue_registration')],
        [InlineKeyboardButton("👋ТЕХ.ПОДДЕРЖКА", url='https://t.me/exteabot')],
        [InlineKeyboardButton("🚀РЕГИСТРАЦИЯ", url='https://1wnurc.com/#ksf8')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(message, reply_markup=reply_markup)

# Остальной ваш код для обработки callback'ов и запуска бота

def generate_random_signal() -> float:
    # Генерируем случайное число с плавающей точкой от 1.01 до 9.99
    import random
    return round(random.uniform(1.01, 3.99), 2)

def get_signal(update: Update, context: CallbackContext) -> None:
    signal_value = generate_random_signal()
    text = f"🚀{signal_value}x\n"

    update.callback_query.answer()  # Отправляем ответ о выполнении команды
    update.callback_query.message.reply_text(text)

    # Обновляем сообщение с кнопками после получения первого сигнала
    keyboard = [
        [InlineKeyboardButton("ПОЛУЧИТЬ СИГНАЛ", callback_data='get_signal_again')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text("Хотите еще один сигнал?", reply_markup=reply_markup)

def continue_registration(update: Update, context: CallbackContext) -> None:
    message = "✅ Теперь вы можете получать сигналы и зарабатывать!\n\n❗️ Проверьте, что бы вы точно были зарегистрированы именно по ссылке в боте. Если вы создали новый аккаунт, нажмите 'ПОЛУЧИТЬ СИГНАЛ'."

    keyboard = [
        [InlineKeyboardButton("ПОЛУЧИТЬ СИГНАЛ", callback_data='get_signal')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.edit_message_text(text=message, reply_markup=reply_markup)


def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'continue_registration':
        continue_registration(update, context)
    elif query.data == 'get_signal':
        get_signal(update, context)
    elif query.data == 'return_to_registration':
        start(update, context)  # Возвращаемся к началу регистрации
    elif query.data == 'get_signal_again':
        get_signal(update, context)  # Получаем еще один сигнал

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_click))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
