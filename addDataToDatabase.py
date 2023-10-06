import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facialrecgrealtime-default-rtdb.firebaseio.com/"
})

ref = db.reference('students')

data = {
    '1211':
        {
            "name": "Vinay Parle",
            "major": "AI\ML",
            "joining_year": 2022,
            "total_attendance": 14,
            "last_attendance_time": "2023-09-09 00:53:01"

        },
    '1222':
        {
            "name": "Priyanshi Agarwal",
            "major": "Graphic Design",
            "joining_year": 2021,
            "total_attendance": 4,
            "last_attendance_time": "2023-04-21 02:10:01"

        },
    '1233':
        {
            "name": "Dhananjay Sharma ",
            "major": "MCA",
            "joining_year": 2023,
            "total_attendance": 7,
            "last_attendance_time": "2023-07-09 04:53:01"

        }
}

for key, value in data.items():
    ref.child(key).set(value)
# c=15
# a=15.2
# b="abc"
# print(type(c))
# print(type(a))
# print(type(b))
