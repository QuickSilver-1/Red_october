from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import InlineKeyboardButton, InputMediaPhoto
from aiogram.types import Message, CallbackQuery
from keyboards import *
from media import *
from config import config_1
from psycopg2 import connect
from psycopg2.errors import UniqueViolation
from asyncio import sleep
from random import choice
from hmac import new
from hashlib import sha256
from re import match


dp = Dispatcher()
bot = Bot(token=config_1.TOKEN)

class Delete(StatesGroup):
    delete_msg_id = State()

class Form(StatesGroup):
    await_msg = State()

class Register(StatesGroup):
    fio = State()
    age = State()
    city = State()
    mail = State()
    number = State()

# @dp.message(F.photo)
# async def photo_handler(message: Message) -> None:
#     photo_data = message.photo[-1]

#     await message.answer(f'{photo_data}')

@dp.message(CommandStart())
async def cmd_start(message: Message):
    connection = connect(config_1.POSTGRES_URL)
    cursor = connection.cursor()
    cursor.execute('''SELECT tg_id FROM "admin"''')
    admins = cursor.fetchall()
    connection.close()
    if str(message.from_user.id) in [i[0] for i in admins]:
        await message.answer(admin_text, reply_markup=admin_kb())
    else:
        await message.answer(text=hello1_text.format(name=message.from_user.first_name), reply_markup=start_kb())

@dp.callback_query(F.data == "Попробовать функции пользователя")
async def admin_to_user(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")

    await callback.message.answer(text="Чтобы вернуться к админ-меню нажмите на кнопку снизу", reply_markup=back_reply_kb())
    await user_start(message=callback.message)

        
@dp.message(F.text == "Вернуться в админ-панель")
async def back_to_home(message: Message):
    await cmd_start(message)

# async def user_start(message):
#     tg_id = str(message.from_user.id)
#     first_name = message.from_user.first_name
#     last_name = message.from_user.last_name
#     username = message.from_user.username
#     await create_user(tg_id, first_name, last_name, username)
#     await message.answer(photo=hello1_photo, caption=hello1_text.format(name=message.from_user.first_name), reply_markup=inline_kb_builder('hello1_text'))
        
@dp.callback_query(F.data == "Настроить рассылку")
async def get_message(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")

    await state.set_state(Form.await_msg)
    await callback.message.answer("Введите текст, который вы хотите разослать или добавьте медиа-файлы")

@dp.message(Form.await_msg)
async def send_msg(message: Message, state: FSMContext) -> None:
    await state.update_data(await_msg = message)

    sure = await message.answer(text = "Вы уверены, что хотите отправить это сообщение?", 
                                reply_markup = are_you_sure())
    await state.update_data(delete_msg = sure.message_id)

@dp.callback_query(F.data == "Да")
async def send_all(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer("")

    data = await state.get_data()
    mes = data.get("await_msg")
    connection = connect(config_1.POSTGRES_URL)
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT tg_id FROM users")
        users = cursor.fetchall()
    except Exception as e:
        print(f"The error '{e}' occurred")
    
    if mes.photo == None:
        for user in users:
            await bot.send_message(chat_id=user[0], text=mes.text)
    else:
        for user in users:
            await bot.send_photo(chat_id=user[0], photo=mes.photo[-1].file_id, caption=mes.caption)

    await callback.message.answer("Сообщение отправлено пользователям", reply_markup=admin_kb())
    await state.clear()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id = data.get("delete_msg"))

@dp.callback_query(F.data == "Нет")
async def cancel(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")

    data = await state.get_data()
    await callback.message.answer("Сообщение не отправлено", reply_markup=admin_kb())
    await state.clear()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id = data.get("delete_msg"))
    
@dp.callback_query(F.data == "Запись")
async def register(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.answer("")

    await state.set_state(Register.fio)
    await state.update_data(username=callback.message.from_user.username, tg_id=callback.message.from_user.id)
    await callback.message.answer(text="Расскажите немного о себе. Введите своё ФИО")

@dp.message(Register.fio)
async def reg_fio(message: Message, state: FSMContext) -> None:

    await state.update_data(fio=message.text)
    await state.set_state(Register.age)
    await message.answer(text="Введите свой возраст")

@dp.message(Register.age)
async def reg_age(message: Message, state: FSMContext) -> None:

    await state.update_data(age=message.text)
    await state.set_state(Register.city)
    await message.answer(text="В каком городе вы живете?")

@dp.message(Register.city)
async def reg_fio(message: Message, state: FSMContext) -> None:

    await state.update_data(city=message.text)
    await state.set_state(Register.mail)
    await message.answer(text="Введите свою электронную почту")

@dp.message(Register.mail)
async def reg_fio(message: Message, state: FSMContext) -> None:

    if match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', message.text) is None:
        await message.answer(text="Неправильный формат данных, попробуйте снова")

    await state.update_data(email=message.text)
    await state.set_state(Register.number)
    await message.answer(text="Отправьте свой номер", reply_markup=contact_keyboard())

@dp.message(Register.number)
async def reg_final(message: Message, state: FSMContext) -> None:
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    tg_id = message.from_user.id
    username = message.from_user.username
    fio = data["fio"]
    age = data["age"]
    city = data["city"]
    email = data["email"]
    number = data["number"]
    await state.clear()
    await create_user(tg_id, username, fio, age, city, email, number)
    await message.answer(text=main_text, reply_markup=main_menu_kb())

async def create_user(tg_id, username, fio, age, city, email, number):
    try:
        connection = connect(config_1.POSTGRES_URL)
        cursor = connection.cursor()
        cursor.execute(f'''INSERT INTO users (tg_id, username, fio, age, city, email, number) VALUES ('{tg_id}', '{username}', '{fio}', '{age}', '{city}', '{email}', '{number}')''')
        connection.commit()
        connection.close()
    except UniqueViolation:
        pass

@dp.callback_query(F.data == "Лотерея")
async def fortune(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=loto_text, reply_markup=loto_kb())

@dp.callback_query(F.data == "Главное меню")
async def main_menu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=main_text, reply_markup=main_menu_kb())

@dp.callback_query(F.data == "Фонд")
async def get_information(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=info_text, reply_markup=information_kb())

@dp.callback_query(F.data == "Линия")
async def hot_line(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text=line_text, reply_markup=bot_kb())



