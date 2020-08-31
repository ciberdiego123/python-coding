import ibm_db
conn = ibm_db.connect("DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-lon02-04.services.eu-gb.bluemix.net;PORT=50001;PROTOCOL=TCPIP;"
                      "UID=jcc52892;PWD=71l@td4cxfqxwgjn;Security=SSL;", "", "")
sql = "SELECT * FROM EMPLOYEES"
stmt = ibm_db.exec_immediate(conn, sql)
dictionary = ibm_db.fetch_both(stmt)
c = 1
while dictionary:
    print('Employee '+str(c)+':')
    print("The ID is : ",  dictionary["EMP_ID"])
    print("The Name is : ", dictionary[1]+' '+dictionary[2])
    dictionary = ibm_db.fetch_both(stmt)
    c += 1
