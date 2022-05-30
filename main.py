from xml.dom.minidom import Element
import numpy as np
from modules import printando

teste_el = Element('teste').element

console.log('oi',teste_el)


arr = np.array([22,58,34,121])

pyscript.write('teste',arr) #seria o equivalente ao innerHTML


def testando(*args):
    pyscript.write('teste',arr)
    printando()
    #pyscript.write('teste','hello there')