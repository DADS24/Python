from collections import OrderedDict
res = {
  'platos':[{
    'nombre':'papas',
    'precio':'20'
  },
  {
    'nombre':'chili',
    'precio':'8'
  }],
  'calidad':'5',
  'rapidez':'8'
}

if 'platos' not in res.keys():
  print("No hay platos")

print(res)

# Extraer la palabra chili

#print(res['platos'][1]['nombre'])

for i in res['platos']:
  print(i['nombre'])
'''
for key in res.keys():
  print (key)
  print (res[key])
'''
#print(res.values())

dictRes = list(OrderedDict.fromkeys("abc"))
print(dictRes)
print(dictRes[0])