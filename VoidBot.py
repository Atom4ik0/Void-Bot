import time
from discord.utils import get
import io
import asyncio
import inspect
import io
import json
#import logging
#import os
import random
#import textwrap
#import traceback
#from contextlib import redirect_stdout
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import requests
#from PIL import Image, ImageFont, ImageDraw

url_list = ['https://tenor.com/view/oh-my-gif-25288613', 'https://tenor.com/view/bunny-floss-dancing-easter-bunny-dance-gif-14042343', 'https://tenor.com/view/mondays-lazy-dog-mood-monday-morning-gif-15086452', 'https://tenor.com/view/monday-relatable-gif-18690309', 'https://tenor.com/view/katze-cat-hasenohren-bunny-ears-gif-24097339']
cat_list = ['https://tenor.com/view/cat-cats-cat-love-cat-kiss-kiss-gif-24653113', 'https://tenor.com/view/cat-finger-gif-23872051', 'https://tenor.com/view/catjam-cat-dancing-cat-music-music-cat-cute-cat-gif-23392229', 'https://tenor.com/view/cute-kitty-best-kitty-alex-cute-pp-kitty-omg-yay-cute-kitty-munchkin-kitten-gif-15917800', 'https://tenor.com/view/kitty-review-kitty-cat-catto-cato-gif-22458047', 'https://tenor.com/view/kiss-cute-gif-23843199', 'https://tenor.com/view/cat-standing-fat-epic-gif-23115386', 'https://tenor.com/view/cat-smiling-smile-cat-orange-smile-cat-gif-23133359', 'https://tenor.com/view/cat-look-who-where-hole-gif-24745714', 'https://tenor.com/view/cat-cat-standing-cat-stare-stare-bruhcat-gif-22348277', 'https://tenor.com/view/cat-berg-cat-orange-cat-swimming-gif-25177582', 'https://tenor.com/view/head-angry-bad-meercat-meerkat-gif-14805612', 'https://tenor.com/view/kittens-pet-lover-cat-love-gif-24138518', 'https://tenor.com/view/kitty-gif-25023528', 'https://tenor.com/view/cat-poor-gif-21795471', 'https://tenor.com/view/shaking-cat-murderous-intent-murder-gif-23855100', 'https://tenor.com/view/cat-watermelon-gif-24388589', 'https://tenor.com/view/sassy-cats-angry-mad-ok-gif-9934420', 'https://tenor.com/view/love-cat-love-cats-cat-cats-gif-24534809', 'https://tenor.com/view/cat-run-gif-24216099', 'https://tenor.com/view/cat-cats-cattitude-catitude-cat-master-gif-23322963', 'https://tenor.com/view/who-are-you-cat-cat-staring-confused-weird-gif-24607471', 'https://tenor.com/view/vat-cat-cats-kitty-dog-gif-20095217', 'https://tenor.com/view/cat-cats-corn-gif-24417734', 'https://tenor.com/view/cat-cats-mad-cat-cat-mad-cat-jealous-gif-23378592', 'https://tenor.com/view/cat-the-cat-he-dance-he-dance-gif-24077288', 'https://tenor.com/view/cat-angry-cat-angy-cat-cat-frown-angry-white-cat-gif-24362646',]
dog_list = ['https://tenor.com/view/dog-serious-gif-15276483', 'https://tenor.com/view/happy-happy-dog-dog-happiest-dog-super-happy-gif-17885812', 'https://tenor.com/view/dog-dancing-dirty-gif-24754370', 'https://tenor.com/view/dog-funny-dog-gif-24432896', 'https://tenor.com/view/xv-gif-23454283', 'https://tenor.com/view/fatdog-dog-funnydog-cute-dog-gif-19059877', 'https://tenor.com/view/puppy-gif-24443090', 'https://tenor.com/view/chill-bro-sorry-dog-hair-gif-16673678', 'https://tenor.com/view/what-the-dog-doin-gif-22356855', 'https://tenor.com/view/dog-wtf-gif-24726819', 'https://tenor.com/view/funny-animals-dog-dance-cute-smile-gif-12759384', 'https://tenor.com/view/swing-relaxing-chill-out-like-a-boss-funny-animals-gif-14520026', 'https://tenor.com/view/ok-okay-but-did-i-ask-did-i-ask-meme-gif-24280789', 'https://tenor.com/view/doggo-dog-pretty-lady-gif-14796558', 'https://tenor.com/view/fun-pet-pet-fun-drive-dog-dog-drive-dog-driving-gif-24512001', 'https://tenor.com/view/help-dog-funy-old-granny-gif-15626700', 'https://tenor.com/view/fknbnuy-funny-dog-waiting-patient-gif-21698298', 'https://tenor.com/view/please-pretty-please-cutie-cute-dog-gif-21727236', 'https://tenor.com/view/funny-dog-scared-dog-omg-gif-18133934', 'https://tenor.com/view/pet-lover-wedding-funny-dog-gif-24924577', 'https://tenor.com/view/shiba-shiny-shiba-doggo-good-doggo-shiny-doggo-gif-16082089']
meme_list= ['https://tenor.com/view/hamster-meme-staring-hd-watching-gif-23055924', 'https://tenor.com/view/sus-gif-24048467', 'https://tenor.com/view/the-wok-the-rock-the-rock-sus-the-rock-meme-the-rock-eyebrows-gif-23750956', 'https://tenor.com/view/the-rock-eyebrow-the-rock-eyebrow-the-rock-eyebrow-meme-eyebrow-meme-gif-23172374', 'https://tenor.com/view/monkey-call-phone-on-call-dialing-gif-16416201', 'https://tenor.com/view/cat-meme-funny-gif-5754572', 'https://tenor.com/view/kids-meme-stare-uhm-gif-16606126', 'https://tenor.com/view/dankjerry-tom-and-jerry-jerry-dank-gif-18715520', 'https://tenor.com/view/cristiano-ronaldo-drinking-meme-ronaldo-gif-23698102', 'https://tenor.com/view/smiling-cat-creepy-cat-cat-zoom-kitty-gif-12199043', 'https://tenor.com/view/memes-bone-skull-skeleton-dancing-gif-17871793', 'https://tenor.com/view/memes-bone-skull-skeleton-dancing-gif-17871793', 'https://tenor.com/view/what-meme-where-huh-gif-17244725', 'https://tenor.com/view/spongebob-nickelodeon-handsome-squidward-funny-meme-gif-14625359', 'https://tenor.com/view/cry-man-bald-meme-gif-15655066', 'https://tenor.com/view/memes-dank-memes-meme-gif-13108012', 'https://tenor.com/view/distorted-cat-meme-distortion-cat-black-cat-meme-gif-14670421', 'https://tenor.com/view/dance-fun-animals-dog-frog-gif-22154297', 'https://tenor.com/view/peppa-pig-pig-dancing-jamming-vibing-gif-22084798', 'https://tenor.com/view/memes-images-gif-19999248', 'https://tenor.com/view/confused-john-travolta-gif-25105508', 'https://tenor.com/view/meme-anime-manga-blend-s-smile-gif-15245379', 'https://tenor.com/view/credit-card-damn-what-is-that-damn-give-me-now-gif-21156291']
rust_list = ['https://tenor.com/view/rust-dance-flex-gif-22407373', 'https://tenor.com/view/flavortown-rust-naked-bow-jack-black-gif-21774222', 'https://tenor.com/view/rust-emotes-rust-play-rust-rust-pvp-video-game-gif-15703741', 'https://tenor.com/view/rust-creepy-spotted-gif-15406101', 'https://tenor.com/view/eoka-beamed-roblox-eoka-gang-rust-gif-21533744', 'https://tenor.com/view/rust-west-gif-18061638', 'https://tenor.com/view/rust-dancing-rust-dancing-liluzium-gif-22100198', 'https://tenor.com/view/rust-facepunch-studios-multiplayer-online-video-game-gif-20269767', 'https://tenor.com/view/rust-dance-dlc-rust-dance-naked-dance-gif-22208491', 'https://tenor.com/view/caveree-ree-rust-cave-laughing-gif-17047401', 'https://tenor.com/view/rust-masuz-keeneri-fire-gif-15667756', 'https://tenor.com/view/rust-waving-rust-waving-creators-hangouts-gif-20433479', 'https://tenor.com/view/rust-playrust-cactus-random-funny-gif-20308390', 'https://tenor.com/view/rust-wave-gif-21846889', 'https://tenor.com/view/rust-playrust-rust-video-game-saltytaco-yrnrust-gif-14459757', 'https://tenor.com/view/rust-gif-20823297', 'https://tenor.com/view/rust-zerg-army-enardo-stream-gif-14732949', 'https://tenor.com/view/rust-boy-gif-21974302', ]

