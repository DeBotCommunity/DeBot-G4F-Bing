import g4f
from telethon import events
from userbot import client

info = {'category': 'tools', 'pattern': '.gpt', 'description': 'Задать вопрос ChatGPT 4'}

@client.on(events.NewMessage(outgoing=True, pattern=r'(?s)^\.gpt (.+)$'))
async def gpt(event):
    await event.edit('<b>♻️ Генерирую ответ, ожидайте...</b>', parse_mode='HTML')
    message = event.pattern_match.group(1)
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_4,
        provider=g4f.Provider.Bing,
        messages=[{"role": "user", "content": str(message)}],
    )
    await event.edit(response, parse_mode='Markdown')
