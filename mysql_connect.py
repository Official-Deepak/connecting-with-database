import mysql.connector
import pandas as pd

def mydata(name,email,course):
    conn = mysql.connector.connect(host = "localhost",username = "root",password = "root",database = "deepak")
    my_cursor = conn.cursor()
    my_cursor.execute("create table if not exists students(name varchar(200),email varchar(220),course varchar(200))")
    sql = "Insert into students values(%s,%s,%s)"
    val = (name,email,course)
    my_cursor.execute(sql,val)
    my_cursor.execute("select name,email,course from students")
    result =  my_cursor.fetchall()
    all_name = []
    all_email = []
    all_course = []
    for x,y,z in result:
        all_name.append(x)
        all_email.append(y)
        all_course.append(z)
    
    #savind data to csv
    #dic = {"name":[name],"email":[email],"all_course":[course]}
    dic = {"name":all_name,"email":all_email,"all_course":all_course}
    df = pd.DataFrame(dic)
    df.to_csv("data.csv")

    conn.commit()
    conn.close()


name = input("Enter your name: ")
email = input("Enter your email: ")
course =input("Enter your course: ")

mydata(name,email,course)
