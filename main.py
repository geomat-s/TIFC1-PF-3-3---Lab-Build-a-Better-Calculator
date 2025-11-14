def main():
  print("Hello learners!")

def addmultiplenumbers(lista):
  return sum(lista)

def multiplymultiplenumbers(lista):
  resultado_final = 1

  for number in lista:
    resultado_final *= number

  return resultado_final

def isiteven(num):
  if num % 2 == 0:
    return True
  else:
    return False

def isitaninteger(num):
  if num.is_integer():
    return True
  else:
    return False

if __name__=="__main__":
  main()