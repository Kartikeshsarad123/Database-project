import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='kartik123',database='bookstoredb')
curs=con.cursor()
curs.execute("select bookname from books")
data=curs.fetchall()
print(data)
con.close()