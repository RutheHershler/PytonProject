import datetime
from Students import StudentsArr
from Card import card
from Bill import bill
from data import excel

import matplotlib.pyplot as mplt

# import logging


b=bill()
s=StudentsArr()
c=card()
studentOrTeacher=0
d=excel()

print("ברוך הבא !!")
select=input("לכניסה הקש 'enter' , ליציאה הקש 'exit'")


def namess():
    pass
def diagram():
    pass

while select!="exit":
    studentOrTeacher=input("מורה הקש 1 , תלמידה הקש 2")
    if studentOrTeacher=="2":
        nameOfLateStudent=input("נא הקלד את שמך")
        if s.find_student(nameOfLateStudent) != False:

            num = s.return_my_lates(nameOfLateStudent)
            s.add_late_for_student(nameOfLateStudent)
            if s.num_of_lates(nameOfLateStudent) :
                print("כרטיסיה עולה 20 שח")
                c.coins()
                c.print_card(nameOfLateStudent)
            b.new_bill(nameOfLateStudent,num)
    elif studentOrTeacher=="1":
        selectAction=input("1-לקבלת הרשימת הבנות שלא איחרו , 2- לקבלת שמות הבנות בכיתה,"
                           "5-ליצוא הנתונים לאקסל"
                           " 3-לקבלת הכיתה עם הכי הרבה איחורים , לקבלת דיאגרמה -4")
        if selectAction=="1":
            s.min_late()
        elif selectAction=="2":
            numclass=input("הכנס איזו כיתה /a/b/c")
            if numclass=="a" or numclass=="b" or numclass=="c":
                s.get_students_names_in_class(numclass)
        elif selectAction=="3":
            s.maxlateclass()
        if selectAction=="4":
            dict = []
            x = s.diagram()
            print(x)
            y = s.namess()
            mplt.bar(y, x)
            mplt.show()
        if selectAction=="5":
            s.output_data_excel()
        else:
            continue
    else:
        print("enter only 1/2")
        continue



