import socket
import math
import pickle

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

     ip = on_message(message) #wiiu ip
     code = """#0E02FB40 3BC00000
#0E02FB50 2C030000
0E02FB40 3BC00001
0E02FB50 2C030001"""  #チートコード
     isKernel = True #カーネルならTrue違ったらFalse
     name = "フェス"
     about = "フェス開催"

     data = {"ip":ip, "code":code, "isKernel":isKernel, "name":name, "about":about}
     import io
     file = io.BytesIO()
     pickle.dump(data,file)
     data = pickle.dumps(data)

     client_socket.send(data)

     print('Server built')