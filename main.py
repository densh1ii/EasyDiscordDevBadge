import discord
from discord.ext import commands
from discord import app_commands


Token = "YOUR TOKEN HERE"  # your discord bot token here (keep it secret)
Guild_ID = 1234566789900 #Please replace with ur Server/Guild Id


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('bot is ready')

    GUILD = discord.Object(id=Guild_ID)

    try:
        synced = await bot.tree.sync(guild=GUILD)
        print(f'synced {len(synced)} commands')
    except Exception as e:
        print(e)

@bot.tree.command(name="ping", description="Check if bot is alive")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong {interaction.user.mention}')

@bot.tree.command(name="get-badge", description="How to claim the Discord Active Developer Badge")
async def getBadge(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Perfect! Now all you need to do is wait (maybe up to 24 hours) then go to:\n"
        "https://discord.com/developers/active-developer\n"
        "If you can claim congrats! "
    )

bot.run(Token)
