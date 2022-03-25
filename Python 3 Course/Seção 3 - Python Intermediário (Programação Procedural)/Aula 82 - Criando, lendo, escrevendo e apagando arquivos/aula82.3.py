import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    }
}

d1_json = json.dumps(d1, indent=True)

with open('aula82.3.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)
