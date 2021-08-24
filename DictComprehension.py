country_to_capital = {'United Kingdom': 'London', 'Brazil':'Brasilia' ,'Moroco': 'Rabat'}
Capital_to_country = { capital: country for country, capital in country_to_capital.items}
from pprint import pprint as pp
pp(Capital_to_country)
{'Brasilia':'Brazil','London':'United Kingdom','Rabat':'Moroco', 'Stockholm': 'Sweden'}
words =["hi," "hello", "foxtrot","hotel"]
{x[0]: x for x in words }
{'h' :'hotel' ,'f': 'foxtrot'}
