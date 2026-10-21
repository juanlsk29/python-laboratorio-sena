import json

producto = {"nombre": "Cámara", "precio": 120000}

texto = json.dumps(producto, ensure_ascii=False)
recuperado = json.loads(texto)

print(texto)
print(recuperado["nombre"])

# PS C:\Users\PC\Desktop\python-laboratorio-4\practica-4-3> python json_cadenas.py
# {"nombre": "Cámara", "precio": 120000}
# Cámara