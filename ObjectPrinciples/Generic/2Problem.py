from typing import List, Dict, Any


def find_mode(elements: List[Any]) -> List[Any]:
    # Write your code here
    diccionario = {}
    for i in elements:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    maximo = max(diccionario.values())
    elemMax= [i for i in diccionario if diccionario[i] == maximo]
    return elemMax[0]
    

elements1 = [1, 2, 3, 4, 2, 5, 2, 6, 7, 8, 2]
elements2 = ['a', 'b', 'c', 'b', 'c', 'c', 'c', 'e', 'c', 'c', 'd', 'e', 'c']
print(find_mode(elements2))