TOKEN = "Token"

PREFIX = '>'

intents = discord.Intents().all()
bot = commands.Bot(PREFIX, intents=intents)
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print("Я запущен!")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('>help || Void.bot'))

@bot.event
async def on_command_error(ctx, error):
    pass

@bot.command()
async def Hi(ctx):
    await ctx.send("Hi")

@bot.command()
async def test1(ctx):
    embed = discord.Embed(
    title="Правила"
)
    await ctx.send(embed=embed)

@bot.command()
async def test2(ctx):
    embed = discord.Embed(
        title="Кнопка",
        description="Текст",
        url='https://www.youtube.com/channel/UC-_7dP7jQPZK_7yv4ZnmYTQ/videos',
    )
    await ctx.send(embed=embed)

@bot.command()
async def Foto(ctx):
    await ctx.send(random.choice(url_list))

@bot.command()
async def cat(ctx):
    await ctx.send(random.choice(cat_list))

@bot.command()
async def dog(ctx):
    await ctx.send(random.choice(dog_list))

@bot.command( pass_context = True)
@commands.has_permissions( administrator = True)
async def clear( ctx, amout : int ):
    await ctx.channel.purge( limit = amout)

@bot.command( pass_context = True)
@commands.has_permissions( administrator = True)
async def kick( ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge( limit = 1)

    await member.kick( reason = reason )
    await ctx.send( f'kick user { member.mention }')

@bot.command( pass_context = True)
@commands.has_permissions( administrator = True)
async def ban( ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit = 1)

    await member.ban( reason = reason )
    await ctx.send( f'ban user { member.mention }')

@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        title='Bot Latency',
        description=f'  My ping is {bot.latency} s !',
        color=discord.Colour.blue()
    )
    embed.set_footer(text='Void Bot')
    await ctx.send(embed=embed)

