import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests
import os
from fetch import *

#Loading in bot key from local file
load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")

#Defining the bots command prefix
bot = commands.Bot(command_prefix="!")

# urls = fetch(subreddit = "memes")
# print(urls)

#When bot is activated will run this
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected!')

#When the crawl command is executed
@bot.command(name="crawl", help="reddit crawler")
async def crawl(ctx, subreddit = None, mode = "random", limit = 1, time = "week"):
    if not subreddit:
        await ctx.send("Please specify a subreddit")
    else:
        url = fetch(subreddit=subreddit, mode=mode, limit= limit, time=time)
        await ctx.send(url)

#Running bot
bot.run(DISCORD_KEY)