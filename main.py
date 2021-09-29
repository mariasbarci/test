import math

'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  flag = "este prim"
  for x in range(2, int(n / 2) + 1):
    if n % x == 0:
      flag = "nu este prim"

  return flag

'''
Returneaza produsul numerelor din lista lst.
'''

def get_product(lst):
  print("pb 2")
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  print("Prima metoda")
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  print("A doua metoda")
  
  
def main():
  print("Ce problema vreti sa rezolvati?")
  nrPb = input()

  if int(nrPb) == 1:
    print("Problema 1. Fie n = ")
    #citeste date ca sir de caractere
    str = input()

    #converteste datele de intrare la intreg
    num = int(str)

    rez = is_prime(num)

    print("Numarul " + str)
    print(rez)

  elif int(nrPb) == 2:
    print("Problema 2...")
    get_product([])

  elif int(nrPb) == 3:
    x = 0
    y = 0
    get_cmmdc_v1(x,y)
    get_cmmdc_v2(x,y)


if __name__ == '__main__':
  main()
