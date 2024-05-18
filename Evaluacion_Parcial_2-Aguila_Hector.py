def ingresar_datos():
    while True:
        nombre = input("Ingrese el nombre del trabajador: ")
        if nombre and len(nombre) <= 30:
            break
        else:
            print("Nombre inválido. Debe tener entre 1 y 30 caracteres.")

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

def calcular_liquidacion(sueldo_base, horas_extras):
    pago_hora_extra = (sueldo_base / 180) * 1.5 * horas_extras
    total_ingresos = sueldo_base + pago_hora_extra
    descuento_fonasa = total_ingresos * 0.07
    descuento_afp = total_ingresos * 0.10
    sueldo_neto = total_ingresos - (descuento_fonasa + descuento_afp)

    return pago_hora_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto

def mostrar_liquidacion(nombre, sueldo_base, pago_hora_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    print("\n----- Liquidación de Sueldo -----\n\n")
    print(f"Nombre del Trabajador: {nombre}\n")
    print(f"Sueldo Base: ${sueldo_base:.2f}")
    print(f"Pago por Horas Extras: ${pago_hora_extra:.2f}\n\n")
    print(f"\nTotal de Ingresos: ${total_ingresos:.2f}\n")
    print(f"Descuento por FONASA: ${descuento_fonasa:.2f}")
    print(f"Descuento por AFP: ${descuento_afp:.2f}\n\n")
    print(f"Sueldo Neto a Pagar: ${sueldo_neto:.2f}")
    print("-------------------------------\n")

def generar_archivo_liquidacion(nombre, sueldo_base, pago_hora_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto):
    archivo_nombre = f"Liquidación_{nombre.replace(' ', '_')}.txt"
    with open(archivo_nombre, 'w') as archivo:
        archivo.write("----- Liquidación de Sueldo -----\n\n")
        archivo.write(f"Nombre del Trabajador: {nombre}\n\n")
        archivo.write(f"Sueldo Base: ${sueldo_base:.2f}\n")
        archivo.write(f"Pago por Horas Extras: ${pago_hora_extra:.2f}\n\n")
        archivo.write(f"Total de Ingresos: ${total_ingresos:.2f}\n\n")
        archivo.write(f"Descuento por FONASA: ${descuento_fonasa:.2f}\n")
        archivo.write(f"Descuento por AFP: ${descuento_afp:.2f}\n\n")
        archivo.write(f"Sueldo Neto a Pagar: ${sueldo_neto:.2f}\n")
        archivo.write("-------------------------------\n")
    print(f"Archivo generado: {archivo_nombre}")

def main():
    while True:
        nombre, sueldo_base, horas_extras = ingresar_datos()
        pago_hora_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto = calcular_liquidacion(sueldo_base, horas_extras)
        mostrar_liquidacion(nombre, sueldo_base, pago_hora_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)
        generar_archivo_liquidacion(nombre, sueldo_base, pago_hora_extra, total_ingresos, descuento_fonasa, descuento_afp, sueldo_neto)
        
        continuar = input("¿Desea calcular la liquidación de otro trabajador? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()