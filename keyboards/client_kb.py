from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

group_list_btn = KeyboardButton('/Список групп')
enter_id_btn = KeyboardButton('/Авторизироваться')
kb_client = ReplyKeyboardMarkup()
kb_client.add(group_list_btn).add(enter_id_btn)