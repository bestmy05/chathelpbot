from dis import disco
import imp
from tkinter import Variable
from unicodedata import name
import discord
from discord.ext import commands
import timetable

prefix = "!"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    game = discord.Game("테스트")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("ready!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return None
    
    await bot.process_commands(message)

@bot.command(name="test")
async def react_test(ctx):
    await ctx.channel.send("testing")

@bot.command(name="시간표")
async def time_table(ctx, SC_NAME, GRAND, CLASS):
    await ctx.channel.send(timetable.TimeTable(SC_NAME, GRAND, CLASS))

@time_table.error
async def time_table_error(ctx, error):
    await ctx.channel.send("명령어를 확인해주세요")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어를 찾지 못했습니다")

bot.run("OTc3MTk3Mjg4OTA2NjkwNTkx.GckM5f.NbaPJPzyNyk_tZnM2YNdvFhlQujSasaZzb2QM0")