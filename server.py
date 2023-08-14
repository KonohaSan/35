import socket
import math

def konchiwa():
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
 
 i = []
 ip = "192.168.1.32" #wiiu ip
 code = """#0E02FB40 3BC00000
#0E02FB50 2C030000
0E02FB40 3BC00001
0E02FB50 2C030001"""  #チートコード
 isKernel = True #カーネルならTrue違ったらFalse
 name = "フェス"
 about = "フェス開催"
 i = [ip,code,isKernel,name,about]
    #iを送信するプログラムを書く
 client_socket.send(i)
    #gecko.disableCodes(codeList)     #解除(コメント化されてる)
    
    # 接続を閉じる
 client_socket.close()


print('Server built')