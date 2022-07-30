import discord
from discord.ext import commands
import discord.ext
import random
import requests
from decouple import config
import json

TOKEN = config("TOKEN")
APIKEY = config("APIKEY")

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
                f"Olá querido amigo(a), {name} :moyai: !"
            )
        if len(message.content) >= 40:
            await message.channel.send(
                f"Ei, {name} não é para spammar :triumph: !"
            )
    await bot.process_commands(message)

@bot.command(name="anime")
async def anime(ctx, *, q="anime"):
    listanimes = q.split(",")
    search = random.choice(listanimes)

    if q == "anime":
        await ctx.channel.send("Por favor, digite o que será sorteado.")
    else:
        r = requests.get("https://g.tenor.com/v1/random?q={}&key={}".format(search, APIKEY))
        data = r.json()
        gif = (data['results'][0]['media'][0]['gif']['url'])

        em = discord.Embed (
            title = f"O anime sorteado foi: {search}",
            color = ctx.author.color
        )

        em.set_image(url = gif)
        em.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
        em.set_footer(text = "Feito por " + bot.user.name)
        await ctx.channel.send(embed=em)

@bot.command(name="ajuda")
async def ajuda(ctx):
    url_image = "https://leosigh.com/wp-content/uploads/2022/02/Miko-Iino-adorable-as-always-Season-3-promo-visual-520x374.jpg"    

    em = discord.Embed (
        title = "Ajuda :heart: ", 
        description = 'Olá à todos! Eu sou a Miko Iino, onde a minha principal funcionalidade é sortear animes e outras coisas :laughing: .', 
        color = ctx.author.color
    )
    em.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
    em.set_footer(text = "Feito por " + bot.user.name)
    em.set_image (url = url_image)
    em.add_field(name = "Propriedades", value = "- diga um olá para mim! Basta digitar olá e me mencionar.\
        \n- anime: Sorteie qualquer anime, sendo da sua escolha e o resultado será mostrado com um GIF! :laughing: (A divisão do que será sorteado é através do uso da vírgula).\
        \n- aleatorio: Sorteie qualquer coisa sendo da sua escolha, sem GIF :frowning2: .(A divisão do que será sorteado é através do uso da vírgula).\
        \n- sorteio: Um anime aleatório será sorteado de uma lista com mais de 1200 animes.", inline = False)
    await ctx.channel.send(embed=em) 

@bot.command(name="aleatorio")
async def aleatorio(ctx, *, q="anime"):
    listaleatorio = q.split(",")
    search = random.choice(listaleatorio)

    if q == "anime":
        await ctx.channel.send("Por favor, digite o que será sorteado.")
    else:
        em = discord.Embed (
            title = (f"O sorteado foi: {search} "),
            color = ctx.author.color
        )
        em.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
        await ctx.send(embed=em)

@bot.command(name="sorteio")
async def sorteio(ctx):
    animes = random.choice(open("animes.txt","r").readlines())

    em = discord.Embed (
        title = f'O anime sorteado foi: {animes}',
        color = ctx.author.color
    )

    await ctx.channel.send(embed=em)

bot.run(TOKEN)