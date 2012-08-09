
import sqlite3



def main():

    conn = sqlite3.connect('example.db')

    c = conn.cursor()

    c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')


    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                ]

    c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
    

    for row in c.execute('SELECT * FROM stocks'):
        print(row)


    c.execute('DROP TABLE stocks')

    conn.commit()

    # We can also close the cursor if we are done with it
    c.close()





if __name__ == '__main__':
    main()
