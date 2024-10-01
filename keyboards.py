from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from media import *


def contact_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(
        text="Отправить номер", request_contact=True
    )
    
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def reg_side():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Intimissimi", callback_data="Intimissimi"
    )
    builder.button(
        text="Интершарм", callback_data="Интершарм"
    )
    builder.button(
        text="Главное меню", callback_data="Главное меню"
    )

    builder.adjust(1)
    return builder.as_markup()

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
        text="Пособие по самодиагностике", callback_data="Пособие по самодиагностике"
    )
    builder.button(
        text="РО2024", callback_data="РО2024"
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

def RO2024_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Пожертвования", url="https://dalshefond.ru/donate/"
    )
    builder.button(
        text="Главное меню", callback_data="Главное меню"
    )

    builder.adjust(1)
    return builder.as_markup()

def agree_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Отправить", callback_data="Отправитьг"
    )

    builder.adjust(1)
    return builder.as_markup()
