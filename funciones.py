def validador (lista):

  nacido = lista[1]
  altura = lista[2]

  edad = nacido >= 2010
  alto = altura >=180

  return [edad, alto]


