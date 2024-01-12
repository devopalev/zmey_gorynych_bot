from functools import partial

from telegram.helpers import escape_markdown

from src.tg.elements.base import BaseMessage

escape_markdown_2 = partial(escape_markdown, version=2)


class HelpMessage(BaseMessage):
    def __init__(self):
        self.text = "Справка бота"


class BadCallbackMessage(BaseMessage):
    def __init__(self):
        self.text = "Не удалось распознать кнопку\\, возможно она устарела"


class StartMessage(BaseMessage):
    def __init__(self, fullname):
        self.text = f"Привет, {fullname}!\nИспользуй /help для вызова справки"
