import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};'
                      'Server=GALAXIUSPC\SQLEXPRESS;'
                      'Database=CampusTrader;'
                      'User ID=GALAXIUSPC\\tomha;')
cursor = cnxn.cursor()

print("Please enter your first name: ")
u_firstName = input()

print("Please enter your last name: ")
u_lastName = input()

print("Please enter your email: ")
u_email = input()

try:
    cursor.execute("""insert into users(firstName, lastName, email) values (?,?,?)""", (u_firstName, u_lastName, u_email))
    cnxn.commit()
except pyodbc.IntegrityError as err:
    print("This email is not valid for Campus Trader.")


##cursor.execute('select * from users')

##for i in cursor:
##    print(i)