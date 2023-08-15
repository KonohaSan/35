import discord
import server
import socket
import math

TOKEN = 'MTE0MDMxMDQ5NDIwMTI0OTgxNA.GaygYb.GtiDdzWTx5VzA8xA_5cM5ohtvtUXbvtkLObdgM' # TOKENを貼り付け

client = discord.Client(intents=discord.Intents.all())

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content.startswith('!wiiu'):
        # Extract the IP address from the command
        ip_address = message.content.split(' ')[1]
        await message.channel.send('IPアドレスを受け付けました。')
        return ip_address 


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)