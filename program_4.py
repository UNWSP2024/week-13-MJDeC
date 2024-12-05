import sqlite3

#define main function
def main():
    #connect to database
    connection=sqlite3.connect('entries.db')
    #get cursor
    cursor=connection.cursor()
    #add entries table
    entries_table(cursor)
    #commit changes and close connection
    connection.commit()
    connection.close()


def entries_table(cursor):
    #if table exists drop table
    cursor.execute('DROP TABLE IF EXISTS Entries')

    #create table
    cursor.execute('''CREATE TABLE Entries (EntriesID INTEGER PRIMARY KEY NOT NULL,Name TEXT,Number BLOB)''')

#add rows to phonebook table
    entries_pop = [(1,'Bigmus Cles','000-430-0544'),
                  (2,'Inp Ain','123-456-789'),
                  (3,'Pointle Sswaste','999-999-99'),
                  (4,'Anno Yed','234-456-633'),
                  (5,'Revo Lution','1-444-234-999')]
    cursor.executemany("insert into entries values (?,?,?)", entries_pop)

    #selects value from database
    cont1='y'
    while cont1=='y':
        select=input("Enter first and last name of person whose phone number you would like to view:")
        cursor.execute("select * from Entries where name=:c",{"c":select})
        name_search=cursor.fetchall()
        print(name_search)
        cont1=input("Would you like to search more names? Press y for yes or another key to continue.")
        
    
    
    #inserts new value into database
    name=input("Enter the name of person you would like to add to database:")
    number=input("Enter their phone number:")
    cursor.execute('''INSERT INTO Entries (name,number) VALUES (?,?)''',(name,number))
    #deletes value of choice from database
    delent=int(input("Enter the ID of the person to delete:"))
    cursor.execute('''DELETE FROM Entries Where EntriesID==?''',(delent,))

    #prints all values in database
    print("Here are the current contents of the database:")
    for row in cursor.execute("select * from entries"):
        print(row)
        
    
   

if __name__ == '__main__':
    main()
