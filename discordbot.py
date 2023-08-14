import discord
import socket
import math

TOKEN = 'あ' # TOKENを貼り付け

client = discord.Client(intents=discord.Intents.all())

# ホストのIPアドレスとポート番号
host_ip = '0.0.0.0'  # すべてのインターフェースで待ち受け
host_port = 46490

# サーバーソケットを作成
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host_ip, host_port))
server_socket.listen(50)  # 最大50つの接続を待ち受け

print('サーバーが起動しました。')

while True:
    # クライアントからの接続を待ち受け
    client_socket, client_address = server_socket.accept()
    print('クライアントが接続しました。IP:', client_address[0], 'ポート:', client_address[1])

    # クライアントにデータを送信
    data_to_send = """30000000 106E46E8
10000000 4DF9FFFE
31000000 00000080
00120000 00000003
D0000000 DEADCAFE"""
    client_socket.send(data_to_send.encode('utf-8'))
    
    # 接続を閉じる
    client_socket.close()

@client.event
async def on_message(message):
    if message.content.startswith('!wiiu'):
        # Extract the IP address from the command
        ip_address = message.content.split(' ')[1]
        await message.channel.send('IPアドレスを受け付けました。')
        
        # Send the data to the client with the extracted IP address
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.send(ip_address.encode('utf-8'))

print('Server built')
client.run(TOKEN)
