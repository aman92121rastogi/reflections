bob = {'name':"bob Smith",'age':23,'address':"Amroha"}
bobu = {'name':"bobu Smith",'age':24,'address':"Amroha"}

people = [bob , bobu]

for person in people:
  print (person['name'] , person['age'])
  
  
  
  
  
  
  
rec = [person['name'] for person in people if person['age'] > 23]
print rec
	
