from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from media import *


def contact_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(
        text="Отправить номер", request_contact=True
    )
    
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def moscow_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="ТЦ Европейский", callback_data="Европейский"
    )
    builder.button(
        text='ТЦ "Авиапарк"', callback_data="Авиапарк"
    )
    builder.button(
        text='ТЦ "Метрополис"', callback_data="Метрополис"
    )
    builder.button(
        text="Выставка InterCHARM", callback_data="Выставка"
    )

    builder.adjust(1)
    return builder.as_markup()    

def reg_intimissimi_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Регистрация", callback_data="Intimissimi"
    )
    builder.button(
        text="Главное меню", callback_data="Главное меню"
    )

    builder.adjust(1)
    return builder.as_markup()

def reg_intersharm_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Регистрация", callback_data="Интершарм"
    )
    builder.button(
        text="Главное меню", callback_data="Главное меню"
    )

    builder.adjust(1)
    return builder.as_markup()

def more_kb():
    builder = InlineKeyboardBuilder()
    
    builder.button(
        text="Розовый Октябрь", url="https://pinkoctober.ru/"
    )
    builder.button(
        text='Фонд "Дальше"', url="https://www.dalshefond.ru/"
    )
    builder.button(
        text="Пособие по профилактике рака груди", url="https://www.dalshefond.ru/prevention-manual/"
    )
    builder.button(
        text="Чек-лист заботы о здоровье груди(нужен файл)", callback_data="РО2024"
    )

    builder.adjust(1)
    return builder.as_markup()

def consultation_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Очно", callback_data="Очно"
    )
    builder.button(
        text="Онлайн", callback_data="Онлайн"
    )
    
    builder.adjust(2)
    return builder.as_markup()

def city_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Москва", callback_data="Москва"
    )
    builder.button(
        text="Воронеж", callback_data="Воронеж"
    )
    builder.button(
        text="Казань", callback_data="Казань"
    )
    builder.button(
        text="Нижний Новгород", callback_data="Нижний Новгород"
    )
    builder.button(
        text="Сочи", callback_data="Сочи"
    )
    
    builder.adjust(1)
    return builder.as_markup()


def main_menu_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Узнать больше", callback_data="Узнать"
    )
    builder.button(
        text="Спросить врача", callback_data="Спросить"
    )
    builder.button(
        text="Помочь", url="https://dalshefond.ru/donate/"
    )
    builder.button(
        text="Получить помощь", callback_data="Помощь"
    )

    builder.adjust(1)
    return builder.as_markup()

def help_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Горячая линия", callback_data="Линия"
    )
    builder.button(
        text="Служба поддержки", url="https://vmesteplus.ru/"
    )
    builder.button(
        text='Курс "Что важно знать о раке молочной железы"', url="https://vmesteplus.ru/distance-programs/oncologist-course/"
    )
    builder.button(
        text='Курс "Рак молочной железы: как принять диагноз"', url="https://vmesteplus.ru/distance-programs/psychologist-course/"
    )
    builder.button(
        text="Руководство для пациентов с диагнозом рак груди", url="https://www.dalshefond.ru/practical-guide/"
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

def menu_kb():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Главное меню", callback_data="Главное меню"
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
        text="Отправить", callback_data="Отправить"
    )

    builder.adjust(1)
    return builder.as_markup()
