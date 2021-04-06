from vpython import *;

def insertion(ev):
    value=int(ev.text)
    hash_key = value % len(HashTable)  
    if(value not in HashTable[hash_key]):
        HashTable[hash_key].append(value)
        index1=HashTable[hash_key].index(value)
        index1 = index1 + 1
        object_table[hash_key].append(box(pos=vec(-60+(index1)*10,20-(hash_key*6.5),0),length=7, height=6, width=4,opacity=0.5,color=color.cyan))
        tag_table[hash_key].append(label( pos=vec(-60+(index1)*10,20-(hash_key*6.5),0), text=value,opacity=0,color=color.black,box=False))
     
       
def deletion(ev):
    value=int(ev.text)
    hash_key = value % len(HashTable)
    if value in HashTable[hash_key]:
        index1=HashTable[hash_key].index(value)
        HashTable[hash_key].remove(value)
        for j in range(index1+1,len(tag_table[hash_key])-1):
            tag_table[hash_key][j].text=tag_table[hash_key][j+1].text
        tag_table[hash_key][-1].visible=False
        object_table[hash_key][-1].visible=False
        tag_table[hash_key].pop()
        object_table[hash_key].pop()
    else:
        statement.visible = True
        sleep(1)
        statement.visible = False
        
                

def searching(ev):
    value=int(ev.text)
    hash_key = value % len(HashTable)
    if value in HashTable[hash_key]:
        index1=HashTable[hash_key].index(value)
        print('your searched value is in index:{}'.format(hash_key))
        sleep(0.5)
        object_table[hash_key][index1+1].color=color.red
        sleep(0.5)
        object_table[hash_key][index1+1].color=color.cyan

    else:
        print('No such value exist in the hash table')
        
           
T = text(text='Hash Table',align='center', color=vec(1,1,0),pos=vec(-10,32,10),height=4,opacity=1)
statement = label(pos = vector(10,7,0),height= 30,text = 'No such element exists',color = color.red,visible = False)
x=int(input('Enter the Hash Table Size:\n'))
object_table=[[] for _ in range(x)]
tag_table=[[] for _ in range(x)]
HashTable = [[] for _ in range(x)]   
for i in range(x):
    object_table[i].append(box(pos=vec(-60,20-(i*6.5),0),length=7, height=6, width=4,opacity=0.4,color=color.blue))
    tag_table[i].append(label( pos=vec(-60,20-(i*6.5),0), text=i,opacity=0,color=color.white,box=True))    
insertion = winput(prompt="\n\nInsert:", type='numeric', bind=insertion)
deletion= winput(prompt="\n\ndelete:", type='numeric', bind=deletion)
search= winput(prompt="\n\nSearch:", type='numeric', bind=searching)