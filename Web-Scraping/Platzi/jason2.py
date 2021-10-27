import json

#Escribir JSON

data = {}
data['cliente'] = []

data['cliente'].append({
    'first_name': 'Sigir',
    'last-name': 'Mannoc',
    'age': 2,
    'amount': 7.17
})

data['cliente'].append({
    'first_name': 'Sidsagir',
    'last-name': 'sa',
    'age': 2,
    'amount': 7.17
})

data['cliente'].append({
    'first_name': 'Sidsagir',
    'last-name': 'Mandsanoc',
    'age': 2,
    'amount': 7.17
})

with open('1.json', 'w') as file:
    json.dump(data, file, indent = 4)

# Leer JSON

with open('1.json') as file:
    data = json.load(file)

    for client in data['cliente']:
        print('First name: ', client['first_name'])
        print('Last name: ', client['last-name'])
        print('Age: ', client['age'])
        print('Amount: ', client['amount'])
        print('')