from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import numpy as np
import sqlite3
import mysql.connector
import re
from sklearn.preprocessing import StandardScaler
import joblib
model = joblib.load("train_model1.pkl")
scaler = StandardScaler()

import secrets

  
app = Flask(__name__)

app.secret_key = '6f28a750db5ccee79a01c796852cf6a7'
  
conn = mysql.connector.connect(user="redblack", password="Server@1", host="test-for-python.mysql.database.azure.com", port=3306, database="personality_predict", ssl_ca="{ca-cert filename}", ssl_disabled=False);
print ("Opened database successfully");

conn.cursor().execute("CREATE TABLE IF NOT EXISTS predict_person (name VARCHAR(30), email VARCHAR(30), password VARCHAR(30))");
print ("Table created successfully");

conn.cursor().execute('CREATE TABLE IF NOT EXISTS questionery (id INTEGER PRIMARY KEY AUTO_INCREMENT, op1 varchar(10), op2 varchar(10), op3 varchar(10), op4 varchar(10), op5 varchar(10), op6 varchar(10), op7 varchar(10), op8 varchar(10), op9 varchar(10), op10 varchar(10), con1 varchar(10), con2 varchar(10), con3 varchar(10), con4 varchar(10), con5 varchar(10), con6 varchar(10), con7 varchar(10), con8 varchar(10), con9 varchar(10), con10 varchar(10), ext1 varchar(10), ext2 varchar(10), ext3 varchar(10), ext4 varchar(10), ext5 varchar(10), ext6 varchar(10), ext7 varchar(10), ext8 varchar(10), ext9 varchar(10), ext10 varchar(10), agr1 varchar(10), agr2 varchar(10), agr3 varchar(10), agr4 varchar(10), agr5 varchar(10), agr6 varchar(10), agr7 varchar(10), agr8 varchar(10), agr9 varchar(10), agr10 varchar(10), ne1 varchar(10), ne2 varchar(10), ne3 varchar(10), ne4 varchar(10), ne5 varchar(10), ne6 varchar(10), ne7 varchar(10), ne8 varchar(10), ne9 varchar(10), ne10 varchar(10))')

print ("Table created successfully");
conn.cursor().close()



def predict():

    return




@app.route('/')
def home():
	return render_template('home.html')

