d={
    'clientes': {
    '':{
    'nome': 'elijose',
    'email': 'elijose55',
    'senha': '',
    'bairro': 'juruce',
    'celular': '976678686',
    }

    },

    'cozinheiro': {
    'a':{
    'nome': 'elijose',
    'email': 'elijose55',
    'senha': '',
    'bairro': 'juruce',
    'celular': '976678686',
    'status': 'online',
    'restaurante': 'asterix',
    'descricao': 'Comida boa e caseira focada em massas e paes',
    'cardapio': [[15,20,'Bolo de Cenoura'],[7,25,'Arroz Branco'],[8,24, 'Feijao Caseiro']],
    }
      }
      }



import json

with open('dict.json','w') as file:
    json.dump(d, file, indent=1)


