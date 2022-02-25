import pymysql
# 연결자 만들기
conn = pymysql.connect(host="localhost", user="secret", password="secret", db="soloDB", charset="utf8")

# 커서(통로) 만들기
# SQL문 사용할 때 커서이름.execute()
cur = conn.cursor()

# 테이블 만들기
# char 공백 채움 varchar 공백 안 채움(권장)
cur.execute("CREATE TABLE IF NOT EXISTS userTable (id varchar(4), userName varchar(15), email varchar(20), birthYear int);")

# 데이터 입력하기(임시로 저장됨)
# "" '' 주의!
cur.execute('INSERT INTO userTable VALUES("one", "오도원", "dhehdnjs@naver.com", 1997);')
cur.execute('INSERT INTO userTable VALUES("two", "오도투", "dhehdnjs2@naver.com", 1997);')
cur.execute('INSERT INTO userTable VALUES("th", "오도쓰리", "dhehdnjs3@naver.com", 1997);')

# 임시로 저장된 데이터 확실하게 저장하기
conn.commit()

# 연결한 데이터베이스 닫기
# 큰 차이가 없지만 하는 걸 권장
conn.close()