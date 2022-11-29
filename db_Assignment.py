import sqlite3

# Open connection to the database or create it if it does not exist
conn = sqlite3.connect('myDB.db')

# Using database connection
with conn:
    # Create a cursor
    cur = conn.cursor()
    # Execute SQL command
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_blank( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    conn.commit() # Commit the changes
conn.close() # Close database connection

conn = sqlite3.connect('myDB.db')

with conn:
    # Creating a tuple
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
    cur = conn.cursor()
    # Inserting each document name into fileList tuple
    for fname in fileList:
        cur.execute("INSERT INTO tbl_blank(col_fname) VALUES (?)",(fname,))
        conn.commit()
conn.close()

conn = sqlite3.connect('myDB.db')

with conn:
    cur = conn.cursor()
    # Selecting file names that end with .txt
    cur.execute("SELECT col_fname FROM tbl_blank WHERE col_fname LIKE '%.txt'")
    # Storing each file name returned from above SQL statement to varTxtFiles
    varTxtFiles = cur.fetchall()
    # Creating a single tuple to be printed later
    myTuple = ()
    i = 0 # Increment variable
    # While i is less than the length of varTxtFiles take each and add it to myTuple
    while i < len(varTxtFiles):
        myTuple += (varTxtFiles[i],)
        i += 1
    print(myTuple) # Print myTuple to the console
conn.close()
