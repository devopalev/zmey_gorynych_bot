import asyncio
import logging

from telegram.constants import ParseMode
from telegram.ext import CallbackContext, ExtBot

from src.repository import AbstractRepository, Repository, RepositoryMemory
from src.tg.elements.base import BaseMessage

KEY_STORAGE = "game"

logger = logging.getLogger(__name__)


class CustomContext(CallbackContext[ExtBot, dict, dict, dict]):
    """Custom class for context."""

    db_storage: AbstractRepository = Repository()

    def send_events(self, event: BaseMessage, users_id: list[int]):
        async def async_send_event(user_id: int, text: str, parse_mode: ParseMode):
            try:
                await self.bot.send_message(user_id, text, parse_mode)
            except Exception as err:
                logger.warning(f"Не удалось отправить сообщение ({text}) пользователю {user_id}: {err}", exc_info=True)

        for tg_id in users_id:
            asyncio.create_task(async_send_event(tg_id, event.text, event.parse_mode))


class MemoryCustomContext(CustomContext):
    db_storage: AbstractRepository = RepositoryMemory()
