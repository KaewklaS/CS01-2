a = int(input("คะแนนเก็บของนักเรียน: "))
b = int(input("คะแนนนสอบกลางภาคของนักเรียน: "))
c = int(input("คะแนนสอบปลายภาคของนักเรียน: "))
d = (a+b+c)
if (d>100):
    print("ตรวจสอบคะแนนอีกครั้ง")
elif (d<0):
    print("ตรวจสอบคะแนนอีกครั้ง")
elif (d>=80):
    print("Grade A")
elif (d>=75):
    print("Grade B+")
elif (d>=70):
    print("Grade B")
elif (d>=65):
    print("Grade C+")
elif (d>=60):
    print("Grade C")
elif (d>=55):
    print("Grade D+")
elif (d>=50):
    print("Grade D")
elif (d<50):
    print("Grade F")
