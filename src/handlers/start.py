from aiogram import types, Router
from aiogram.filters import CommandStart

start_router = Router(name="start_r")


@start_router.message(CommandStart())
async def greet(message: types.Message) -> None:
    await message.answer(text="Добро пожаловать!")
