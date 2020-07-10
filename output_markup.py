from telebot import types


def generate_markup():
    variants = ["Yas", "Nah", "Dunno"]
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for variant in variants:
        markup.add(variant)
    return markup
