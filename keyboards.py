from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from media import *


def admin_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Настроить рассылку", callback_data="Настроить рассылку"
    )
    builder.button(
        text="Попробовать функции пользователя", callback_data="Попробовать функции пользователя"
    )
    builder.button(
        text="Розыгрыш", callback_data="Рандом"
    )

    builder.adjust(1)
    return builder.as_markup()

def are_you_sure():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Да", callback_data="Да"
    )
    builder.button(
        text="Нет", callback_data="Нет"
    )
    builder.adjust(1)
    return builder.as_markup()

def back_reply_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="Вернуться в админ-панель",
    )

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def inline_kb_builder(callback: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=callback_keys[callback],
        callback_data=callback
    )

    return builder.as_markup(resize_keyboard=True)

def contact_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(
        text="Отправить номер", request_contact=True
    )
    
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def main_menu_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Записаться на акцию", callback_data="Запись"
    )
    builder.button(
        text="Беспроигрышная лотерея", callback_data="Лотерея"
    )
    builder.button(
        text="Познакомиться с Фондом", callback_data="Фонд"
    )
    builder.button(
        text="Горячая линия", callback_data="Линия"
    )
    builder.button(
        text="5 шагов к здоровью груди", callback_data="5 шагов"
    )
    builder.button(
        text="Мерч", callback_data="Мерч"
    )

    builder.adjust(1)
    return builder.as_markup()

def loto_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Ссылка на оплату", url="https://dalshefond.ru/donate/"
    )
    builder.button(
        text="Главное меню", callback_data="Главное меню"
    )

    builder.adjust(1)
    return builder.as_markup()

def start_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Вперед", callback_data="Главное меню"
    )

    builder.adjust(1)
    return builder.as_markup()

def information_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Сайт Фонда", url="https://dalshefond.ru/",
    )
    builder.button(
        text="Сайт РО2024", url="https://pinkoctober.ru/info",
    )
    builder.button(
        text="ТГ канал", url="https://t.me/dalshefond",
    )
    builder.button(
        text="Пожертвования", url="https://dalshefond.ru/donate/"
    )
    builder.button(
        text="Главное меню", callback_data="Главное меню"
    )

    builder.adjust(1)
    return builder.as_markup()

def bot_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Чат-бот", url="https://t.me/dalshe_fond_bot"
    )
    builder.button(
        text="Главное меню", callback_data="Главное меню"
    )

    builder.adjust(1)
    return builder.as_markup()
