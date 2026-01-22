import discord
from openai import OpenAI
import os

ai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Bot online")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    response = ai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Reply like a chill human friend, Hinglish"},
            {"role": "user", "content": message.content}
        ]
    )

    await message.channel.send(response.choices[0].message.content)

bot.run(os.getenv("DISCORD_TOKEN"))
