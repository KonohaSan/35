import discord
import socket
import math

TOKEN = 'MTE0MDMxMDQ5NDIwMTI0OTgxNA.GaygYb.GtiDdzWTx5VzA8xA_5cM5ohtvtUXbvtkLObdgM' # TOKENを貼り付け

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('ログインしました')

# -*- coding : UTF-8 -*-

@client.event
async def on_ready():
    print('TCPサーバー接続')
# ホスト鯖のIPアドレスとポート番号
host_ip = "	118.27.16.228"
port = 46490

# ソケットの作成
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ソケットのバインド
server_socket.bind((host_ip, port))

# 接続の待機
server_socket.listen(1)
print("ゲスト鯖からの接続を待機中...")

# 接続の受け入れ
guest_socket, guest_address = server_socket.accept()
print("ゲスト鯖と接続されました。")

# ゲスト鯖からのデータを受信
data = guest_socket.recv(1024)

# データの処理（WiiUへの送信など）
# ...

# ソケットを閉じる
guest_socket.close()
server_socket.close()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!connect'):
        # コマンドの引数を取得
        args = message.content.split()
        ip = args[1] #ipアドレス
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,7331))
        self = """09020000 13862EF0
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
D0000000 DEADCAFE""".replace(" ","").replace("\n","") #カフェコードから空白と改行を削除

        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,7331))
        s.send(bytes.fromhex('03'))
        s.send(bytes.fromhex('10014CFC00000000'))
        for x in range(math.floor(len(self)/8)):
            s.send(bytes.fromhex('03'))
            s.send(bytes.fromhex('0'+format(0x01133000+x*4,'X')+self[x*8:x*8+8]))
        s.send(bytes.fromhex('03'))
        s.send(bytes.fromhex('10014CFC00000001'))

client.run(TOKEN)