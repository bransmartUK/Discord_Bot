import os
import random
import fileinput
import random

import discord 
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

def dictinize(filename_text):
    d = {}
    with open(filename_text) as f:
        for line in f:
            (key, val) = line.split(" ",1)
            d[int(key)] = val
    return d

survPerks = dictinize("survivorperks.txt")
killerPerks = dictinize("killerperks.txt")
helpPage = open('help.txt', 'r').read()
patchPage = open('patchnotes.txt', 'r').read()
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


def randomPerks(referredDictionary):
    numb = 0
    arrayOfUsedNumbers = []
    listOfPerks = []
    while numb != 4:
        randNumb = random.randint(1, len(referredDictionary))
        if randNumb in arrayOfUsedNumbers:
            continue
        else:
            arrayOfUsedNumbers.append(randNumb)
            listOfPerks.append(referredDictionary.get(randNumb))
            numb = numb + 1
    return listOfPerks



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

    if 'what naruto character am i' in message.content.lower():
        word = random_line('characters.txt')
        response = word
        await message.channel.send(response)
    elif 'what ua student am i' in message.content.lower():
        word = random_line('UAstudents.txt')
        response = word
        await message.channel.send(response)
    elif 'what harry potter character am i' in message.content.lower():
        word = random_line('harryCharacters.txt')
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
    elif 'what killer should i play' in message.content.lower():
        word = random_line('killersdbd.txt')
        response = word
        await message.channel.send(response)
    elif 'what survivor should i play' in message.content.lower():
        word = random_line('survivorsdbd.txt')
        response = word
        await message.channel.send(response)
    elif 'what killer perks should i pick' in message.content.lower():
        listOfPerks = randomPerks(killerPerks)
        response = "These perks: " + listOfPerks[0] + ", " + listOfPerks[1] + ", " + listOfPerks[2] + " and " + listOfPerks[3]
        await message.channel.send(response)
    elif 'what survivor perks should i pick' in message.content.lower():
        listOfPerks = randomPerks(survPerks)
        response = "These perks: " + listOfPerks[0] + ", " + listOfPerks[1] + ", " + listOfPerks[2] + " and " + listOfPerks[3]
        await message.channel.send(response)
    elif 'give me a random survivor perk' in message.content.lower():
        word = random_line('survivorperksNoNumb.txt')
        response = word
        await message.channel.send(response)
    elif 'give me a random killer perk' in message.content.lower():
        word = random_line('killerperksNoNumb.txt')
        response = word
        await message.channel.send(response)
    elif '?help' in message.content.lower():
        response = helpPage
        await message.channel.send(response)
    elif '?patch' in message.content.lower():
        response = patchPage
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException


client.run(TOKEN)
