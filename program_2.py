import sqlite3

def main():
    #connect to database
    connection = sqlite3.connect('cities.db')

    #get cursor
    cursor = connection.cursor()
    
    #add cities table
    add_cities_table(cursor)
    #add rows to table
    add_cities(cursor)
    #commit changes
    connection.commit()
    #close connection
    connection.close()

def add_cities_table(cursor):
    #if table exists drop table
    cursor.execute('DROP TABLE IF EXISTS Cities')

    #create table
    cursor.execute('''CREATE TABLE Cities (CityID INTEGER PRIMARY KEY NOT NULL,CityName TEXT,Population REAL)''')

#add 20 rows to cities table
    cities_pop = [(1,'Tokyo',38001000),
                (2,'Delhi',25703168),
                (3,'Shanghai',23740778),
                (4,'Sao Paulo',21066245),
                (5,'Mumbai',21042538),
                (6,'Mexico City',20998543),
                (7,'Beijing',20383994),
                (8,'Osaka',20237645),
                (9,'Cairo',18771769),
                (10,'New York',18593220),
                (11,'Dhaka',17598228),
                (12,'Karachi',16617644),
                (13,'Buenos Aires',15180176),
                (14,'Kolkata',14864919),
                (15,'Istanbul',14163989),
                (16,'Chongqing',13331579),
                (17,'Lagos',13122829),
                (18,'Manila',12946263),
                (19,'Rio de Janeiro',12902306),
                (20,'Guangzhou',12458130)]
    cursor.executemany("insert into cities values (?,?,?)", cities_pop)
    #print contents of cities table
    for row in cursor.execute("select * from cities"):
        print(row)
      
  

#execute main
if __name__ == '__main__':
    main()
