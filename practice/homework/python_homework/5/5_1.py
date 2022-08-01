def rotten(fruit):
    fruit_lower = fruit.lower()
    fruit_split = fruit_lower.split(',')
    
    for i in range(len(fruit_split)):
        fruit_split[i] = fruit_split[i].replace('rotten','')
    return(fruit_split)


print(rotten('apple,banana,rottenOrange,Orange'))
