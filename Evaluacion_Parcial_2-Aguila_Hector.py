# Estructura condicional mientras se cumpla con el largo total de caracteres al ingresar nombre o en su defecto al no ingresar nada.
def ingresar_datos():
    while True:
        nombre = input("Ingrese el nombre del trabajador: ")
        if nombre and len(nombre) <= 30:
            break
        else:
            print("Nombre inválido. Debe tener entre 1 y 30 caracteres.")

    # Mientras el sueldo base y horas extras sean números positivos, se ejecuta el código.
    # Al llevar los except, nos arrojará un mensaje que indique que estos valores sean positivos.
    while True:
        try:
            sueldo_base = float(input("Ingrese el sueldo base: "))
            if sueldo_base > 0:
                break
            else:
                print("El sueldo base debe ser un valor numérico positivo.")
        except ValueError:
            print("El sueldo base debe ser un valor numérico positivo.")

    while True:
        try:
            horas_extras = float(input("Ingrese el número de horas extras trabajadas: "))
            if horas_extras >= 0:
                break
            else:
                print("Las horas extras deben ser un valor numérico positivo.")
        except ValueError:
            print("Las horas extras deben ser un valor numérico positivo.")
    
    return nombre, sueldo_base, horas_extras

# Declaración de variables y funciones donde se realizarán los cálculos correspondientes.
def calcular_liquidacion(sueldo_base, horas_extras):
    pago_hora_extra = (sueldo_base / 180) * 1.5 * horas_extras
    total_ingresos = sueldo_base + pago_hora_extra
    descuento_fonasa = total_ingresos * 0.07
    descuento_afp = total_ingresos * 0.10
    sueldo_neto = total_ingresos - (descuento_fonasa + descuento_afp)

    # Esto nos devuelve las variables con los datos ingresados
    # para posteriormente ser impresos por pantalla en la siguiente sección del código
    return pago_hora_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto

# Aquí se establece lo que se imprimirá por pantalla.
# Se agregó a las variables numéricas el formateador ".2f", que limita la cantidad de decimales hasta 2.
def mostrar_liquidacion(nombre, sueldo_base, pago_hora_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    print("\n----- Liquidación de Sueldo -----\n\n")
    print(f"Nombre del Trabajador: {nombre}\n")
    print(f"Sueldo Base: ${sueldo_base:.2f}")
    print(f"Pago por Horas Extras: ${pago_hora_extra:.2f}\n")
    print(f"Total de Ingresos: ${total_ingresos:.2f}\n")
    print(f"Descuento por FONASA: ${descuento_fonasa:.2f}")
    print(f"Descuento por AFP: ${descuento_afp:.2f}\n")
    print(f"Sueldo Neto a Pagar: ${sueldo_neto:.2f}")
    print("-------------------------------\n")

# En esta sección se genera el archivo ".txt" que contendrá la información mostrada anteriormente por pantalla.
# En cada línea se van agregando los datos almacenados en las funciones creadas más arriba.
# Se agregó a las variables numéricas el formateador ".2f", que limita la cantidad de decimales hasta 2.
def generar_archivo_liquidacion(nombre, sueldo_base, pago_hora_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    archivo_nombre = f"Liquidacion_{nombre.replace(' ', '_')}.txt"
    with open(archivo_nombre, 'w') as archivo:
        archivo.write("----- Liquidación de Sueldo -----\n\n")
        archivo.write(f"Nombre del Trabajador: {nombre}\n\n")
        archivo.write(f"Sueldo Base: ${sueldo_base:.2f}\n")
        archivo.write(f"Pago por Horas Extras: ${pago_hora_extra:.2f}\n\n")
        archivo.write(f"Total de Ingresos: ${total_ingresos:.2f}\n")
        archivo.write(f"Descuento por FONASA: ${descuento_fonasa:.2f}\n")
        archivo.write(f"Descuento por AFP: ${descuento_afp:.2f}\n\n")
        archivo.write(f"Sueldo Neto a Pagar: ${sueldo_neto:.2f}\n")
        archivo.write("-------------------------------\n")
    print(f"Archivo generado: {archivo_nombre}")

# En esta sección se define la función "main" para repetir un bucle infinito mientras se cumpla la condición establecida.
def main():
    while True:
        nombre, sueldo_base, horas_extras = ingresar_datos()
        pago_hora_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto = calcular_liquidacion(sueldo_base, horas_extras)
        mostrar_liquidacion(nombre, sueldo_base, pago_hora_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)
        generar_archivo_liquidacion(nombre, sueldo_base, pago_hora_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)
        
        # Aquí validamos si se desea generar otra liquidación, donde el usuario debe responder Sí o No, con las letras "s" o "n".
        # Se implementa el método ".lower" para que se asuma que el carácter ingresado sea minúscula y así evitar algún fallo en la lectura.
        continuar = input("¿Desea calcular la liquidación de otro trabajador? (s/n): ").lower()
        if continuar != 's':
            break

# Código que me permite ejecutar y repetir el programa.
if __name__ == "__main__":
    main()
