import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='kartik123',database='bookstoredb')
curs=con.cursor()
nm=int(input("enter the bookcode "))
curs.execute("select * from books where bookcode=%d" %nm)
data=curs.fetchall()
print(data)
try:
    ns=input("do you want to delete the data ")
    if ns=="yes" :
        curs.execute("delete from books where bookcode=%d" %nm)
        con.commit()
        print("data deleted successfully")
    else :
        print("thank you")

except:
    print("invalid bookcode")



con.close()
