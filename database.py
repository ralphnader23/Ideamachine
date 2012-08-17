
import sqlite3



def main():

    conn = sqlite3.connect('example.db')

    c = conn.cursor()

    c.execute('''DROP TABLE contacts''')

    c.execute('''CREATE TABLE contacts 
             (name, age)''')



    purchases = [('Jessie', '26'),
                ('Brett', '25'),
                ('Mike', '22')
                ]

    c.executemany('INSERT INTO contacts VALUES (?,?)', purchases)
    

    for row in c.execute('SELECT * FROM contacts'):
        print(row)



    conn.commit()

    # We can also close the cursor if we are done with it
    c.close()





if __name__ == '__main__':
    main()
