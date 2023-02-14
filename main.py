import requests

status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})

print(res.status_code)
print(res.json())

res = requests.post(f'https://petstore.swagger.io/v2/pet/', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data='{"id": 0, "category": { "id": 0, "name": "string" }, "name": "doggie", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string" } ], "status": "available"}')
print(res.status_code)
print(res.json())

petId = res.json()['id']
print(petId)

res = requests.put(f'https://petstore.swagger.io/v2/pet/', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data='{"id": ' + str(petId) + ', "category": { "id": 0, "name": "string" }, "name": "777", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string" } ], "status": "available"}')
print(res.status_code)
print(res.json())

res = requests.delete(f'https://petstore.swagger.io/v2/pet/{petId}')
print(res.status_code)

