from telegram import BotCommand
from telegram.ext import (BaseHandler,
                          CommandHandler,
                          CallbackQueryHandler,
                          Application)

from src.tg.elements.data import CallbackData
from src.tg.elements.data import CommandData
from src.tg.handlers import common
from src.tg.handlers.common import ignore_callback
from src.tg.handlers.common import unknown_callback
from src.tg.utils.tg_calendar import CallbackBuilder


def build_handlers() -> list[BaseHandler]:
    """
    Строитель обработчиков BaseHandler
    :return: list[BaseHandler]
    """
    unknown_handlers = [CallbackQueryHandler(unknown_callback, pattern=CallbackData.UNKNOWN.regex)]
    calendar_handler = CallbackQueryHandler(common.handle_calendar, CallbackBuilder.base_cb)

    handlers = [
        CommandHandler(CommandData.START, common.handle_start),
        CommandHandler(CommandData.HELP, common.handle_help),
        calendar_handler,
        CallbackQueryHandler(ignore_callback, pattern=CallbackData.IGNORE.regex),
        *unknown_handlers
    ]
    return handlers


def build_commands() -> list[BotCommand]:
    commands = [
        BotCommand(CommandData.START, CommandData.START.description),
        BotCommand(CommandData.HELP, CommandData.HELP.description),
    ]
    return commands


async def setup(app: Application):
    handlers = build_handlers()
    commands = build_commands()

    app.add_handlers(handlers)
    await app.bot.set_my_commands(commands)
