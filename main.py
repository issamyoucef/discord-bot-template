import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file
token = os.getenv('DISCORD_TOKEN') # gets the discord bot token

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents) # the symbol you type before running a command, in this case it's . (dot)


@bot.event
async def on_ready():
    print(f'Your bot {bot.user.name} is now online!')