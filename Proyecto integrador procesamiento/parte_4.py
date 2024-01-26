import requests

url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('salida.csv', 'w') as file:
            file.write(response.text)

        print(f"El archivo CSV ha sido guardado con éxito como 'salida.csv'")
    else:
        print(f"Error al descargar CSV. Estatus: {response.status_code}")
        
get_request(url)
