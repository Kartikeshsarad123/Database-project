import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='kartik123',database='bookstoredb')
curs=con.cursor()


try:
  nm=int(input("enter the bookcode"))
  curs.execute("select * from books where bookcode=%d" %nm)
  data=curs.fetchone()
  print(data)

except:
    print('books not found')

con.close()      
