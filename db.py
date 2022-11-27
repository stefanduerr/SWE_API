import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_tables():
    connection_obj = sqlite3.connect(r"C:\Users\xpara\SWE_API\db\pythonsqlite.db")
    
    # cursor object
    cursor_obj = connection_obj.cursor()
    
    # Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS CUSTOMERS")
    
    # Creating table
    table_customer = """ CREATE TABLE CUSTOMERS (
                First_Name VARCHAR(25) NOT NULL,
                Last_Name VARCHAR(25) NOT NULL,
                Address VARCHAR(50),
                Postal_Code VARCHAR(10),
                Date_Of_Birth DATE,
                Email VARCHAR(255) NOT NULL,
                Status VARCHAR(10)            
            ); """
    
    # Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS PRODUCTS")
    
    # Creating table
    table_product = """ CREATE TABLE PRODUCTS (
                Name VARCHAR(25) NOT NULL,
                Balance FLOAT,
                Product_Code VARCHAR(10),
                Interest_Rate FLOAT        
            ); """

    cursor_obj.execute(table_customer)
    cursor_obj.execute(table_product)
    connection_obj.commit()
    # cursor_obj.execute(table_product)

    customers = [('Franzl', 'Lang', 'Liebhartsgasse 27', '1160', '1992-11-22', 'franzl@gmx.at', 'online'),
                        ('Alex', 'Kurz', 'Liebhartsgasse 27', '1160', '1986-10-16', 'Alex@gmx.at', 'away'),
                        ('Mark', 'Huber', 'Liebhartsgasse 27', '1160', '1998-07-29', 'Mark@gmx.at', 'offline'),
                        ('Oliver', 'Kahn', 'Liebhartsgasse 27', '1160', '1999-03-30', 'Oliver@gmx.at', 'away'),
                        ('Joachim', 'Rhabarber', 'Liebhartsgasse 27', '1160', '1997-12-14', 'Joachim@gmx.at', 'offline'),
                        ('Sarah', 'Zichmann', 'Burggasse 27', '1150', '2001-07-02', 'Sarah@gmx.at', 'offline'),
                        ('Annalena', 'Lager', 'Burggasse 27', '1150', '1950-11-25', 'Annalena@gmx.at', 'offline'),
                        ('Maria', 'Robust', 'Burggasse 27', '1150', '1934-01-01', 'Maria@gmx.at', 'online'),
                        ('Hannah', 'Augartner', 'Burggasse 27', '1150', '1960-05-05', 'Hannah@gmx.at', 'online'),
                        ('Julia', 'Legano', 'Burggasse 27', '1150', '1993-12-12', 'Julia@gmx.at', 'away')]

    values = ', '.join(map(str, customers))                      
    cursor_obj.execute("INSERT INTO CUSTOMERS(First_Name, Last_Name, Address, Postal_Code, Date_Of_Birth, Email, Status) VALUES {};".format(values))
    connection_obj.commit()

    products = [('Schwarzbrot', 1.50, '67YZ4T630J', 0.01),
                        ('Apfel', 1.35, 'JFZWIAYWU1', 0.03),
                        ('PlayStation', 399.50, 'VKN78HT4ZW', 0.15),
                        ('Maus', 11.40, '3JMA9CH8DC', 0.02),
                        ('Keyboard', 31.50, 'YT8ZGMWTXJ', 0.12)]

    values = ', '.join(map(str, products))                      
    cursor_obj.execute("INSERT INTO PRODUCTS(Name, Balance, Product_Code, Interest_Rate) VALUES {};".format(values))
    connection_obj.commit()    

    # cursor_obj.execute(Insert_product) 

    print("Table is Ready")
    connection_obj.close()

def get_list():
    connection_obj = sqlite3.connect(r"C:\Users\xpara\SWE_API\db\pythonsqlite.db")
    
    # cursor object
    cursor_obj = connection_obj.cursor()
    
    # Drop the GEEK table if already exists.
    cursor_obj.execute("SELECT * FROM CUSTOMERS;")
    rows = cursor_obj.fetchall()
    arr = []

    for row in rows:
        arr.append(row)

    return arr




