import discord
from discord.ext import commands
from mctools import RCONClient
from mctools.formattertools import DefaultFormatter
import re

with open("token.txt") as f:
    token = f.read().strip()

with open("admin.txt") as f:
    admin = f.read().strip()

with open("rcon_passwd.txt") as f:
    rcon_passwd = f.read().strip()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

rcon = RCONClient("titan.minecraft.rent", 25748)

success = rcon.login(rcon_passwd)

if success == False:
    exit(2)

def remove_cc(text):
    pattern = r"\x1b\[[0-9;]+m"
    return re.sub(pattern, "", text)

def cmd(command):
    resp = DefaultFormatter.clean(rcon.command(command))
    if resp == "":
        resp = "None"
    return resp

@bot.command()
async def ping(ctx):
    await ctx.reply("Pong!")

@bot.command()
@commands.has_any_role("AltWorld Admin")
async def w(ctx):
    print(ctx.message.content)
    action = ctx.message.content.split()[1]
    if not action == "rl":
        nick = ctx.message.content.split()[2]
    if action == "add":
        action = "add"
        resp = cmd(f"whitelist add {nick}")
        await ctx.reply(f"Игрок {nick} (Java) добавлен в вайтлист.\n```ansi\n{resp}```")
    elif action == "rm":
        action = "remove"
        resp = cmd(f"whitelist remove {nick}")
        await ctx.reply(f"Игрок {nick} (Java) удалён из вайтлиста.\n```ansi\n{resp}```")
    elif action == "rl":
        action == "reload"
        resp = cmd(f"whitelist reload")
        await ctx.reply(f"Вайтлист перезагружен.\n```ansi\n{resp}```")
    else:
        await ctx.reply("Неверный синтаксис команды.")

@bot.command()
@commands.has_any_role("AltWorld Admin")
async def fw(ctx):
    print(ctx.message.content)
    action = ctx.message.content.split()[1]
    if not action == "rl":
        nick = ctx.message.content.split()[2]
    if action == "add":
        action = "add"
        resp = cmd(f"fwhitelist add {nick}")
        await ctx.reply(f"Игрок {nick} (Bedrock) добавлен в вайтлист.\n```ansi\n{resp}```")
    elif action == "rm":
        action == "remove"
        resp = cmd(f"fwhitelist remove {nick}")
        await ctx.reply(f"Игрок {nick} (Bedrock) удалён из вайтлиста.\n```ansi\n{resp}```")
    elif action == "rl":
        action == "reload"
        resp = cmd(f"whitelist reload")
        await ctx.reply(f"Вайтлист перезагружен.\n```ansi\n{resp}```")
    else:
        await ctx.reply("Неверный синтаксис команды.")

@bot.command()
@commands.has_any_role("AltWorld Admin")
async def e(ctx):
    print(ctx.message.content)
    command = ctx.message.content.removeprefix("/e ")
    resp = cmd(command)
    await ctx.reply(f"```ansi\n{resp}```")

bot.run(token)
