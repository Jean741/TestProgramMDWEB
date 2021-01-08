from io import BytesIO
import json

from exercice1 import trieCroissant
from exercice2 import *


#test du trie
def test_trieCroissant():
	#Exemple de liste a trier
	liste=[1.3,2.5,4.6,7.2,0.4,-0.8,6.9,1.2,0.6,1.2]
	assert trieCroissant(liste) == sorted([1.3,2.5,4.6,7.2,0.4,-0.8,6.9,1.2,0.6,1.2])
	assert trieCroissant([1,0,2]) == [0,1,2]
	assert trieCroissant([]) == []
	assert trieCroissant([0,0,2]) == [0,0,2]


def test_convertExelFileToJson():
    convertExelFileToJson('test_exemple.xlsx',4,11)
    local_res = json.load(open("test_exemple.json"))
    assert local_res == getJsonFromExel('test_exemple.xlsx',4,11)

    convertExelFileToJson('test_exemple.xlsx',5,8)
    local_res = json.load(open("test_exemple.json"))
    assert local_res == getJsonFromExel('test_exemple.xlsx',5,8)