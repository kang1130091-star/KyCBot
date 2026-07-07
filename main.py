import os
import discord
from discord.ext import commands

# 設定 Discord 機器人的意圖（Intents）
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
def on_ready():
    print("=================================")
    print(f"機器人已成功在 Railway 上線：{bot.user.name}")
    print("=================================")

@bot.command()
def ping(ctx):
    await ctx.send("Pong!")

# 從 Railway 的環境變數中安全地讀取 TOKEN
TOKEN = os.environ.get("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("錯誤：找不到 DISCORD_TOKEN 環境變數！")
