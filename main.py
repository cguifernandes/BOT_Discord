import discord
from decouple import config
from discord.ext import commands
import random
import giphy_client

bot = commands.Bot(command_prefix = "<")
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"Estou pronto! {bot.user}")

@bot.event
async def on_message(message):
    name = message.author.mention
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        if "OLÁ".lower() in message.content.lower() or "OLA".lower() in message.content.lower():
            await message.channel.send(
                f"Olá querido amigo, {name} :moyai: !"
            )
        if len(message.content) >= 30:
            await message.channel.send(
                f"Ei, {name} não é para spammar :triumph: !"
            )
    await bot.process_commands(message)

@bot.command(name="anime")
async def anime(ctx, *, q):
    APIKEY = config("APIKEY")
    listanimes = q.split(",")
    search = random.choice(listanimes)
    api_instace = giphy_client.DefaultApi()

    api_responce = api_instace.gifs_search_get(APIKEY, search, limit=5)
    lst = list(api_responce.data)
    giff = random.choice(lst)

    em = discord.Embed (
        title = f"O anime escolhido foi: {search}",
        color = ctx.author.color
    )
    em.set_image(url = f"https://media.giphy.com/media/{giff.id}/giphy.gif")
    em.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    em.set_footer(text="Feito por " + bot.user.name)
    await ctx.channel.send(embed=em) 

@bot.command(name="character")
async def anime(ctx, *, q):
    APIKEY = config("APIKEY")
    listanimes = q.split(",")
    search = random.choice(listanimes)
    api_instace = giphy_client.DefaultApi()

    api_responce = api_instace.gifs_search_get(APIKEY, search, limit=5)
    lst = list(api_responce.data)
    giff = random.choice(lst)

    em = discord.Embed (
        title = f"O anime escolhido foi: {search}",
        color = ctx.author.color
    )
    em.set_image(url = f"https://media.giphy.com/media/{giff.id}/giphy.gif")
    em.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    em.set_footer(text="Feito por " + bot.user.name)
    await ctx.channel.send(embed=em)

@bot.command(name="ajuda")
async def help(ctx):
    url_image = "https://preview.redd.it/ngnenrma5i191.png?auto=webp&s=2d700f306dda3d85e5821d3be0da5558bec40728"    

    em = discord.Embed (
        title = "Ajuda :heart: ", 
        description = 'Escrava no chat com "Olá" para que assim, o bot responda! \n oi', 
        color = ctx.author.color, 
    )
    em.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    em.set_footer(text="Feito por " + bot.user.name)
    em.set_thumbnail (url=url_image)

    await ctx.send(embed=em)

TOKEN = config("TOKEN")
bot.run(TOKEN)

