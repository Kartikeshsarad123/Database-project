import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='kartik123',database='bookstoredb')
curs=con.cursor()
ns=input("enter the author ")
ns1=input("enter the publication ")
curs.execute("select * from books where author='%s' AND publication='%s'" %(ns,ns1))
data=curs.fetchone()
print(data)
con.close()