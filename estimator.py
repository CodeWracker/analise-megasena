from service import *
from tqdm.auto import tqdm
def verificaCombinacoes():
    print("Iniciando analise")
    data = localFetch()
    verifica(data)

def verifica(data):
    freqComb = {
        "quatro":[
            {"jogo" : [],
            "freq" : 0}
        ],
        "cinco":[
            {"jogo" : [],
            "freq" : 0 }
        ],
        "seis":[
            {"jogo" : [],
            "freq" : 0}
        ]
    }
    for row in tqdm(data):
        print(" ",end='\r')
        for i in range(0,6): 
            for j in range(i+1,6):
                aux = []
                #print(str(i) + " "+str(j))
                for k in range(0,6):
                    
                    if(k!=i and k!=j):
                        aux.append(row['dezenas'][k])
                aux.append(0)
                aux.append(0)
                aux =stringListToIntList(aux)
                #print(aux)
                freqComb = verificaInclusaoNoHistorico(data,aux,freqComb,'quatro')
    
    for row in tqdm(data):
        print(" ",end='\r')
        for i in range(0,6): 
            aux = []
            #print(str(i) + " "+str(j))
            for k in range(0,6):
                
                if(k!=i):
                    aux.append(row['dezenas'][k])
            aux.append(0)
            aux =stringListToIntList(aux)
            #print(aux)
            freqComb = verificaInclusaoNoHistorico(data,aux,freqComb,'cinco')
    
    for row in tqdm(data):
        print(" ",end='\r')
        aux = []
        #print(str(i) + " "+str(j))
    
        aux =stringListToIntList(row['dezenas'])
        #print(aux)
        freqComb = verificaInclusaoNoHistorico(data,aux,freqComb,'seis')
    print(freqComb)

def verificaInclusaoNoHistorico(data,jogo,freqComb,ganho):
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
    #print(result)
    if(result != []):
        if(len(result)>=freqComb[ganho][0]['freq']):
            comb = {
                "jogo": jogo,
                "freq" : len(result)
            }
            if(len(result)!=freqComb[ganho][0]['freq']):
                freqComb[ganho] = []
            
            if comb not in freqComb[ganho]:
                freqComb[ganho].append(comb)
    return freqComb
