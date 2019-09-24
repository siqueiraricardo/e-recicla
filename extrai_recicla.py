import request


payload = {'fabricante': bombril, 'tiporeciclavel': plastico}
r = request.get('http://localhost:3000/recicla', params=payload)

print(r.text)