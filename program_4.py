
def add_phonebook_table(cursor):
    #if table exists drop table
    cursor.execute('DROP TABLE IF EXISTS Entries')

    #create table
    cursor.execute('''CREATE TABLE Entries (CityID INTEGER PRIMARY KEY NOT NULL,Name TEXT,Number Integer)''')

#add rows to phonebook table
    phonebook_pop = [(1,'Micah DeCaro',6514300544)]
    cursor.executemany("insert into phonebook values (?,?,?)", entries)
