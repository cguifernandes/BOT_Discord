import discord
from decouple import config
from discord.ext import commands

bot = commands.Bot(command_prefix = "<")
bot.remove_command("help")

#event

@bot.event
async def on_ready():
    print(f"Estou pronto! {bot.user}")

#Ola

@bot.event
async def on_message(message):
    name = message.author.mention
    if message.author == bot.user:
        return

    if "OLÁ".lower() in message.content.lower() or "OLA".lower() in message.content.lower():
        await message.channel.send(
            f"Olá querido amigo, {name} :moyai: "
        )
    await bot.process_commands(message)

#ajuda

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

#run do bot
TOKEN = config("TOKEN")

bot.run(TOKEN)

