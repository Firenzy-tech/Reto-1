# reto 1 mision tic

start = True
product = []
descrip = []
cant_product = 0

while start:
    descrip.append(str(input("Ingrese descripción del producto ")))
    product.append(float(input("Ingrese el valor unitario del producto ")))
    cant_product = 1+cant_product

    keep = str(input("Desea continuar registrando más productos Ingrese S para si o N para no").upper())

    if keep == "N":
        start = False
        for i in range(0, len(product)):
            print(product[i])
            print(dir(list))
    else:

        start = True
