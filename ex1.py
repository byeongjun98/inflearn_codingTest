name = "박병준"
print(name)

fruits = ["사과", "배", "포도"]
for fruit in fruits:
    print(fruit)

age = 29
if age >= 20:
    print("성인입니다.")
else:
    print("성인이 아닙니다")

now = 24
if now >= 17 and now <= 23:
    print("운영시간입니다")
else:
    print("나가세요")

def check(name, age):
    if age >= 20:
        print(name, "성인입니다.")
    else:
        print(name, "성인이 아닙니다")

check("손님1", 19)
check("손님2", 30)
check("손님3", 10)
check("손님4", 50)