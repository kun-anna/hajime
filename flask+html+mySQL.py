from flask import Flask,render_template,request
import pymysql

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template('记录.html')

    a = request.form.get('时间')
    b = request.form.get('地点')
    c = request.form.get('人物')
    d = request.form.get('事件')
    e = request.form.get('补充')
    f = request.form.get('专注')
    g = request.form.get('能量')
    h = request.form.get('心流')

    # 连接MySQL
    conn = pymysql.connect(host='localhost',
                                     port=3306,
                                     user='root',
                                     password='anna0716',
                                     charset='utf8',
                                     db='爱好')
    cursor = conn.cursor()

    # 执行SQL
    sql = "insert into `事件体验记录`(时间,地点,人物,事件,补充,专注,能量,心流) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,[a,b,c,d,e,f,g,h])
    conn.commit()

    # 关闭连接
    cursor.close()
    conn.close()
    return '提交成功'

if __name__ == '__main__':
    app.run()