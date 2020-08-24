import os
import random
import fileinput

import discord 
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

def random_line(filename):
    line_num = 0
    selected_line = ''
    with open(filename, encoding="utf8") as f:
        while 1:
            line = f.readline()
            if not line: break
            line_num += 1
            if random.uniform(0, line_num) < 1:
                selected_line = line
    return selected_line.strip()


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            f.write(f'swag')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'naruto character' in message.content.lower():
        word = random_line('characters.txt')
        response = word
        await message.channel.send(response)
    elif 'what character should brandon play' in message.content.lower():
        word = random_line('valorant(b).txt')
        response = word
        await message.channel.send(response)
    elif 'what character should i play' in message.content.lower():
        word = random_line('valorant.txt')
        response = word
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException


client.run(TOKEN)