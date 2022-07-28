import discord # Import the discord library
from discord.ext import commands # Import the commands library
import mysql.connector # Import the mysql connector





mydb = mysql.connector.connect(host="", user="", passwd="", database="") #connect to database
cursor = mydb.cursor(dictionary=True) #create cursor


bot = commands.Bot(command_prefix='!', description="description  !" , STATUS=discord.Status.online) #Prefix for commands and status of bot


@bot.event
async def on_ready():
    print('Logged in as') #print login
    print(bot.user.name) #print name
    print(bot.user.id) #print id
    print('------')


#command ping
@bot.command() 
async def ping(ctx): 
    await ctx.send('Pong!') #send message




bot.run("TOKEN") #Token of the bot

