

#abrimos el archivo ventas.csv
def apertura_archivo():
    with open ("datos/ventas.csv", "r") as ventas: #.. significa que tiene que subir un nivel ya que ventas.csv y el script estan en distintas carpetas
        next(ventas) #descarta la primer linea del archivo
        datos = ventas.readlines()#copia lo que haya en el archivo a la variable datos
    return datos 

#calculamos ventas totales
def ventas_totales(datos):
    total = 0
    for linea in datos:
        id, producto, cantidad, precio, fecha = linea.strip().split(",") #desempaqueta los valores, tomando la coma como referencia 
        precio = float(precio)
        cantidad = int(cantidad)
        total += precio*cantidad
    return total

def producto_mas_vendido(datos):
    Notebook=0
    Mouse=0
    Teclado=0
    for linea in datos:
        id, producto, cantidad, precio, fecha = linea.strip().split(",")
        cantidad = int(cantidad)
        if producto == "Notebook":
            Notebook += cantidad
        elif producto == "Mouse":
            Mouse += cantidad 
        elif producto == "Teclado":
            Teclado += cantidad

    if Notebook > Mouse and Notebook > Teclado:
        MayorVentas = "Notebook"
    elif Mouse > Notebook and Mouse > Teclado:
        MayorVentas = "Mouse"
    elif Teclado > Notebook and Teclado > Mouse:
        MayorVentas = "Teclado"
    else:
        MayorVentas= "Empate"

    return MayorVentas

def ventas_mensuales(datos):
    meses = {} # es una diccionario vacio donde vamos a contener el mes y el total de venta

    for linea in datos:
        id, producto, cantidad, precio, fecha = linea.strip().split(",")
        cantidad = int(cantidad)
        precio = float(precio)

        venta= cantidad*precio

        mes = fecha.split("-")[1] #crea una lista de fecha, tomando como referencia el guion para separar.

        if mes not in meses:
            meses[mes]=0 #inicializa cada mes en 0 ya que pregunta si existe en el diccionario mes
        
        meses[mes] += venta

    return meses

def resultados(TotalVentas, ProdMasVendido, VentasXmes):
    with open("/content/Trabajo-Practico-n-2/resultados/informe.txt", "w") as archivo:
        archivo.write(f"El total de ventas fue de {TotalVentas}\n")
        archivo.write(f"El producto mas vendido fue: {ProdMasVendido}\n")

        archivo.write("Ventas por mes:\n")
        for mes, total in VentasXmes.items():
            archivo.write(f"Mes {mes}: ${total}\n")

archivo = apertura_archivo()
TotalVentas = ventas_totales(archivo)
pmv = producto_mas_vendido(archivo)
ventas_por_mes = ventas_mensuales(archivo)
resultados(TotalVentas, pmv, ventas_por_mes)
#Fin del SCRIPT - El analisis de las ventas fue completado con exito
