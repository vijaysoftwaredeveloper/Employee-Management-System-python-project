import sqlite3


class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS Employees(
        id Integer Primary Key,
        name text,
        age text,
        doj text,
        email text,
        gender text,
        contact text,
        address text
        )
        """
        self.cursor.execute(sql)
        self.connection.commit()

    # INSERT Function...
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cursor.execute("insert into  Employees values(Null,?,?,?,?,?,?,?)",(name,age,doj,email,gender,contact,address))
        self.connection.commit()


    #Fetch all data in db

    def fetch(self):
        self.cursor.execute("SELECT * from Employees")
        rows=self.cursor.fetchall()
        # print(rows)
        return rows

    #delete in record in db
    def remove(self,id):
        self.cursor.execute("delete from Employees where id=?",(id,))
        self.connection.commit()

    #update record in db.
    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cursor.execute("update   Employees set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?",
                            (name, age, doj, email, gender, contact, address,id))
        self.connection.commit()










# o = Database("Employees.db")
# # o.insert("sam","30df","20-10-24","sam@gmail.com","male","123456789","CHENNAI")
# # o.fetch()
# o.update("2","samkumar","32","12-10-24","samkumar@gmail.com","male","9080742861","trichy")
#