@bot.command()
async def meme(ctx):
    await ctx.send(random.choice(meme_list))

@bot.command()
async def send( ctx ):
    await ctx.author.send( 'Hello World!' )

@bot.command()
async def hello( ctx, member: discord.Member):
    await member.send( f'{member.name}, привіт від { ctx.author.name }')

@bot.command()
async def rust(ctx):
    await ctx.send(random.choice(rust_list))

@bot.command()
async def flipcoin(ctx):
	heads_tails = ['Орел', 'Решка']
	choice = random.choice(heads_tails)
	await ctx.send(choice)

@bot.command()
async def rand(ctx):
    number = random.randint(1, 1000)
    await ctx.send(str(number))

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='Навигация по командам')

    embed.set_footer(text='Void bot')
    embed.add_field( name = '📷 Image', value = '`>cat` `>dog` `>meme` `>rust`', inline = False)
    embed.add_field( name = '🔨 Admin', value = '`>clear` `>ban` `>kick`', inline = False)
    embed.add_field( name = 'ℹ Info', value = '`>help` `>ping`', inline = False)
    embed.add_field( name = '🎉 Fun', value = '`>hello` `>send` `>rand` `>flipcoin`', inline = False)
    embed.set_thumbnail(
        url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnT0F9xwqfAq_7QaSndEXbSi7X4a4gz_9ihjTiEQhYx6u9xoV0QYepAuvWfC4pRTRqhls&usqp=CAU')
    embed.set_author(name='Void',
        icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnT0F9xwqfAq_7QaSndEXbSi7X4a4gz_9ihjTiEQhYx6u9xoV0QYepAuvWfC4pRTRqhls&usqp=CAU')

    await ctx.send(embed=embed)

bot.run(TOKEN)
