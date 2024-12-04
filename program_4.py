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
    cursor.execute('''CREATE TABLE Entries (CityID INTEGER PRIMARY KEY NOT NULL,Name TEXT,Number Integer)''')

#add rows to phonebook table
    entries_pop = [(1,'Micah DeCaro',6514300544)]
    cursor.executemany("insert into entries values (?,?,?)", entries)
    for row in cursor.execute("select * from entries"):
        print(row)

if __name__ == '__main__':
    main()
