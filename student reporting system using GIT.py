# name
# id 
#subject with mark
#total 
#grade

name = input("enter the NAME:")
stud_id = input("enter the number")

python_mark = int(input("enter the python mark:"))
dbms_mark = int(input("enter the dbms mark:"))
dsa_mark = int(input("enter the dsa mark:"))
it_mark = int(input("enter the it mark:"))
bi_mark = int(input("enter the bi mark:"))

marks = {"python": python_mark ,"Dbms":dbms_mark , "Dsa": dsa_mark, "It" : it_mark, "Bi" : bi_mark}

total = sum(marks.values())
average = total / len(marks)

if average <= 90:
    grade = "A+"

elif average <= 80 :
    grade = "B+"

elif average <= 70 :
    grade = "B"

elif average <= 60:
    grade = "C"

elif average <= 50:
    print = "D"

else:
    print("fail")

print("///////////////////////////////////////\n")
print("               STUDENT REPORT          \n")
print("///////////////////////////////////////")

print("STUDENT_NAME:",name)
print("STUDENT_ID:",stud_id )

print("marks:")
for key,value in marks.items():

    print(key,":" ,value )

print("TOTAL_MARK:",total)
print("GRADE:",grade)

print("atho painnurah effort ku palan erutha seri")

print("day two of my git learning journey")

print("today holiday i just practice my git")

print("hello guy")

print("hello iam praksh")
print("enn  peru prakash")


print("otha na tha")
print("iam hero")
 
