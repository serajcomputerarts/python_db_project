import sqlite3
import random
import string 
class Test:
    con=sqlite3.Connection
    # db is the name of database
    db="mylib.db"
    cur=str()
    def __init__(self):
        #connects to database
        self.con=sqlite3.connect(self.db)
        #create cursor
        self.cur=self.con.cursor()
    def create_tables(self):
        # This function creates database tables
        # Student,Book,Borrow are tables
        sqltable = """
            CREATE TABLE if not exists Student (
            sid int,
            sname VARCHAR(255),
            scity VARCHAR(255),
            sadd VARCHAR(255),
            primary key(sid)
        );"""
        self.cur.execute(sqltable)
        sqltable="""
        
        CREATE TABLE if not exists Books (
            bid int,
            btitle VARCHAR(255),
            bauther VARCHAR(255),
            bprice int,
            primary key(bid)
        );
        """
        self.cur.execute(sqltable)
        sqltable="""
        
        CREATE TABLE if not exists borrow (
            bid int,
            sid int,
            bdate VARCHAR(255)
        );
        """
        self.cur.execute(sqltable)
    def add_students(self):
        # I create data from random names
        names=["hadi","reza","ali","kazem"]
        city=["tabriz","Tehran","shiraz"]
        add=["P11","p300","P40","p60"]
        # add 10 random students 
        for x in range(10):
            insql="insert into student (sid,sname,scity,sadd) values ("+str(random.randint(1000,9999))+",'"+random.choice(names)+"','"+random.choice(city)+"','"+random.choice(add)+"');"
            self.cur.execute(insql)
            self.con.commit() 
        
    def show_all_students(self):
        r=self.cur.execute("select * from student")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
    def find_student_by_id(self,sid):
        r=self.cur.execute("select * from student where sid="+sid)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
    def find_student_by_name(self,sname):
        r=self.cur.execute("select * from student where sname='"+sname+"'")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)


ob=Test()
#creates database tables
#ob.create_tables()
#adds students to database
#ob.add_students()
#shows all students
#ob.show_all_students()
#finds student by id
#ob.find_student_by_id("1019")
#finds student by name
#ob.find_student_by_name("ali")

