import mysql.connector

auth_db = { # authorize to database.
    'host': 'localhost',
    'user': 'pauls',
    'password': 'Udens123!',
    'database': 'rng_base',
}

connection = mysql.connector.connect(**auth_db) # connect to db
cursor = connection.cursor()
# table query.
create_table_query = ''' 
CREATE TABLE IF NOT EXISTS rngtable (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    `random_number` int DEFAULT NULL
)
'''

cursor.execute(create_table_query) # run the query.

connection.commit() # commit changes and close connection.
connection.close()

print("Migrated.") # console output to show something happening.
