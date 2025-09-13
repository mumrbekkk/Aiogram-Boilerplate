from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Hello welcome")

