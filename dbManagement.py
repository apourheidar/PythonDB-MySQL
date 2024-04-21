import mysql.connector
dbName="mydatabase44"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE "+dbName)

#mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mycursor.close()
mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute("SELECT * FROM customers WHERE address ='Park Lane 38'")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()
print (sql)
for x in myresult:
  print(x)

mycursor.close()
mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print(sql)
for x in myresult:
  print(x)
mycursor.close()
mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

mycursor.close()
mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

mycursor.close()
mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)
print(sql)
mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("SHOW TABLES")


mycursor.close()
mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

mycursor.close()
mydb.close()



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()
print(sql)
print(mycursor.rowcount, "record(s) affected")


mycursor.close()
mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()
print(sql)
for x in myresult:
  print(x)


mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav VARCHAR(255))")
#mycursor.execute("SHOW TABLES")


mycursor.close()
mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()
sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
val = [('John', '154'),('Peter','154'),('Amy','155'),('Hannah','155'),('Michael','156')]


mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE products (ids VARCHAR(255) , name VARCHAR(255))")
#mycursor.execute("SHOW TABLES")


mycursor.close()
mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()
sql = "INSERT INTO products (ids,name) VALUES (%s,%s)"
val = [( '154','Chocolate Heaven'),('155','Tasty Lemons'),('156','Vanilla Dreams')]


mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

mycursor.close()
mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.ids"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print(sql)
for x in myresult:
  print(x)


mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"


print(sql)
for x in myresult:
  print(x)


mycursor.close()
mydb.close()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567",
  database=dbName
)
mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"


print(sql)
for x in myresult:
  print(x)


mycursor.close()
mydb.close()
