import pymysql 
db = pymysql.connect('localhost','root','123456','chat')
cursor = db.cursor()
sql='''select * from user where name='liswu' and passwd='123456';'''
cursor.execute(sql)
result_user = cursor.fetchall()
print(result_user)

#print(r1[0][2])
#for line in r1:
#    print(line[1])


