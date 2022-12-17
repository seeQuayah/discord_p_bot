import discord
from discord import app_commands
import random
import os
import mysql.connector as mariadb
from dotenv import load_dotenv

load_dotenv() 

def connect_db():
        connection = mariadb.connect(
            user="jc",
            password="password_database",
            host="mariadb",
            port=3306,
            database="discord_p"
        )
        return connection, connection.cursor()

connect, cursor = connect_db()


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

list_of_servers = [discord.Object(608763799192862733), discord.Object(781456077443170325), discord.Object(1020027394461007924)]
@tree.command(name = "boob", description = "boobs", guilds=list_of_servers) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def boob(interaction):
    cursor.execute("SELECT * from natural_tits ORDER BY RAND() LIMIT 1;")
    rand_select = cursor.fetchone()
    await interaction.response.send_message("%s" % (rand_select[2]))

@tree.command(name = "ass", description = "ass", guilds=list_of_servers) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def boob(interaction):
    cursor.execute("SELECT * from ass ORDER BY RAND() LIMIT 1;")
    rand_select = cursor.fetchone()
    await interaction.response.send_message("%s" % (rand_select[2]))

@tree.command(name = "thread_ass", description = "thread ass", guilds=list_of_servers) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def boob(interaction):
    cursor.execute("SELECT * from ass ORDER BY RAND() LIMIT 1;")
    rand_select = cursor.fetchone()
    await interaction.response.send_message("%s" % (rand_select[1]))

@tree.command(name = "thread_boob", description = "thread boob", guilds=list_of_servers) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def boob(interaction):
    cursor.execute("SELECT * from boobs ORDER BY RAND() LIMIT 1;")
    rand_select = cursor.fetchone()
    await interaction.response.send_message("%s" % (rand_select[1]))


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=608763799192862733))
    await tree.sync(guild=discord.Object(id=1020027394461007924))
    await tree.sync(guild=discord.Object(id=781456077443170325))
    print("Ready!")

client.run(str(os.getenv("TOKEN")))
