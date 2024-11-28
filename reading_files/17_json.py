import json
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")

data_json = '''
{
  "assinantes" : [
    {
      "nome": "Adriano Soares",
      "telefone": "51 99999999",
      "email": "adriano@email.com",
      "em_dia": true
    },
    {
      "nome": "Juliano faccioni",
      "telefone": "51 99999999",
      "email": "juliano@email.com",
      "em_dia": false
    }
    ],
  "data_extração": "2023/08/22"
}
'''

# Json to Dict
json_dict = json.loads(data_json)

print(type(data_json))  # str
print(type(json_dict))  # dict
print(json_dict)  # python dict

# Dict to Json
dict_json = json.dumps(json_dict, ensure_ascii=False, indent=2)
print(type(json_dict))
print(type(dict_json))
print(dict_json)

# # Lendo arquivos json
curr_dir = Path(__file__).parent
with open(curr_dir / 'jsons' / 'assinantes.json', encoding='utf-8') as file:
    loaded_data = json.load(file)
print(type(loaded_data))  # Dict
print(loaded_data)
print(loaded_data['assinantes'])

# # Escrevendo arquivos json
with open(curr_dir / 'jsons' / 'copy.json', 'w', encoding='utf-8') as file:
    json.dump(loaded_data, file, indent=2, ensure_ascii=False)
