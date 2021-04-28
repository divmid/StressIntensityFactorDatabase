from flask import Flask, request, jsonify, render_template
import bisect
import traceback
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)



class Siftable(db.Model):
    __tablename__ = 'siftable'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    k = db.Column(db.FLOAT())
    F = db.Column(db.FLOAT())


sql_dict = {
    0: 1.000,
    0.05: 1.012,
    0.10: 1.023,
    0.15: 1.030,
    0.20: 1.033,
    0.25: 1.042,
    0.30: 1.051,
    0.35: 1.072,
    0.40: 1.088,
    0.45: 1.128,
    0.50: 1.152,
    0.55: 1.212,
    0.60: 1.243,
    0.65: 1.332,
    0.70: 1.384,
    0.75: 1.486,
    0.80: 1.638,
    0.85: 1.867,
    0.90: 2.178,
    0.95: 2.278,
}


@app.route('/')
@app.route('/index')
def index():
    print(request.args)
    print(request.data)
    print(request.form)
    return render_template('index.html')

@app.route('/test', methods=["GET", "POST"])
def test():
    print(request.args)
    print(request.data)
    print(request.form)
    return render_template('index.html')

@app.route('/sitf')
def getsiftable():
    message = {"code": 400}
    try:
        k = float(request.args.get('k'))
        print(k)
        if k < 0 or k > 0.95:
            message["msg"] = "参数异常"
            return jsonify(message)
        sql_list = list(sql_dict.keys())
        left_index = bisect.bisect_left(sql_list, k)
        right_index = bisect.bisect_right(sql_list, k)
        left_val = sql_list[left_index]
        if k == left_val:
            index = left_index
        elif right_index > len(sql_list):
            index = left_index
        else:
            index = right_index
        sitf = Siftable.query.filter_by(k=sql_list[index]).first()
        print(sitf.F)
        message["F"] = sitf.F
        message['code'] = 200
    except Exception as e:
        print(traceback.print_exc())
        message["msg"] = "参数异常"

    return jsonify(message)


if __name__ == '__main__':
    # port是可修改的端口，启动之后是本机ip
    app.run(host="0.0.0.0", port="5001")


