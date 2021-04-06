from vpython import *

scene.width = 1000
scene.height = 700
scene.range = 13
lastbox = vector(0,1,0)

def Delete():
    key = str(input("Enter Key: "))
    if(keys.__contains__(key)):
        map[keys.index(key)]["first"].visible = False
        map[keys.index(key)]["second"].visible = False
        map[keys.index(key)]["third"].visible = False
        map[keys.index(key)]["fourth"].visible = False
        map[keys.index(key)]["fifth"].visible = False
 
def checkIf():
    key = str(input("Enter Key: "))
    if(keys.__contains__(key)):
        value = str(input("Enter Value: "))
        map[keys.index(key)]["fifth"].text = value
    else:
        Insert_node(key)


def Insert_node(key):
    keys.append(key)
    value = str(input("Enter Value: "))
    first = box(length=4,height=2,pos = vector(lastbox.x,lastbox.y,lastbox.z))
    second = box(length=4,height=2,pos = vector(lastbox.x + 10,lastbox.y,lastbox.z))
    third = arrow(pos=vector(lastbox.x+2,lastbox.y,lastbox.z),axis=vector(6,0,0),color=vector(0,0,1))
    fourth = label(text = key,pos=lastbox)
    fifth = label(text = value,pos = vector(lastbox.x + 10,lastbox.y,lastbox.z))
    lastbox.y = lastbox.y - 5
    dict_map = {
        "first" : first,
        "second" : second,
        "third" : third,
        "fourth" : fourth,
        "fifth" : fifth
    }
    map.append(dict_map)


keys = []
dict_map = {}
map = []

T = text(text='Dictionary',align='center', color=vec(0,0.5,0),pos=vec(0,5,0),height=1,opacity=1)
button(text="Insert",pos=scene.title_anchor,bind=checkIf)
button(text="Delete",pos=scene.title_anchor,bind=Delete)
