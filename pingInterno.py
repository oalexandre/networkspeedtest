from time import sleep
from pythonping import ping
import speedtest
import csv
import datetime


for

agora = datetime.datetime.now()
data = str(agora.day) + '/' + str(agora.month) + '/' + str(agora.year)
hora = str(agora.hour) + ':' + str(agora.minute) + ':' + str(agora.second)


response_list = ping('192.168.0.1')
roteadorWifi = response_list.rtt_avg_ms

response_list = ping('192.168.2.1')
modemUnifique = response_list.rtt_avg_ms

response_list = ping('8.8.8.8')
dnsGoogle = response_list.rtt_avg_ms

response_list = ping('google.com')
siteGoogle = response_list.rtt_avg_ms

esponse_list = ping('g1.com.br')
siteG1 = response_list.rtt_avg_ms

esponse_list = ping('lohasstore.com.br')
siteLohas = response_list.rtt_avg_ms


#Data hora #hora #download #upload #ping
novaLinha = [data, hora, roteadorWifi, modemUnifique, dnsGoogle, siteGoogle, siteG1, siteLohas]
print (novaLinha)
with open('pingInterno.csv', 'w') as arquivo_csv:
    escrever = csv.writer(arquivo_csv, delimiter=';', lineterminator='\n')
    escrever.writerow(novaLinha)