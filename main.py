import discord
from discord.ext import commands
import requests as req
import pymongo
import os
from dotenv import load_dotenv

client = commands.Bot(command_prefix='-', intents=intents.all())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx,arg):
    userid = getUserId(ctx,arg)
    await ctx.author.send(userid) 

@client.event
async def on_member_join(member):
    print("Recognized that " + member.name + " joined")
    await member.send(newUserDmMessage)
    print("Sent message to " + member.name)

client.run(TOKEN)