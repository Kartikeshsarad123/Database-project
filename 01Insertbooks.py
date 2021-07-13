import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='kartik123',database='bookstoredb')
curs=con.cursor()
nm=int(input("enter a bookcode "))
ns=input("enter a bookname ")
ns1=input("enter a category ")
ns2=input("enter a author ")
ns3=input("enter a publication ")
ns4=input("enter a edition ")
nm1=int(input("enter a price "))


curs.execute("insert into books value(%d,'%s','%s','%s','%s','%s',%d)"%(nm,ns,ns1,ns2,ns3,ns4,nm1))
con.commit()
print("Books added succesfully")
con.close()