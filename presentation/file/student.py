def getName():
    name=input("Write name : ")
    return name
def getTrade():
    trade=input("write trade : ")
    return trade
def getClass():
    studentClass=input("Write class : ")
    return studentClass
def getHome():
    home=input("write home : ")
    return home

name=getName()
trade=getTrade()
studentClass=getClass()
home=getHome()

fl=open("student.txt","a")
fl.write(f"Name : {name} \n")
fl.write(f"Trade: {trade} \n")
fl.write(f"Class: {studentClass} \n")
fl.write(f"Home : {home} \n")
fl.write(" \n \n \n")
fl.close()