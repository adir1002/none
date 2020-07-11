def sorter(item):
    return item['age']

persons= [
    {'name':'Adir', 'age' : 23},
    {'name':'Keren', 'age' : 20},
]

persons.sort(key=sorter)
print(persons)
persons.sort(key=lambda item: item['name'])
print()
print(persons)