import discord
from discord.ext import commands

from residuos import residuos


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.command()
async def reciclar(ctx, *, objeto):

    objeto = objeto.lower()

    if objeto in residuos:

        informacion = residuos[objeto]

        await ctx.send(
            f"{informacion['emoji']} **{objeto.title()}**\n"
            f"Categoría: **{informacion['categoria'].title()}**\n"
            f"💡 {informacion['mensaje']}"
        )

    else:

        await ctx.send(
            f"❓ No conozco el residuo **{objeto}**.\n"
            "Puedes intentar con otro objeto."
        )


bot.run("el token va aqui")