@app.route('/admin',methods =['GET', 'POST'])
def admin():
    email="vidya@gmail.com"
    password=123

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email == "vidya@gmail.com" and password == "123":
            return render_template('upload.html')
           
    return render_template('admin.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        if file:
            file.save(r'C:\Users\Administrator\Desktop\personality_predict\uploads_files\\' + file.filename)
            # message = 'File uploaded successfully!'
            flash('CSV file uploaded successfully!', 'success')
            return redirect(url_for('/upload'))
         
    
          
    

  
@app.route('/note', methods =['GET', 'POST'])
def note():
    return render_template('que2.html')

@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get the username and password from the form data
        email = request.form['email']
        password = request.form['password']

        # check if the user exists in the database
        conn = mysql.connector.connect(user="redblack", password="Server@1", host="test-for-python.mysql.database.azure.com", port=3306, database="personality_predict", ssl_ca="{ca-cert filename}", ssl_disabled=False);
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM predict_person WHERE email=%s AND password=%s''', (email, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            # if the user exists, redirect to the home page
            print('login success')
            return render_template('note.html')
            # return render_template('que2.html')
        else:
            # if the user doesn't exist, show an error message
            return render_template('login.html', error='Invalid username or password')



    return render_template('login.html')

     



   
  
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))
  

@app.route('/register', methods =['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        with mysql.connector.connect(user="redblack", password="Server@1", host="test-for-python.mysql.database.azure.com", port=3306, database="personality_predict", ssl_ca="{ca-cert filename}", ssl_disabled=False) as con:
            cur = con.cursor()
            cur.execute('''INSERT INTO predict_person(name, email, password) VALUES (%s,%s,%s)''',(userName, email, password))

            con.commit()
            msg = "record added successfully"

    return render_template('register.html')


@app.route('/questions', methods =['GET', 'POST'])
def questions():

  if request.method == 'POST':
      gender = request.form['gender']
      if(gender == "Female"):
        gender_no = 1
      else:
        gender_no = 2
      age = request.form['age']
      openness1 = request.form['openness1']
      openness2 = request.form['openness2']
      openness3 = request.form['openness3']
      openness4 = request.form['openness4']
      openness5 = request.form['openness5']
      openness6 = request.form['openness6']
      openness7 = request.form['openness7']
      openness8 = request.form['openness8']
      openness9 = request.form['openness9']
      openness10 = request.form['openness10']
      neuroticism1 = request.form['neuroticism1']
      neuroticism2 = request.form['neuroticism2']
      neuroticism3 = request.form['neuroticism3']
      neuroticism4 = request.form['neuroticism4']
      neuroticism5 = request.form['neuroticism5']
      neuroticism6 = request.form['neuroticism6']
      neuroticism7 = request.form['neuroticism7']
      neuroticism8 = request.form['neuroticism8']
      neuroticism9 = request.form['neuroticism9']
      neuroticism10 = request.form['neuroticism10']
      conscientiousness1 = request.form['conscientiousness1']
      conscientiousness2 = request.form['conscientiousness2']
      conscientiousness3 = request.form['conscientiousness3']
      conscientiousness4 = request.form['conscientiousness4']
      conscientiousness5 = request.form['conscientiousness5']
      conscientiousness6 = request.form['conscientiousness6']
      conscientiousness7 = request.form['conscientiousness7']
      conscientiousness8 = request.form['conscientiousness8']
      conscientiousness9 = request.form['conscientiousness9']
      conscientiousness10 = request.form['conscientiousness10']
      agreeableness1 = request.form['agreeableness1']
      agreeableness2 = request.form['agreeableness2']
      agreeableness3 = request.form['agreeableness3']
      agreeableness4 = request.form['agreeableness4']
      agreeableness5 = request.form['agreeableness5']
      agreeableness6 = request.form['agreeableness6']
      agreeableness7 = request.form['agreeableness7']
      agreeableness8 = request.form['agreeableness8']
      agreeableness9 = request.form['agreeableness9']
      agreeableness10 = request.form['agreeableness10']
      extraversion1 = request.form['extraversion1']
      extraversion2 = request.form['extraversion2']
      extraversion3 = request.form['extraversion3']
      extraversion4 = request.form['extraversion4']
      extraversion5 = request.form['extraversion5']
      extraversion6 = request.form['extraversion6']
      extraversion7 = request.form['extraversion7']
      extraversion8 = request.form['extraversion8']
      extraversion9 = request.form['extraversion9']
      extraversion10 = request.form['extraversion10']
      result = np.array([gender_no, age, openness1,openness2,openness3,openness4,openness5,openness6,openness7,openness8,openness9,openness10,neuroticism1,neuroticism2,neuroticism3,neuroticism4,neuroticism5,neuroticism6,neuroticism7,neuroticism8,neuroticism9,neuroticism10, conscientiousness1,conscientiousness2,conscientiousness3,conscientiousness4,conscientiousness5,conscientiousness6,conscientiousness7,conscientiousness8,conscientiousness9,conscientiousness10, agreeableness1,agreeableness2,agreeableness3,agreeableness4,agreeableness5,agreeableness6,agreeableness7,agreeableness8,agreeableness9,agreeableness10, extraversion1,extraversion2,extraversion3,extraversion4,extraversion5,extraversion6,extraversion7,extraversion8,extraversion9,extraversion10], ndmin = 2)
      final = scaler.fit_transform(result)
      personality = str(model.predict(final)[0])
      print(personality)
     
      return render_template('openness_q2.html',answer = personality)

  return render_template('questions.html')

@app.route('/question2', methods =['GET', 'POST'])
def question2():  
    return render_template('openness_q2.html')

@app.route('/que2', methods =['GET', 'POST'])
def que2():
    
    if request.method == 'POST':
        openness1 = request.form['openness1']
        openness2 = request.form['openness2']
        openness3 = request.form['openness3']
        openness4 = request.form['openness4']
        openness5 = request.form['openness5']
        openness6 = request.form['openness6']
        openness7 = request.form['openness7']
        openness8 = request.form['openness8']
        openness9 = request.form['openness9']
        openness10 = request.form['openness10']
        print(openness1)
        with mysql.connector.connect(user="redblack", password="Server@1", host="test-for-python.mysql.database.azure.com", port=3306, database="personality_predict", ssl_ca="{ca-cert filename}", ssl_disabled=False) as con:
            cur = con.cursor()
            cur.execute('''INSERT INTO  questionery (op1 , op2 , op3 , op4 , op5, op6, op7, op8, op9, op10 ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(openness1,openness2, openness3,openness4,openness5,openness6,openness7,openness8,openness9,openness10))

            con.commit()
            msg = "record added successfully"
    

        return render_template('que3.html')

    return render_template('que2.html')

@app.route('/que3', methods =['GET', 'POST'])
def que3():
    if request.method == 'POST':
        conscientiousness1 = request.form['conscientiousness1']
        conscientiousness2 = request.form['conscientiousness2']
        conscientiousness3 = request.form['conscientiousness3']
        conscientiousness4 = request.form['conscientiousness4']
        conscientiousness5 = request.form['conscientiousness5']
        conscientiousness6 = request.form['conscientiousness6']
        conscientiousness7 = request.form['conscientiousness7']
        conscientiousness8 = request.form['conscientiousness8']
        conscientiousness9 = request.form['conscientiousness9']
        conscientiousness10 = request.form['conscientiousness10']
     
        with mysql.connector.connect(user="redblack", password="Server@1", host="test-for-python.mysql.database.azure.com", port=3306, database="personality_predict", ssl_ca="{ca-cert filename}", ssl_disabled=False) as con:
            cur = con.cursor()
            # cur.execute("INSERT INTO  questionery (ne1  , ne2 , ne3  , ne4 , ne5  ) VALUES (%s,%s,%s,%s,%s)",(neuroticism1,neuroticism2, neuroticism3,neuroticism4,neuroticism5))
                 
            query = '''UPDATE questionery SET con1 = %s , con2= %s , con3  = %s, con4 = %s , con5  = %s, con6 = %s , con7 = %s , con8  = %s, con9 = %s , con10  = %s WHERE id = %s'''
            cur.execute('''SELECT MAX(id) FROM questionery''')

# Fetch the result
            result = cur.fetchone()
            max_id = result[0] if result[0] is not None else 0
            print("Max ID:", max_id)
            aa = (conscientiousness1,conscientiousness2,conscientiousness3,conscientiousness4,conscientiousness5,conscientiousness6,conscientiousness7,conscientiousness8,conscientiousness9,conscientiousness10,max_id)
            cur.execute(query, aa)

            con.commit()
            msg = "record added successfully"

        return render_template('que4.html')
    
    return render_template('que3.html')

@app.route('/que4', methods =['GET', 'POST'])
def que4():
    if request.method == 'POST':
        extraversion1 = request.form['extraversion1']
        extraversion2 = request.form['extraversion2']
        extraversion3 = request.form['extraversion3']
        extraversion4 = request.form['extraversion4']
        extraversion5 = request.form['extraversion5']
        extraversion6 = request.form['extraversion6']
        extraversion7 = request.form['extraversion7']
        extraversion8 = request.form['extraversion8']
        extraversion9 = request.form['extraversion9']
        extraversion10 = request.form['extraversion10']
      
        with mysql.connector.connect(user="redblack", password="Server@1", host="test-for-python.mysql.database.azure.com", port=3306, database="personality_predict", ssl_ca="{ca-cert filename}", ssl_disabled=False) as con:
            cur = con.cursor()
            # cur.execute("INSERT INTO  questionery (ne1  , ne2 , ne3  , ne4 , ne5  ) VALUES (%s,%s,%s,%s,%s)",(neuroticism1,neuroticism2, neuroticism3,neuroticism4,neuroticism5))
                 
            query = '''UPDATE questionery SET ext1 = %s , ext2= %s , ext3  = %s, ext4 = %s , ext5  = %s, ext6 = %s , ext7 = %s , ext8  = %s, ext9 = %s , ext10  = %s WHERE id = %s'''
            cur.execute('''SELECT MAX(id) FROM questionery''')

# Fetch the result
            result = cur.fetchone()
            max_id = result[0] if result[0] is not None else 0
            print("Max ID:", max_id)
            aa = (extraversion1,extraversion2,extraversion3,extraversion4,extraversion5,extraversion6,extraversion7,extraversion8,extraversion9,extraversion10,max_id)
            cur.execute(query, aa)

            con.commit()
            msg = "record added successfully"

        return render_template('que5.html')

    
    return render_template('que4.html')

@app.route('/que5', methods =['GET', 'POST'])
def que5():
    if request.method == 'POST':
        agreeableness1 = request.form['agreeableness1']
        agreeableness2 = request.form['agreeableness2']
        agreeableness3 = request.form['agreeableness3']
        agreeableness4 = request.form['agreeableness4']
        agreeableness5 = request.form['agreeableness5']
        agreeableness6 = request.form['agreeableness6']
        agreeableness7 = request.form['agreeableness7']
        agreeableness8 = request.form['agreeableness8']
        agreeableness9 = request.form['agreeableness9']
        agreeableness10 = request.form['agreeableness10']
      
        with mysql.connector.connect(user="redblack", password="Server@1", host="test-for-python.mysql.database.azure.com", port=3306, database="personality_predict", ssl_ca="{ca-cert filename}", ssl_disabled=False) as con:
            cur = con.cursor()
            # cur.execute("INSERT INTO  questionery (ne1  , ne2 , ne3  , ne4 , ne5  ) VALUES (%s,%s,%s,%s,%s)",(neuroticism1,neuroticism2, neuroticism3,neuroticism4,neuroticism5))
                 
            query = '''UPDATE questionery SET agr1 = %s , agr2= %s , agr3  = %s, agr4 = %s , agr5  = %s, agr6 = %s , agr7 = %s , agr8  = %s, agr9 = %s , agr10  = %s WHERE id = %s'''
            cur.execute('''SELECT MAX(id) FROM questionery''')

# Fetch the result
            result = cur.fetchone()
            max_id = result[0] if result[0] is not None else 0
            print("Max ID:", max_id)
            aa = (agreeableness1,agreeableness2,agreeableness3,agreeableness4,agreeableness5,agreeableness6,agreeableness7,agreeableness8,agreeableness9,agreeableness10,max_id)
            cur.execute(query, aa)

            con.commit()
            msg = "record added successfully"

        return render_template('que6.html')
    
    return render_template('que5.html')

@app.route('/que6', methods =['GET', 'POST'])
def que6():
    if request.method == 'POST':
        neuroticism1 = request.form['neuroticism1']
        neuroticism2 = request.form['neuroticism2']
        neuroticism3 = request.form['neuroticism3']
        neuroticism4 = request.form['neuroticism4']
        neuroticism5 = request.form['neuroticism5']
        neuroticism6 = request.form['neuroticism6']
        neuroticism7 = request.form['neuroticism7']
        neuroticism8 = request.form['neuroticism8']
        neuroticism9 = request.form['neuroticism9']
        neuroticism10 = request.form['neuroticism10']
      
      
        with mysql.connector.connect(user="redblack", password="Server@1", host="test-for-python.mysql.database.azure.com", port=3306, database="personality_predict", ssl_ca="{ca-cert filename}", ssl_disabled=False) as con:
            cur = con.cursor()
            # cur.execute("INSERT INTO  questionery (ne1  , ne2 , ne3  , ne4 , ne5  ) VALUES (%s,%s,%s,%s,%s)",(neuroticism1,neuroticism2, neuroticism3,neuroticism4,neuroticism5))
                 
            query = '''UPDATE questionery SET ne1 = %s , ne2= %s , ne3  = %s, ne4 = %s , ne5  = %s, ne6 = %s , ne7= %s , ne8  = %s, ne9 = %s , ne10  = %s WHERE id = %s'''
            cur.execute('''SELECT MAX(id) FROM questionery''')

# Fetch the result
            result = cur.fetchone()
            max_id = result[0] if result[0] is not None else 0
            print("Max ID:", max_id)
            aa = (neuroticism1,neuroticism2,neuroticism3,neuroticism4,neuroticism5,neuroticism6,neuroticism7,neuroticism8,neuroticism9,neuroticism10,max_id)
            cur.execute(query, aa)

            con.commit()
            msg = "record added successfully"

            import random

            items = ["serious", "agreeableness", "lively", "responsible", "dependable", "extraverted","responsible"]
            random_item = random.choice(items)
            print(random_item)

        
        return render_template('openness_q2.html', answer1 = random_item)

    return render_template('que6.html')


    
if __name__ == "__main__":
    app.run(debug=True, port=5000)