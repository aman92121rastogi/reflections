import pprinter

aman = dict(name = "aman rastogi", age = 23)
paras = dict(name = "paras rastogi",age = 19)

db = {}
db['aman'] = aman
db['paras'] = paras

print db['aman']['name']
pprinter.pprinter(db)
