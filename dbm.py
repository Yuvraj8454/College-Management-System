import pymysql as p
def getconnection():
    return p.connect(user="root",password="",database="bhagyashree",host="localhost")

def adddata(t):
    con=getconnection()
    cur=con.cursor()
    query="insert into records(ID,USER_NAME,EMAIL,PASSWORD,CITY) values(%s,%s,%s,%s,%s)";
    cur.execute(query,t)
    con.commit()
    con.close()

def addattendance(t):
    con=getconnection()
    cur=con.cursor()
    query="insert into attendance(ID,USER_NAME,ATTENDANCE) values(%s,%s,%s)";
    cur.execute(query,t)
    con.commit()
    con.close()

def addresult(t):
    con=getconnection()
    cur=con.cursor()
    query="insert into result(ID,USER_NAME,RESULT) values(%s,%s,%s)";
    cur.execute(query,t)
    con.commit()
    con.close()

def fetchdata():
    con=getconnection()
    cur=con.cursor()
    cur.execute("select * from records;")
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist

def fetchattendance():
    con=getconnection()
    cur=con.cursor()
    cur.execute("select * from attendance;")
    attendance=cur.fetchall()
    con.commit()
    con.close()
    return attendance
    
def fetchresult():
    con=getconnection()
    cur=con.cursor()
    cur.execute("select * from result;")
    result=cur.fetchall()
    con.commit()
    con.close()
    return result

def register(t):
    con=getconnection()
    cur=con.cursor()
    query="insert into users(name,pass) values(%s,%s)";
    cur.execute(query,t)
    con.commit()
    con.close()