# def insert_test_data():
#     connection_obj = sqlite3.connect('pythonsqlite.db')
#     cursor_obj = connection_obj.cursor()

#     Insert_customer = """ INSERT INTO CUSTOMERS
#                             (First_Name, Last_Name, Address, Postal_Code, Date_Of_Birth, Email, Status)
#                         VALUES
#                             (Franzl, Lang, Burggasse_27, 1150, 1993-12-12, franzl@gmx.at, online),
#                             (Alex, Kurz, Burggasse_27, 1150, 1993-12-12, Alex@gmx.at, away),
#                             (Mark, Huber, Burggasse_27, 1150, 1993-12-12, Mark@gmx.at, offline),
#                             (Oliver, Kahn, Burggasse_27, 1150, 1993-12-12, Oliver@gmx.at, away),
#                             (Joachim, Rhabarber, Burggasse_27, 1150, 1993-12-12, Joachim@gmx.at, offline),
#                             (Sarah, Zichmann, Burggasse_27, 1150, 1993-12-12, Sarah@gmx.at, offline),
#                             (Annalena, Lager, Burggasse_27, 1150, 1993-12-12, Annalena@gmx.at, offline),
#                             (Maria, Robust, Burggasse_27, 1150, 1993-12-12, Maria@gmx.at, online),
#                             (Hannah, Augartner, Burggasse_27, 1150, 1993-12-12, Hannah@gmx.at, online),
#                             (Julia, Legano, Burggasse_27, 1150, 1993-12-12, Julia@gmx.at, away); """

#     Insert_product = """ INSERT INTO PRODUCTS
#                             (Name, Balance, Product_Code, Interest_Rate)
#                         VALUES
#                             (Schwarzbrot, 1.50, 67YZ4T630J, 0.01),
#                             (Apfel, 1.35, JFZWIAYWU1, 0.03),
#                             (PlayStation, 399.50, VKN78HT4ZW, 0.15),
#                             (Maus, 11.40, 3JMA9CH8DC, 0.02),
#                             (Keyboard, 31.50, YT8ZGMWTXJ, 0.12); """    

#     # cursor_obj.execute(Insert_customer)

#     customers = [('Franzl', 'Lang', 'Burggasse_27', '1150', '1993-12-12', 'franzl@gmx.at', 'online'),
#                         ('Alex', 'Kurz', 'Burggasse_27', '1150', '1993-12-12', 'Alex@gmx.at', 'away'),
#                         ('Mark', 'Huber', 'Burggasse_27', '1150', '1993-12-12', 'Mark@gmx.at', 'offline'),
#                         ('Oliver', 'Kahn', 'Burggasse_27', '1150', '1993-12-12', 'Oliver@gmx.at', 'away'),
#                         ('Joachim', 'Rhabarber', 'Burggasse_27', '1150', '1993-12-12', 'Joachim@gmx.at', 'offline'),
#                         ('Sarah', 'Zichmann', 'Burggasse_27', '1150', '1993-12-12', 'Sarah@gmx.at', 'offline'),
#                         ('Annalena', 'Lager', 'Burggasse_27', '1150', '1993-12-12', 'Annalena@gmx.at', 'offline'),
#                         ('Maria', 'Robust', 'Burggasse_27', '1150', '1993-12-12', 'Maria@gmx.at', 'online'),
#                         ('Hannah', 'Augartner', 'Burggasse_27', '1150', '1993-12-12', 'Hannah@gmx.at', 'online'),
#                         ('Julia', 'Legano', 'Burggasse_27', '1150', '1993-12-12', 'Julia@gmx.at', 'away')]
#     values = ', '.join(map(str, customers))                      
#     cursor_obj.executemany("INSERT INTO CUSTOMERS(First_Name, Last_Name, Address, Postal_Code, Date_Of_Birth, Email, Status) VALUES {};".format(values))

#     # cursor_obj.execute(Insert_product)   
#     connection_obj.close() 



# names = ["apple", "banana", "cherry"]



# cursor.execute("INSERT INTO barcodes(barcode) VALUES ('{}');".format(names))