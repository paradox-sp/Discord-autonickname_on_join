import discord
import os
from dotenv import load_dotenv

load_dotenv()
get_token = os.environ['token']

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name='RIP'))


@client.event
async def on_member_join(member):
    await member.edit(nick="RIP")


client.run(get_token)
