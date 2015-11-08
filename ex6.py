fields = ['name','age','pay','address']
values = ['Aman','23','18500','Gurgaon']
reform = dict.fromkeys(fields , values * 3)
print reform 