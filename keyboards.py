from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🧠 Изучить технику", callback_data="menu_techniques")
    builder.button(text="⚙️ Создать фразу", callback_data="menu_build")
    builder.button(text="💡 Афоризм", callback_data="menu_wisdom")
    builder.button(text="🎯 Задание дня", callback_data="menu_train")
    builder.adjust(2)
    return builder.as_markup()

def techniques_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Трюизмы", callback_data="tech_truisms")
    builder.button(text="Иллюзия выбора", callback_data="tech_choice")
    builder.button(text="Да-цикличка", callback_data="tech_yeschain")
    builder.button(text="Потому что", callback_data="tech_because")
    builder.button(text="Утилизация", callback_data="tech_utilization")
    builder.button(text="◀️ Назад", callback_data="back_to_main")
    builder.adjust(2)
    return builder.as_markup()

def back_to_techniques_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="◀️ Назад к техникам", callback_data="back_to_techniques")
    return builder.as_markup()

def back_to_main_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="◀️ В главное меню", callback_data="back_to_main")
    return builder.as_markup()
