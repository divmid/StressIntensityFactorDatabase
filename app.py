import bisect
import traceback

from flask import request, jsonify, render_template

from model import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

sql_index_list = (
    0,
    0.05,
    0.10,
    0.15,
    0.20,
    0.25,
    0.30,
    0.35,
    0.40,
    0.45,
    0.50,
    0.55,
    0.60,
    0.65,
    0.70,
    0.75,
    0.80,
    0.85,
    0.90,
    0.95,
)


@app.route('/')
@app.route('/index')
def index():
    print(request.args)
    print(request.data)
    print(request.form)
    return render_template('index.html')


@app.route('/test', methods=["GET", "POST"])
def test():
    print("aaaaaaa", request.args)
    print("aaaaaaa", request.args.get("crack_type"))
    print(request.data)
    print(request.form)
    return render_template('index.html')


@app.route('/sitf')
def getsiftable():
    """
    crack_type: 裂纹模式
    a1:
    a2:
    d:
    a1[0,20],a2[0,40],d(0.0-100.0]
    :return:
    """
    message = {"code": 400}
    try:
        crack_type = float(request.args.get('crack_type'))
        a1 = int(request.args.get('a1'))
        a2 = int(request.args.get('a2'))
        d = int(request.args.get('d'))
        if not (0 <= a1 <= 20):
            message["msg"] = "参数异常: 0<= a1<=20"
            return jsonify(message)
        if not (0 < a2 <= 40):
            message["msg"] = "参数异常: 0<= a2<=40"
            return jsonify(message)
        if not (0 < d <= 100):
            message["msg"] = "参数异常: 0< d <=100"
            return jsonify(message)
        q = (a1 + a2) / d
        if not (0 <= q <= 0.9):
            message["msg"] = "参数异常: 0< d <=100"
            return jsonify(message)
        left_index = bisect.bisect_left(sql_index_list, q)
        right_index = bisect.bisect_right(sql_index_list, q)
        left_val = sql_index_list[left_index]
        if q == left_val:
            index = left_index
        elif right_index > len(sql_index_list):
            index = left_index
        else:
            index = right_index

        a = a1 / a2
        if crack_type == 1:
            if a == 0:
                DBtable = Sifator1
            elif a == 10:
                DBtable = Sifator2
            elif a == 20:
                DBtable = Sifator3
            else:
                message["msg"] = "参数异常: a1/a2 0 10 20"
                return jsonify(message)
        elif crack_type == 2:
            if a == 0:
                DBtable = Sifator4
            elif a == 10:
                DBtable = Sifator5
            elif a == 20:
                DBtable = Sifator6
            else:
                message["msg"] = "参数异常: a1/a2 0 10 20"
                return jsonify(message)
        elif crack_type == 3:
            if a == 11:
                DBtable = Sifator7
            elif a == 3:
                DBtable = Sifator8
            elif a == 5:
                DBtable = Sifator9
            else:
                message["msg"] = "参数异常: a1/a2 11 3 5"
                return jsonify(message)
        else:
            message["msg"] = "参数异常:crack_type 1 2 3"
            return jsonify(message)

        sitf = DBtable.query.filter_by(q=sql_index_list[index]).first()
        print(sitf.F)
        message["q"] = q
        message["a"] = a
        message["F"] = sitf.F
        message["k"] = sitf.F * ((3.14 * a1) * 0.5)
        message['code'] = 200
    except Exception as e:
        print(traceback.print_exc())
        message["msg"] = "参数异常"

    return jsonify(message)


if __name__ == '__main__':
    # port是可修改的端口，启动之后是本机ip
    app.run(host="0.0.0.0", port="5000", debug=True)
