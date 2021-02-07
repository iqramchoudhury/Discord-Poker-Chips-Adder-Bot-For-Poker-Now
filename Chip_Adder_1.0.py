import discord
from discord.ext import commands
import csv

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready!')


#Change file path to where csv is downloaded to and rename the file to chosen name
@client.command()
async def Add_Chips(ctx, x):
    file = open(r"C:\Users\user\Downloads\chips_rank.csv", "r", encoding='ANSI')
    csv_reader = csv.reader(file)
    for line in csv_reader:
        await ctx.send('!pac {} {}'.format(line[2],x))

#Change file path to where csv is downloaded to and rename the file to chosen name
@client.command()
async def Remove_Chips(ctx, x):
    file = open(r"C:\Users\user\Downloads\chips_rank.csv", "r", encoding='ANSI')
    csv_reader = csv.reader(file)
    for line in csv_reader:
        await ctx.send('!prc {} {}'.format(line[2],x))


#Add your bot token
client.run('ADD_YOUR_BOT_TOKEN_HERE')