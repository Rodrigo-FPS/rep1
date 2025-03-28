import requests

def buscar_palabras(   target_url, archivo):
    try:
        with open( archivo, 'r') as f:
            palabras = f.read().splitlines()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return
    
    for palabra in palabras:
        url = f"{target_url.rstrip('/')}/{palabra}"
        try:
            respuesta = requests.get(url,timeout=5)
            if respuesta.status_code == 200:
                print(f"Encontrado: {url} (Código {respuesta.status_code})")
            elif respuesta.status_code == 403:
                print(f"Acceso denegado: {url} (Código {respuesta.status_code})")
            elif respuesta.status_code == 404:
                print(f"No encontrado: {url} (Código {respuesta.status_code})")
            else:
                print(f"Estado desconocido: {url} (Código {respuesta.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con {url}: {e}")

TARGET_URL = "http://127.0.0.1:8000"  
archivo_palabras = "lista_palabras.txt"
print(f"Buscando palabras de {archivo_palabras} en {TARGET_URL}...\n")
buscar_palabras(TARGET_URL, archivo_palabras)
