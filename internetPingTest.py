from time import sleep
import speedtest
import csv
import datetime

agora = datetime.datetime.now()
data = str(agora.day) + '/' + str(agora.month) + '/' + str(agora.year)
hora = str(agora.hour) + ':' + str(agora.minute) + ':' + str(agora.second)

st = speedtest.Speedtest()
st.best
ping = st.results.ping


#Data hora #hora #download #upload #ping
novaLinha = [data, hora, ping]
print (novaLinha)
with open('internetPingTest.csv', 'w') as arquivo_csv:
    escrever = csv.writer(arquivo_csv, delimiter=';', lineterminator='\n')
    escrever.writerow(novaLinha)