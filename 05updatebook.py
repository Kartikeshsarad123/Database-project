import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='kartik123',database='bookstoredb')
curs=con.cursor()
try:
 nm=int(input("enter a bookcode "))
 nm1=int(input("enter a price "))
 curs.execute("update books set price=%d where bookcode=%d" %(nm1,nm))
 con.commit()
 print("update book data succesfully")

except:
    print("book does not exist")
con.close()