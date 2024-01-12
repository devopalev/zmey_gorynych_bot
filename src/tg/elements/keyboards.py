from telegram import InlineKeyboardMarkup

from src.tg.elements import buttons


class ExampleButton(InlineKeyboardMarkup):
    def __init__(self):
        keyboard = [[buttons.ExampleButton]]
        super().__init__(keyboard)
