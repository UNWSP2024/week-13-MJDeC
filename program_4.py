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
    cursor.execute('''CREATE TABLE Entries (EntriesID INTEGER PRIMARY KEY NOT NULL,Name TEXT,Number Integer)''')

#add rows to phonebook table
    entries_pop = [(1,'Micah DeCaro',6514300544),
                  (2,'Bob Bobbson',123456),
                  (3,'Brandon Sanderson',99999999),
                  (4,'Steve Jobs',234566)]
    cursor.executemany("insert into entries values (?,?,?)", entries_pop)
    #for row in cursor.execute("select * from entries"):
        #print(row)
    cursor.execute("select * from entries where name=:n",{"n":"Micah DeCaro"})
    name_search=cursor.fetchall()
    print(name_search)

if __name__ == '__main__':
    main()
