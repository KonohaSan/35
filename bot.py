import discord
import server
import socket
import math

TOKEN = 'MTE0MDMxMDQ5NDIwMTI0OTgxNA.GaygYb.GtiDdzWTx5VzA8xA_5cM5ohtvtUXbvtkLObdgM' # TOKEN��\��t��

client = discord.Client(intents=discord.Intents.all())

# �N�����ɓ��삷�鏈��
@client.event
async def on_ready():
    # �N��������^�[�~�i���Ƀ��O�C���ʒm���\�������
    print('���O�C�����܂���')

@client.event
async def on_message(message):
    if message.content.startswith('!wiiu'):
        # Extract the IP address from the command
        ip_address = message.content.split(' ')[1]
        await message.channel.send('IP�A�h���X���󂯕t���܂����B')
        return ip_address 


# Bot�̋N����Discord�T�[�o�[�ւ̐ڑ�
client.run(TOKEN)