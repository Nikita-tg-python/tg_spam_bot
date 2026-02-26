from telethon import TelegramClient
import asyncio
from random import randrange as R
from random import choice as C
from random import sample as S

api_id = API_ID

api_hash = API_HASH


target_chats = [
    # 'https://t.me/joinchat/...' # Можно и ссылки, но лучше юзернеймы
]


client = TelegramClient('my_userbot_session', api_id, api_hash)

async def main():
    print("Бот запущен! Начинаю рассылку...")
    
    while True:

        for chat in target_chats:

            message_text = f'''
            Текст который будет росылаться'''

            try:
                await client.send_message(chat, message_text)
                print(f"Отправлено в: {chat}")
                
                await asyncio.sleep(R(15, 20)) 
                
            except Exception as e:
                print(f"Ошибка с {chat}: {e}")
        
        time = R(10, 15)
        print(f"Жду {time} минут до следующей рассылки...")
        await asyncio.sleep(time * 60)

with client:
    client.loop.run_until_complete(main())