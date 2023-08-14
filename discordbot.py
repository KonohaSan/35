import discord
import socket
import math

TOKEN = 'MTE0MDMxMDQ5NDIwMTI0OTgxNA.GaygYb.GtiDdzWTx5VzA8xA_5cM5ohtvtUXbvtkLObdgM' # TOKENを貼り付け

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('logged in')

@client.event
async def on_message(message):
    if message.content.startswith('!wiiu'):
        # Extract the IP address from the command
        ip_address = message.content.split(' ')[1]
        await message.channel.send('IPアドレスを受け付けました。')
        # Send the data to the client with the extracted IP address
        send_data_to_ip(ip_address)

@client.event
async def on_ready():
    
       # ホストのIPアドレスとポート番号
        host_ip = '0.0.0.0'  # すべてのインターフェースで待ち受け
        host_port = 46490

        # サーバーソケットを作成
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host_ip, host_port))
        server_socket.listen(50)  # 最大50つの接続を待ち受け

        print('Server built')

# Function to send data to a specified IP address
def send_data_to_ip(ip_address):
    try:
        # Create a client socket and connect to the specified IP address
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Send the IP address as bytes
        client_socket.send(ip_address.encode('utf-8'))

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while True:
            # クライアントからの接続を待ち受け
            client_socket, client_address = server_socket.accept()
            print('client accessed IP:', client_address[0], 'port:', client_address[1])
    # クライアントにデータを送信
            data_to_send = """09020000 13862EF0
00002000 00000000
30000000 106E46E8
10000000 50000000
001200C4 00000000
001201CC 00000000
001201D0 00000000
001201EC 00000000
001201F0 00000000
00120348 50800000
0012049C 00000000
001204A0 00000000
001204A4 00000000
001204A8 00000000
001204AC 00000000
001204C0 40800000
001205BC 00000000
001205C0 00000000
001205C4 00000000
001205D0 00000000
001205D4 00000000
001205D8 00000000
001205DC 00000000
001205E0 00000000
001205E4 00000000
00120664 00000000
00120668 00000000
D0000000 DEADCAFE
00020000 105EBE40
3F000000 00000000
00020000 105EBFF0
3DCCCCCD 00000000
00020000 105EC2E4
3F933333 00000000
09020000 102F48A8
00002000 00000000
00020000 105EBE40
3F100000 00000000
00020000 105EBFF0
3ECCCCCD 00000000
00020000 105EC2E4
3F633333 00000000
D0000000 DEADCAFE
30000000 106E46E8
10000000 50000000
0012035C 00000000
00120360 00000000
00120364 00000000
00120898 00000000
0012089C 00000000
001208A0 00000000
D0000000 DEADCAFE"""
        client_socket.send(data_to_send.encode('utf-8'))

        # Close the client socket
        client_socket.close()
        print(f'IPに送信されるデータ:: {ip_address}')
    except Exception as e:
        print(f'IPへのデータ送信エラー: {ip_address}, Error: {str(e)}')

client.run(TOKEN)