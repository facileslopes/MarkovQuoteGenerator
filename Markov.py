import random
fileloc = "/Users/donti/Desktop/Programming/Incomplete Projects/Quote Generator/Markov/data.txt"
data = (open(fileloc)).read()    
dataset = data.split(' ')
newset = []
for word in dataset:
    n = dataset.index(word)
    if '\n' in word:
        newset.append(word[1:])
    elif '.' in word:
        newset.append(word[:-1])
        newset.append('.')
    else:
        newset.append(word)
def filter_func(x):
    if x == ' ':
        return False
    else:
        return True
dataset = list(filter(filter_func,newset))
chain = {}
for x in range(0,len(dataset) - 1):
    word = dataset[x]
    if word not in chain:
        chain[word] = [dataset[x+1]]
        if word[0].isupper():
            if '.' not in chain:
                chain['.'] = [word]
            else:
                if word not in chain['.']:
                    chain['.'].append(word)
    else:
        if dataset[x+1] not in chain[word]:
            chain[word].append(dataset[x+1])
length = int(input('How long do you want your quote to be?(in sentences)'))
rand_word = '.'
n = 0
quote = ''
while n < length:
    pickfrom = chain[rand_word]
    rand_word = random.choice(pickfrom)
    quote = quote + rand_word + ' '
    if rand_word == '.':
        n += 1
print(quote)
