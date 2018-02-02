import random, string,pymysql

forSelect = string.ascii_letters + string.digits

def generate(count, length):
    # count = 200
    # length = 20
    
    conn=connection()
    params=[]
	
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        print(Re)
        sql="INSERT COUPON(COUPON) VALUES('{0}')"
        exeSql(conn,sql.format(Re))
    close(conn)
		
def connection():
	conn = pymysql.connect(host='172.16.180.155', port=3306,user='root',passwd='admin',db='test',charset='UTF8')
	return conn
	
def close(conn):
	conn.close()
	
def exeSql(conn,sql):
	cur=conn.cursor()
	cur.execute(sql)
	conn.commit()
	cur.close()

if __name__ == "__main__":
	generate(200, 20)

	
