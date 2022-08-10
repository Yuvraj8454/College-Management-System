import re
from flask import Flask,request, render_template, redirect,session
from dbm import addattendance, adddata, addresult, fetchdata,fetchattendance, fetchresult,register,getconnection
app = Flask(__name__)
app.secret_key= "bhagyashree"

@app.route('/')
def home1():
   return render_template("home.html") 

@app.route('/studentlink')
def home():
   return render_template("student.html")

@app.route('/teacherlink')
def teacher():
   return render_template("teacher.html")

@app.route('/teacher1link')
def teacher1():
   return render_template("teacher1.html")

@app.route('/aboutlink')
def about():
   return render_template("about.html")

@app.route('/addrecords')
def addrecords1():
   return render_template("addrecords.html")

@app.route('/addattendance')
def addattendance1():
   return render_template("addattendance.html")

@app.route('/addresult')
def addresult1():
   return render_template("addresult.html")

@app.route('/feesstructure')
def fees():
   return render_template("feesstructure.html")

@app.route('/registerlink')
def register1():
   return render_template('register.html')

@app.route('/loginlink')
def login1():
   return render_template('login.html')

@app.route('/logoutlink')
def logout1():
   return render_template('login.html')

@app.route('/addrecords' ,methods=["POST"]) 
def addrecords2():
   ID=request.form["ID"]
   USER_NAME=request.form["USER_NAME"]
   EMAIL=request.form["EMAIL"]
   PASSWORD=request.form["PASSWORD"]
   CITY=request.form["CITY"]
   t=(ID,USER_NAME,EMAIL,PASSWORD,CITY)
   adddata(t)
   return redirect("/addrecords")  

@app.route("/recordsview")
def recordsview():
   datalist=fetchdata()
   return render_template("recordsview.html",data=datalist)

@app.route('/addattendance' ,methods=["POST"]) 
def addattendance2():
   ID=request.form["ID"]
   USER_NAME=request.form["USER_NAME"]
   ATTENDANCE=request.form["ATTENDANCE"]
   t=(ID,USER_NAME,ATTENDANCE)
   addattendance(t)
   return redirect("/addattendance")  

@app.route("/attendanceview")
def attendanceview():
   attendance=fetchattendance()
   return render_template("attendanceview.html",data=attendance)

@app.route('/addresult' ,methods=["POST"]) 
def addresult2():
   ID=request.form["ID"]
   USER_NAME=request.form["USER_NAME"]
   RESULT=request.form["RESULT"]
   t=(ID,USER_NAME,RESULT)
   addresult(t)
   return redirect("/addresult")  

@app.route("/resultview")
def resultview():
   result=fetchresult()
   return render_template("resultview.html",data=result)

@app.route('/registerlink' ,methods=["POST"]) 
def register2():
   name=request.form["name"]
   password=request.form["pass"]
   t=(name,password)
   register(t)
   return redirect("/registerlink")

@app.route('/loginlink' ,methods=["POST"]) 
def login2():
   if request.method =='POST' and 'name' in request.form and 'pass' in request.form:  
      username=request.form["name"]
      password=request.form["pass"]
      con=getconnection()
      cur=con.cursor()
      cur.execute('select * from users where name=%s and pass=%s',(username,password));
      result=cur.fetchone()
      if result:
         session['k']=True
         
         return redirect('/teacherlink')
      else:
         return render_template('/login.html')



@app.route('/logoutlink')
def logout2():
   session.pop('name',None)
   session.pop('pass',None)
   return render_template('login.html')


if __name__=="__main__":
    app.run() 