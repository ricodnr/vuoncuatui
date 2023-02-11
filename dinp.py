
fh=open('plants.txt','r')
c=0
tl=list()
for line in fh:
    line = line.rstrip().split('--')
    tl.append(line)
    
    
#print(tl[1][0])
js=''
for i in tl:
    c+=1
    minTemp=i[1].split()[0]
    maxTemp=i[1].split()[1]
    minHumi=i[2].split()[0]
    maxHumi=i[2].split()[1]
    js += f'''
  {{
    "model": "grows.Tata",
    "pk": {c},
    "fields": {{
      "plant": "{i[0]}",
      "name": "{i[3]}",
      "minTemp": "{minTemp}",
      "maxTemp": "{maxTemp}",
      "minHumi": "{minHumi}",
      "maxHumi": "{maxHumi}",
      "fintime": "{i[4]}"
    }}
  }}'''
    if c != len(tl):
        if c == 1:
            js = '[' + js + ','
        else:
            js += ','
    else:
        js += '\n]'
wf = open('dinp.json','w')
wf.write(js)
