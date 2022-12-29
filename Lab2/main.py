import sys
import json
from Dog import Dog
from Beagle import Beagle
from Cavalier import Cavalier
from Pomeranian import Pomeranian
from Samoyed import Samoyed

def write(data):
    jsonstr = json.dumps(data, indent = 4)
    open('./objects.json','w').write(jsonstr)
def read_from_json():
    return json.load(open('./objects.json','r'))

d = Dog("workers","Japan","black")
b = Beagle("hunter","UK","brown",5,0.5)
c = Cavalier("hunter","UK","blenheim",70000,"great")
p = Pomeranian("hunter","UK","white",10,7)
s = Samoyed("herder","Russia","white",0.8)

l=[d, b, c, p, s]
data = {
    'amount': len(1),
    'obj' :[]
}
for elem int l:
    data['obj'].append(elem.__dict__)

write(data)
data.clear()
l.clear()
data = read_from_json()
for elem in data['obj']:
    if elem['name'] == "Dog"
       obj = Dog(elem['_group'], elem['_country'], elem['_color'])
    elif elem['name'] == "Beagle"
       obj = Beagle(elem['_group'], elem['_country'], elem['_color'], elem['_age'], elem['_max_height'])
    elif elem['name'] == "Cavalier"
       obj = Cavalier(elem['_group'], elem['_country'], elem['_color'], elem['_price'], elem['_health_condition'])
    elif elem = "Pomeranian"
       obj = Pomeranian(elem['_group'], elem['_country'], elem['_color'], elem['_max_length'])
    elif elem['Samoyed']
       obj = Beagle(elem['_group'], elem['_country'], elem['_color'], elem['_age'], elem['_max_height'])
l.append(obj)
for elem in l:
    elem._repr__()


    
