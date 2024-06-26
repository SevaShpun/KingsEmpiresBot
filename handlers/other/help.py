from loader import dp
from aiogram import types
from utils.misc.read_file import read_txt_file
from keyboards.help import kb_help


@dp.message_handler(state="*", commands="help")
@dp.throttled(rate=1)
async def help_handler(message: types.Message):
    msg_text = read_txt_file("text/help")
    await message.answer(
        msg_text,
        reply_markup=kb_help
    )
    # print(message.from_user.last_name)



