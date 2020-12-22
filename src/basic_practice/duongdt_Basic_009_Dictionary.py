def main():
  # UnOrdered, changeable and does not allow duplicates.
  carDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 1924
  }

  print(carDict)

  print(carDict["brand"])
  #print(carDict["brandx"])
  print("brandx" in carDict)
  print(carDict.values())
  print(carDict.items())




  carDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  for item in carDict:
    print(item)
  
  for item in carDict.keys():
    print(item)

  for item in carDict.values():
    print(item)

  for item in carDict.items():
    print(item)

  for key, value in carDict.items():
    print(key + " -> " + str(value))


  carDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
  }
  carDict["name"] = "MyCar"
  carDict["year"] = "1990"
  print(carDict)

  carDict.update({"year":"1991", "status":"OK"})
  print(carDict)

  carDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
  }
  carDict.pop("brand")
  print(carDict)

  carDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
  }
  carDict.clear()
  print(carDict)


if __name__ == "__main__": 
    main()
else: 
    print ("duongdt_Basic_009_Dictionary.py imported")