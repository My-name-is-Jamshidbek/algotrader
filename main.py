import logging
from aiogram import Bot, Dispatcher, executor, types
import cryptocompare
API_TOKEN = '5480591291:AAHTGkyT6sd9GlNqmfr8jB9yo1oNocRqd_c'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    # joriy_narx_m_id = await bot.send_message(2081653869,'joriy narx')
    # bizdagi_pul_m_id = await bot.send_message(2081653869,'bizdagi pul')
    # bizdagi_coin = await bot.send_message(2081653869,'bizdagi coin')
    # holat_m_id = await bot.send_message(2081653869,'holat')
    # sotib_olingan_narx_m_id = await bot.send_message(2081653869,'sotib olingan narx')
    # sotib_yuborilgan_narx_m_id = await bot.send_message(2081653869,'sotib yuborilgan narx')
    # foyda_m_id = await bot.send_message(2081653869,'foyda')
    m_id = await message.answer('boshlandi')
    if message.from_user.id == 2081653869:
        MY_KEY = 'd94cd11e163c04b4df01a96ea83085fd2c1385f7d3fd9647a0db479b92b4a276'
        cryptocompare.cryptocompare._set_api_key_parameter(MY_KEY)
        bizdagi_coin = 0
        bizdagi_pul = 100
        sotib_olingan_narx = 0
        sotib_yuborilgan_narx = 0
        joriydan_oldingi_narx=0
        bitcoin = False
        tur,mal,qoldiq = '','b',0
        while True:
            a = cryptocompare.get_price('BTC', currency='USD', full=True)
            joriy_narx=int(a['RAW']['BTC']['USD']['PRICE'])
            if bitcoin:
                 if joriydan_oldingi_narx < joriy_narx:
                     tur = 'sotilgan'
                     bizdagi_pul=bizdagi_coin*joriy_narx
                     bizdagi_coin = 0
                     sotib_yuborilgan_narx = joriy_narx
                     bitcoin=False
                     if bizdagi_pul>100:
                         qoldiq+=bizdagi_pul-100
                         bizdagi_pul=100
            else:
                if joriydan_oldingi_narx > joriy_narx:
                    tur = 'sotibolingan'
                    bizdagi_coin=bizdagi_pul/joriy_narx
                    bizdagi_pul=0
                    sotib_olingan_narx=joriy_narx
                    bitcoin=True
            mal = (f"joriy narx = {joriy_narx},\n"
                   f"tur = {tur}\n"
                   f"sotib olingan narx = {sotib_olingan_narx}\n"
                   f"sotilgan narx = {sotib_yuborilgan_narx}\n"
                   f"bizdagi coin = {bizdagi_coin}\n"
                   f"bizdagi pul = {bizdagi_pul}\n"
                   f"foyda = {qoldiq}\n"
                   )
            joriydan_oldingi_narx = joriy_narx
            # await bot.edit_message_text(chat_id=2081653869,message_id=m_id.message_id,text=mal,reply_markup=None/)
            m_id=await message.answer(
                text=mal
            )
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)