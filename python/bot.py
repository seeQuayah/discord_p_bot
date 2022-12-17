import discord
from discord import app_commands
import random
import os


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

list_of_servers = [discord.Object(608763799192862733), discord.Object(781456077443170325), discord.Object(1020027394461007924)]
@tree.command(name = "boob", description = "boobs", guilds=list_of_servers) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def boob(interaction):
    afile = open("booburl.txt")
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    afile.close()
    await interaction.response.send_message(line)


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=608763799192862733))
    await tree.sync(guild=discord.Object(id=1020027394461007924))
    await tree.sync(guild=discord.Object(id=781456077443170325))
    print("Ready!")

#client.run(os.getenv("TOKEN"))
