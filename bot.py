import discord
from discord.ext import commands
import psutil
import time
from config import TOKEN


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)



# Bot hazır olduğunda çalışır
@bot.event
async def on_ready():
    print(f"Bot hazır: {bot.user}")

# !status komutu
@bot.command()
async def status(ctx):

    # Başlangıç zamanı
    start = time.time()

    # CPU bilgileri
    logical = psutil.cpu_count(True)
    physical = psutil.cpu_count(False)

    # Sistem kullanımı
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent

    # Bitiş zamanı
    end = time.time()

    # Mesaj gönder
    await ctx.send(
        f"🖥️ Mantıksal CPU: {logical}\n"
        f"🧠 Fiziksel CPU: {physical}\n"
        f"⚡ CPU Kullanımı: {cpu_usage}%\n"
        f"💾 RAM Kullanımı: {ram_usage}%\n"
        f"⏱️ Süre: {round(end - start, 4)} saniye"
    )

# Botu başlat
bot.run(TOKEN)