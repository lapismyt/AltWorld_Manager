import discord
from discord.ext import commands
from mctools import RCONClient

with open("token.txt") as f:
    token = f.read().strip()

with open("admin.txt") as f:
    admin = f.read().strip()

with open("rcon_passwd.txt") as f:
    rcon_passwd = f.read().strip()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=">", intents=intents)

rcon = RCONClient("titan.minecraft.rent:25681")
success = rcon.login(rcon_passwd)

@bot.command()
async def ping(ctx):
    await ctx.reply("Pong!")

@bot.command()
@commands.has_any_role("AltWorld Admin")
async def w(ctx):
    await ctx.reply(f"Пользователь {ctx.message.content.split()[1]} (Java) добавлен в вайтлист!")

@bot.command()
@commands.has_any_role("AltWorld Admin")
async def fw(ctx):
    await ctx.reply(f"Пользователь {ctx.message.content.split()[1]} (Bedrock) добавлен в вайтлист!")

bot.run(token)
