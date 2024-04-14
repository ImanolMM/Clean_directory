import os


def limpiar_carpeta(ruta):
    # Verificar si la ruta existe y es una carpeta
    if os.path.exists(ruta) and os.path.isdir(ruta):

        for elemento in os.listdir(ruta):
            ruta_elemento = os.path.join(ruta, elemento)

            if os.path.isfile(ruta_elemento):
                os.remove(ruta_elemento)
                print(f"Archivo {ruta_elemento} eliminado.")

            elif os.path.isdir(ruta_elemento):
                limpiar_carpeta(ruta_elemento)
        # Después de eliminar todos los elementos, intentar eliminar la carpeta principal
        try:
            if ruta != carpeta_para_borrar:
                os.rmdir(ruta)
                print(f"La carpeta {ruta} ha sido eliminada.")
        except PermissionError as e:
            print(f"No se pudo eliminar la carpeta {ruta}: {e}")
    else:
        print(f"La carpeta {ruta} no existe o no es una carpeta válida.")


# Ruta de la carpeta a limpiar
carpeta_para_borrar = ""

limpiar_carpeta(carpeta_para_borrar)
