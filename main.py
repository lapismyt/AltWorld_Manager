import discord
from discord.ext import commands

with open("token.txt") as f:
    token = f.read().strip()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.command()
async def ping(ctx):
    ctx.send("Pong!")

bot.run(token)
