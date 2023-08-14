import discord
import socket
import math

TOKEN = 'MTE0MDMxMDQ5NDIwMTI0OTgxNA.GaygYb.GtiDdzWTx5VzA8xA_5cM5ohtvtUXbvtkLObdgM' # TOKENを貼り付け

client = discord.Client(intents=discord.Intents.all())

# ホストのIPアドレスとポート番号
host_ip = '0.0.0.0'  # すべてのインターフェースで待ち受け
host_port = 46490

def send_data_to_ip(client_socket, ip_address):
    client_socket.send(ip_address.encode('utf-8'))
    # クライアントにデータを送信
    data_to_send = """30000000 106E46E8
10000000 4DF9FFFE
31000000 00000080
00120000 00000003
D0000000 DEADCAFE"""
    client_socket.send(data_to_send.encode('utf-8'))

@client.event
async def on_message(message):
    if message.content.startswith('!wiiu'):
        # Extract the IP address from the command
        ip_address = message.content.split(' ')[1]
        await message.channel.send('IPアドレスを受け付けました。')
        
        # Send the data to the client with the extracted IP address
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((ip_address, host_port))
            send_data_to_ip(client_socket, ip_address)

print('Server built')
client.run(TOKEN)