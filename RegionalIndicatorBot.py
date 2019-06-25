import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = ""
Botspace = 'regional-land'
prefix = '$'
bot = commands.Bot(command_prefix=prefix)
numDict = {
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
}
specialDict = {
	'a':'a',
	'b':'b',
	'o':'o',
	'x':'x',
	'i':'information_source',
	'p':'parking',
	'm':'m',
	'!':'exclamation',
    '?':'question',
	'+':'heavy_plus_sign',
	'-':'heavy_minus_sign'
	
}

@bot.event
async def on_ready():
    print('Bot Ready!')

@bot.event
async def on_message(message):
    if message.author != bot.user:
        if message.content.startswith(prefix):
            await bot.process_commands(message)
        elif message.channel.name == Botspace:
            print('Converting..."' + message.content + '"')
            sendMsg = ''
            for i in message.content.lower():
                if i in specialDict:
                    sendMsg += ':' + specialDict[i] + ":"
                elif i.isnumeric():
                    sendMsg += ":" + numDict[i] + ":"
                elif i.isalpha():
                        sendMsg += ":regional_indicator_" + i + ":"
                else:
                    sendMsg += '         '
                sendMsg += ' '
            chunkingList = list()
            while len(sendMsg) > 2000:
                idx = sendMsg[:2000].rfind(" :")
                chunkingList.append(sendMsg[:idx])
                sendMsg = sendMsg[idx:]
            chunkingList.append(sendMsg)
            for chunk in chunkingList:
                if chunk:
                    await message.channel.send(chunk)

@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(latency)

@bot.command()
async def createBotspace(ctx):
    createBotspace = True
    for channel in ctx.guild.channels:
        if channel.name == Botspace:
            createBotspace = False
    if (createBotspace):
        await ctx.guild.create_text_channel(Botspace)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run(TOKEN)