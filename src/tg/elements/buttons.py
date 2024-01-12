from telegram import InlineKeyboardButton

from src.tg.elements.base import BaseCallbackConstructor
from src.tg.elements.data import CallbackData


class CallbackOneArg(BaseCallbackConstructor):
    __slots__ = ["game_id", "callback"]
    splitter = "="

    def __init__(self, callback: CallbackData, value: str):
        self.callback = callback
        self.value = value

    @property
    def callback_data(self):
        return self.callback + self.splitter + self.value

    @classmethod
    def from_callback_data(cls, callback_data: str):
        return cls(*callback_data.split(cls.splitter))


class ExampleButton(InlineKeyboardButton):
    def __init__(self, value: str):
        callback_data = str(CallbackOneArg(CallbackData.EXAMPLE, value))
        super().__init__("example button", callback_data=callback_data)
