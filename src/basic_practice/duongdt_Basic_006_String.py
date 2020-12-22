def main():
  for i in "Doan Thanh Duong":
    print(i)

  myName = "dOAN thanh duong"
  print(len(myName))
  print(myName.capitalize())

  myName = "Sáng chói lòa cả chiến mã"
  print(myName) # Sáng chói lòa cả chiến mã
  print(len(myName)) # 31
  #for i in myName:
  #  print(i)

  myName = "Sáng chói lòa cả chiến mã"
  print(myName) # Sáng chói lòa cả chiến mã
  print(len(myName)) # 25
  #for i in myName:
  #  print(i)

  myName = "Sáng chói lòa cả chiến mã"
  print("ng in myName = " + str("ng" in myName))

  myName = "Sáng chói lòa cả chiến mã"
  print("th not in myName = " + str("th" not in myName))


  myName = "Sáng chói lòa cả chiến mã"
  print("myName[0:5]=" + myName[0:5])

  print("myName[:5]=" + myName[:5])

  print("myName[2:]=" + myName[2:])

  print("myName[-5:-2]=" + myName[-5:-2])


  messageTemplate = "{} đã có mặt tại lớp học vào ngày {}"
  message = messageTemplate.format("Mr. Duong", "30/11/2020")
  print(message)

  message1 = "{0} đã có mặt tại lớp học vào ngày {1}"
  message = message1.format("Mr. Duong", "30/11/2020")
  print(message)

  message1 = "{1} đã có mặt tại lớp học vào ngày {0}"
  message = message1.format("30/11/2020", "Mr. Duong")
  print(message)

  message1 = "{1} đã có mặt tại lớp học vào ngày {0}, người thông báo: {1}"
  message = message1.format("30/11/2020", "Mr. Duong")
  print(message)

  message1 = "{name} đã có mặt vào ngày {date}, người thông báo: {name}"
  message = message1.format(date = "30/11/2020", name = "Mr. Duong")
  print(message)


  message1 = "{name} chấm {num_students:,} bài thi vào ngày {date}, điểm trung bình {avg:.2f}"
  message = message1.format(date = "30/11/2020", name = "Mr. Duong", num_students = 1097, avg = 8.7)
  print(message)



if __name__ == "__main__": 
    main()
else: 
    print ("duongdt_Basic_006_String.py imported")