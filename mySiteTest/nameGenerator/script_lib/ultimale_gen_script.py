import csv, random, os

def build_markov_chain(data, n):
    chain = {
        '_initial':{},
        '_names': set(data)
    }
    for word in data:
        word_wrapped = str(word) + '.'
        for i in range(0, len(word_wrapped) - n):
            tuple = word_wrapped[i:i + n]
            next = word_wrapped[i + 1:i + n + 1]
            
            if tuple not in chain:
                entry = chain[tuple] = {}
            else:
                entry = chain[tuple]
            
            if i == 0:
                if tuple not in chain['_initial']:
                    chain['_initial'][tuple] = 1
                else:
                    chain['_initial'][tuple] += 1
                    
            if next not in entry:
                entry[next] = 1
            else:
                entry[next] += 1
    return chain

def select_random_item(items):
    rnd = random.random() * sum(items.values())
    for item in items:
        rnd -= items[item]
        if rnd < 0:
            return item

def generate(chain):
    tuple = select_random_item(chain['_initial'])
    result = [tuple]
    
    while True:
        tuple = select_random_item(chain[tuple])
        last_character = tuple[-1]
        if last_character == '.':
            break
        result.append(last_character)
    
    generated = ''.join(result)
    if generated not in chain['_names']:
        return generated
    else:
        return generate(chain)

def from_existing(num,vocabulary):
    #print('!*** ESTRAZIONE DA PREESISTENTI ***!\n')
    #User driven name selection
    #num = input('Quanti nomi vuoi estrarre?:\n
    #print('<><><><><><><><><><><><><><><><><><>')
    
    #Male or female selection
    #vocabulary = input('Qual è il tipo dei nomi?: M/F/B\n')
    #print('<><><><><><><><><><><><><><><><><><>')

    #Open csv file
    names = fetch_names(vocabulary)
    namelist=random.sample(names,num)
    #print('<><><><><><><><><><><><><><><><><><>')
    return namelist

def fetch_names(vocabulary):

    filename = os.getcwd() + "/nameGenerator/script_lib"
    
    #Dataset from vocabulary selection
    if vocabulary == 'M':
        filename += '/m_names.csv'
    elif vocabulary == 'F':
    	filename += '/f_names.csv'
    elif vocabulary == 'B':
        filename += '/c_names.csv'


    #Open csv file
    namelist = []
    with open(filename) as names:
        csv_reader = csv.reader(names, delimiter=',')
        line_count=0
        for row in csv_reader:
            if line_count == 0:
                
                line_count += 1
            else:
                namelist.append(row[0])
                line_count += 1
    return namelist

    
def markov_generation(num,vocabulary):

    #print('!*** GENERAZIONE MARKOV ***!\n\nQual è il genere dei nomi?: M/F/B/MILAN\n')
    #os.system('ls -a')
    namelist = fetch_names(vocabulary)
    #print('<><><><><><><><><><><><><><><><><><>')
    #num = input('Quanti nomi vuoi generare?:\n')
    #num = int(num)
    
    #print('<><><><><><><><><><><><><><><><><><>')
    
    chain = build_markov_chain(namelist,3)
    markov_names = []
    for i in range(num):
    	markov_names.append(generate(chain))
    
    #for m in markov_names:
    #	print('·'+m)
    #print('<><><><><><><><><><><><><><><><><><>')
    return markov_names

def main(fun,num,vocabulary):
    #print('Benvenuto in SARDINIAN NAME GENERATOR!\n')
    namelist = []
    if fun == '1':
        namelist = from_existing(num,vocabulary)
    elif fun == '2':
        namelist = markov_generation(num,vocabulary)
    else:
        print('Arigato gozaimashita, weeb')
    return namelist

#####
#MARKOV MODEL RESOURCES
#https://towardsdatascience.com/generating-startup-names-with-markov-chains-2a33030a4ac0
#####
