import typing

def main():
  # Sets are used to store multiple items in a single variable.
  # UnOrdered + UnIndexed
  fruitSet = {"apple", "banana", "cherry"}
  print(fruitSet)

  fruitSet = set(("apple", "banana", "cherry"))
  print(fruitSet)

  # Do not allow duplicate values
  fruitSet = {"apple", "banana", "cherry", "cherry", "banana"}
  print(fruitSet)

  # UnChangeable, but you can add new items
  fruitSet = {"apple", "banana", "cherry"}
  fruitSet.add("apple1")
  fruitSet.add("apple2")
  print(fruitSet)


  # Can contain different data types
  fruitSet: typing.Set[typing.Any] = {"apple", "banana", "cherry"}
  fruitSet.add(109)
  print(fruitSet)

  # Add duplicate item -> do nothing
  fruitSet = {"apple", "banana", "cherry"}
  fruitSet.add("apple")
  print(fruitSet)

  # Length of a Set
  fruitSet = {"apple", "banana", "cherry"}
  print(len(fruitSet)) 


  # Access Items
  for fruit in fruitSet:
    print(fruit)

  # Check a item in set
  print("banana" in fruitSet) 

  # Add items
  fruitSet1: typing.Set[typing.Any] = {"apple"}
  fruitSet2: typing.Set[typing.Any] = {"apple", "banana", "cherry"}
  fruitSet1.update(fruitSet2)
  print(fruitSet1) 

  fruitSet1.update([1, 2, 3, 4])
  print(fruitSet1)




  # Remove item
  fruitSet = {"apple", "banana", "cherry"}
  fruitSet.remove("apple")
  fruitSet.discard("banana")
  print(fruitSet) 

  # Remove all of items
  fruitSet = {"apple", "banana", "cherry"}
  fruitSet.clear()
  print(fruitSet)


if __name__ == "__main__": 
    main()
else: 
    print ("duongdt_Basic_008_Set.py imported")