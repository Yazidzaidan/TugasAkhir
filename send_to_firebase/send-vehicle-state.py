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

data={"Height": "100",
    "Distance From Home":"50"+" m",
    "Coordinate": "x"+","+"y",
    "Ground Speed":"15"+" m/s",
    "Vertical Speed":"7"+" m/s"}
db.child("vehicle_state").set(data)