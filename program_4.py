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
    entries_pop = [(1,'Micah DeCaro','651-430-0544'),
                  (2,'Inp Ain','123-456'),
                  (3,'Pointle Sswaste','999-999-99'),
                  (4,'Anno Yed','23-456-6')]
    cursor.executemany("insert into entries values (?,?,?)", entries_pop)

    #inserts new value into database
    name=input("Enter name:")
    number=input("Enter phone number with no dashes or spaces:")
    cursor.execute('''INSERT INTO Entries (name,number) VALUES (?,?)''',(name,number))
    #deletes value of choice from database
    delent=int(input("Enter the ID of the phone number to delete:"))
    cursor.execute('''DELETE FROM Entries Where EntriesID==?''',(delent,))

    #prints all values in database
    print("Here are the current contents of the database:")
    for row in cursor.execute("select * from entries"):
        print(row)
        
    
    #selects specific value from database
    cursor.execute("select * from entries where name=:n",{"n":"Micah DeCaro"})
    name_search=cursor.fetchall()
    print(name_search)

if __name__ == '__main__':
    main()
