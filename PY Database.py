import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE pythondb")
mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), contact VARCHAR(255), email VARCHAR(255))")


sql = "INSERT INTO student (name, address, contact, email) VALUES (%s, %s, %s, %s)"

val = ("ABC", "MUMBAI","9999999999","abc@db.com")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

val = ("XYZ", "Delhi","8888888888","xyz@db.com")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")


mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

sql = "SELECT * FROM customers WHERE address ='Delhi'"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

sql = "DROP TABLE customers"
mycursor.execute(sql)
