
def add_cities_table(cursor):
    #if table exists drop table
    cursor.execute('DROP TABLE IF EXISTS Cities')

    #create table
    cursor.execute('''CREATE TABLE Entries (CityID INTEGER PRIMARY KEY NOT NULL,CityName TEXT,Population REAL)''')

#add rows to phonebook table
    phonebook_pop = [(1,'Micah DeCaro',6514300544)]
    cursor.executemany("insert into phonebook values (?,?,?)", entries)
