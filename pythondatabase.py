import mysql.connector as con
mydb = con.connect(
        host= "localhost", user ="root", database="python",password = "password2$"
    )

#1. connect
#2. cursor()
#3. execute()
mydata = mydb.cursor()
sql ="SELECT * FROM python1"
mydata.execute(sql)

print("ID",'\t',"NAME",'\t',"Address",'\t', "Password",'\t', )
for i in mydata:
    print("-----------------------------------------------------")
    print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])
