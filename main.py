from tienda import calcular_precio, calcular_iva

def main ():
    precio = float(input("Ingresa el precio del producto: "))
    descuento = float(input("Ingresa el porcentaje del descuento: "))

    try:
        precio_con_descuento = calcular_precio(precio, descuento)
        precio_final = calcular_iva(precio_con_descuento)

        print(f"Precio con descuento : {precio_con_descuento:.2f}")
        print(f"Precio final con IVA : {precio_final:.2f}")
    except ValueError as e:
        print("Error: {e}")

if __name__ == "__main__":
    main()
    