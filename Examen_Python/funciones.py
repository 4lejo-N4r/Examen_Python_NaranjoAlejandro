import json
from user import usuario


def cargar_json(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def guardar_json(ruta_archivo, datos):
    with open(ruta_archivo, 'w') as f:
        json.dumps(datos, f, indent=4)


def agregar_usuario(user_data, ruta_archivo="user.json"):
    users = cargar_json(ruta_archivo)
    user = usuario(**user_data)
    users.append(user.to_dict())
    guardar_json(ruta_archivo, user)
    print(f"Camper {user.nombres} {user.apellidos} agregado correctamente.")


        
