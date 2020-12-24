import math

def main():
  minNumber = min(5, 10, 25)
  maxNumber = max(5, 10, 25)

  print((5, 10, 25), "minNumber", minNumber)
  print((5, 10, 25), "maxNumber", maxNumber) 

  absNumber = abs(-7.25)
  print(-7.25, "absNumber", absNumber)

  powerValue = pow(4, 3)
  print("pow(4, 3) = 4 * 4 * 4 =", powerValue)

  sqrtValue = math.sqrt(64)
  print("sqrt(64) =", sqrtValue)


  ceilValue = math.ceil(1.4)
  print("ceil(1.4)", ceilValue)
  floorValue = math.floor(1.4)
  print("floor(1.4)", floorValue)



if __name__ == "__main__": 
    main()
else: 
    print ("math.py imported")