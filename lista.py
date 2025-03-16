marcas_de_celulares = ['iphone', 'xiaomi', 'samsumg', 'android']
print("Marcas de celulares: \n", marcas_de_celulares)
marca_nova = (input("Digite uma nova marca de celular: "))
marcas_de_celulares.append(marca_nova)
print(f'\n{marca_nova}, foi adicionado a lista.')
marcas_de_celulares.sort()
print(f'\nLista atualizada em ordem alfabética:,\n\n {marcas_de_celulares}')