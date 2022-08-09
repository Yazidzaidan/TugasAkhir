import pyrebase

firebaseConfig={"apiKey": "AIzaSyDubuVKj7XYrnp3yX3x5YPFfX-m8z0GEPU",
  "authDomain": "pyrebaserealtime-example.firebaseapp.com",
  "databaseURL": "https://pyrebaserealtime-example-default-rtdb.firebaseio.com",
  "projectId": "pyrebaserealtime-example",
  "storageBucket": "pyrebaserealtime-example.appspot.com",
  "messagingSenderId": "101749055169",
  "appId": "1:101749055169:web:69909934e038b47fa63e40",
  "measurementId": "G-TXX3Y2YDRJ"}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

#Push Data with random branch
# data={"name": "Azhara", "age":22, "addres":["Bukit Rahmah"]}
# db.push(data)

#Branch Value
data={"age":22, "addres":"GBR 2"}
db.child("Yazid").set(data)