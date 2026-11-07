# =========================
# ამოცანა 1. მონაცემთა ტიპები და type()
# =========================

age = 55
height = 1.65
name = "Flora"
is_student = True

print("ასაკი:", age, type(age))
print("სიმაღლე:", height, type(height))
print("სახელი:", name, type(name))
print("სტუდენტი:", is_student, type(is_student))


# =========================
# ამოცანა 2. მათემატიკური ოპერაციები
# =========================

num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

print("ჯამი:", num1 + num2)
print("სხვაობა:", num1 - num2)
print("ნამრავლი:", num1 * num2)

if num2 != 0:
    print("გაყოფა:", num1 / num2)
    print("მთელი გაყოფა:", num1 // num2)
    print("ნაშთი:", num1 % num2)
else:
    print("ნულზე გაყოფა შეუძლებელია.")

print("ხარისხი:", num1 ** num2)


# =========================
# ამოცანა 3. სტრიქონების მანიპულაცია
# =========================

first_name = input("შეიყვანეთ სახელი: ")
last_name = input("შეიყვანეთ გვარი: ")

full_name = first_name + " " + last_name

print("სრული სახელი:", full_name)
print("დიდი ასოებით:", full_name.upper())
print("პატარა ასოებით:", full_name.lower())
print("პირველი ასო დიდი:", full_name.capitalize())


# =========================
# ამოცანა 4. print()-ის პარამეტრები
# =========================

print("Python", "Java", "C++", sep="-")
print(10, 20, 30, sep="***")
print("ერთი", "ორი", "სამი", sep="\t")

print("გამარჯობა", end=" ")
print("მოგესალმებით!")

print("პირველი", end=" | ")
print("მეორე", end=" | ")
print("მესამე")


# =========================
# ამოცანა 5. შედარების და ლოგიკური ოპერატორები
# =========================

age = 20
height = 1.70
is_student = True

print("== :", age == 20)
print("!= :", age != 18)
print("> :", age > 18)
print("< :", age < 25)
print(">= :", age >= 20)
print("<= :", age <= 20)

print("and :", age > 18 and is_student == True)
print("or :", height > 1.80 or is_student == True)
print("not :", not is_student)


# =========================
# ამოცანა 6. input() და ტიპის სწორად გარდაქმნა
# =========================

user_name = input("შეიყვანეთ სახელი: ")
user_age = int(input("შეიყვანეთ ასაკი: "))
user_height = float(input("შეიყვანეთ სიმაღლე მეტრებში: "))

print("გამარჯობა,", user_name)
print("თქვენი ასაკია:", user_age)
print("თქვენი სიმაღლეა:", user_height, "მეტრი")