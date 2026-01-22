import discord
from openai import OpenAI
import os

# OpenAI client
ai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Discord intents
intents = discord.Intents.default()
intents.message_content = True

# Discord client
bot = discord.Client(intents=intents)

# Bot online event
@bot.event
async def on_ready():
    print("Bot online")

# Message event
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # OpenAI reply
    response = ai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Reply like a chill human friend, Hinglish"},
            {"role": "user", "content": message.content}
        ]
    )

    # Send reply in Discord
    await message.channel.send(response.choices[0].message.content)

# Run bot
bot.run(os.getenv("DISCORD_TOKEN"))
