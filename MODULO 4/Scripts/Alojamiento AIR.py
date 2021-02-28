import config as cfc
import csv
from restaurantLoop import *
from google.cloud import storage


def descarga_restaurantes():
    miApartamento = None
    listaApartamentos = []
    i = 0

    with open(cfc.csvpath) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:
            if i > 0:
                miApartamento = Apartment(pId=row[0], pCodPosta=row[40], pProvincia=row[39], pCiudad=row[38],
                                          pCodPais=row[43], pNombrePais=row[44], pLatitud=row[45], pLongitud=row[46])

                listaApartamentos.append(miApartamento)

            i += 1

    # Una vez tenemos la lista de apartamentos, la filtramos si así está configurado
    if cfc.filtroPais != '*':
        listaApartamentos = [x for x in listaApartamentos if x.codPais() == cfc.filtroPais]

    # Fichero
    filep = open('restaurants.csv', 'w')
    print(
        f"Id Apartamento\",\"Id Restaurante\",\"Nombre restaurante\",\"Url Restaurante\",\"Direccion\",\"Precio medio\",\"Valoracion\"",
        file=filep)

    # Obtenemos los datos de la app El Tenedor
    miRest = RestaurantLoop()

    for ap in listaApartamentos:
        miRest = RestaurantLoop()
        miRest.setData(pApartamento=ap, pFile=filep)  # Establecer url coordenadas todos los apartamentos

    miRest.empieza()  # Iniciar crawler
    filep.close()  # Cerrar fichero resultados


def sube_archivos():
    client = storage.Client.from_service_account_json('key.json')
    buckets = list(client.list_buckets())

    bucket = client.get_bucket(buckets[0])  # Cogemos el primer segmento de la lista

    # Subir fichero restaurantes
    blob = bucket.blob('restaurants.csv')
    blob.upload_from_filename('restaurants.csv')

    # Subir fichero apartamentos
    blob = bucket.blob('apartments.csv')
    blob.upload_from_filename(cfc.csvpath)


def mostrarMenu():
    print('Seleccionar opción:')
    print('1- Descargar restaurantes')
    print('2- Subir ficheros a Google Storage')
    print('3- Salir')


def main():
    salir = False
    print(chr(27) + "[2J")

    while not salir:
        mostrarMenu()
        opcion = str(input("Opción (1|2|3): "))

        if opcion == '3':
            salir = True
            break
        elif opcion == '1':
            descarga_restaurantes()
        elif opcion == '2':
            sube_archivos()
        else:
            print(chr(27) + "[2J")


if __name__ == "__main__":
    main()