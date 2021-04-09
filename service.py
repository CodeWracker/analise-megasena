import requests
import json
import csv
from bokeh.plotting import figure, output_file, show
import os
from secrets import TOKEN
from tqdm import tqdm

def verificaAcertos():
    jogo = []
    print("Insira suas dezenas")
    for i in range(0,6):
        jogo.append(int(input()))
    data = localFetch()
    result = []
    for row in data:
        acertos = 0
        linha = stringListToIntList(row['dezenas'])
        #print(linha)
        for dez in jogo:
            if(dez in linha):
                acertos+=1
        #print(acertos)
        if(acertos>=4):
            result.append({
                "Jogo": row["numero"],
                "Acertos": acertos
            })
    print(result)
    
def stringListToIntList(list):
    valores = []
    for val in list:
        valores.append(int(val))
    return valores

def apiFetch():
    primeiro = int(input("Qual o numero do primeiro jogo: "))
    ultimo =int( input("Qual o numero do ultimo jogo: "))
    print("Buscando os resultados do jogo " + str(primeiro) + " ao " + str(ultimo) )
    resultados = []
    for i in tqdm(range(primeiro, ultimo+1)):
        #print("Jogo "+ str(i))
        r = requests.get("https://apiloterias.com.br/app/resultado?loteria=megasena&token="+TOKEN+"&concurso=" + str(i),timeout=None)
        try:
            resp = json.loads(r.content)
            resultados.append({
            "dezenas": resp["dezenas"],
            "numero" : resp["numero_concurso"]
        })
        except:
            print("ERRO!")
            print(r) 
            print(r.status_code)
            print(r.headers) 
            print("-----------------")
        #print(resp["dezenas"])
        #print(resp["numero_concurso"])
        
        print()
    #print(resultados[0])
    saveData(resultados,primeiro, ultimo)
    precessedData = processData(resultados)
    plotData(precessedData)

def analiseLocal():
    precessedData = processData(localFetch())
    plotData(precessedData)

def localFetch():
    files = []
    path = 'data'
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    print("Arquivos disponíveis (inicio-fim)")
    i = 0
    for file in files:
        print(str(i) + " - " + file)
        i+=1
    esc = int(input("Escolha: "))

    data = []
    with open('data/'+files[esc],'r') as f:
        reader = csv.reader(f)
        for row in reader:
            aux = {
                "numero" : row.pop(0),
                "dezenas": row
            }
            data.append(aux)
    return data


def saveData(results,primeiro, ultimo):
    print("Salvando dados")
    data = []
    for res in results:
        aux = []
        aux.append(res["numero"])
        for dez in res["dezenas"]:
            aux.append(dez)
        data.append(aux)
    #print(data)
    with open('data/'+str(primeiro)+'-'+str(ultimo)+'.csv', 'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
        f.close()

def processData(results):
    data = []
    for i in range(1,61):
        data.append(0)
    
    for res in results:
        for dez in res['dezenas']:
            data[int(dez)-1] +=1
    #print(data)
    return data

def plotData(data):
    x = []
    for i in range(1,61):
        x.append(i)
    
    output_file('output/index.html')

    p = figure(
        plot_width=600, plot_height=600
    )

    p.vbar(x=x,width=1,bottom=0, top=data,fill_alpha=1.0, fill_color='gray', hatch_alpha=1.0, hatch_color='black', hatch_extra={}, hatch_pattern=None, hatch_scale=12.0, hatch_weight=1.0, line_alpha=1.0, line_cap='butt', line_color='black', line_dash=[], line_dash_offset=0, line_join='bevel', line_width=1)
    show(p)


