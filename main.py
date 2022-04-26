from discord.ext.commands import Bot
from discord.ext import commands
import discord

from musicbot import Music

from youtube_dl import YoutubeDL

import sys 

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

bot.add_cog(Music(bot))

with open(sys.argv[1], 'r') as f:
    token = f.read()

bot.run(token)