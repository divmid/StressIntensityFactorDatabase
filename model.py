from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Sifator1(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    q = db.Column(db.FLOAT())
    F = db.Column(db.FLOAT())

class Sifator2(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    q = db.Column(db.FLOAT())
    F = db.Column(db.FLOAT())
class Sifator3(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    q = db.Column(db.FLOAT())
    F = db.Column(db.FLOAT())

class Sifator4(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    q = db.Column(db.FLOAT())
    F = db.Column(db.FLOAT())

class Sifator5(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    q = db.Column(db.FLOAT())
    F = db.Column(db.FLOAT())

class Sifator6(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    q = db.Column(db.FLOAT())
    F = db.Column(db.FLOAT())

class Sifator7(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    q = db.Column(db.FLOAT())
    F = db.Column(db.FLOAT())

class Sifator8(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    q = db.Column(db.FLOAT())
    F = db.Column(db.FLOAT())

class Sifator9(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    q = db.Column(db.FLOAT())
    F = db.Column(db.FLOAT())


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    table1 = [(0, 1.0), (0.05, 1.012), (0.1, 1.023), (0.15, 1.03), (0.2, 1.033), (0.25, 1.042), (0.3, 1.051),
              (0.35, 1.072), (0.4, 1.088), (0.45, 1.128), (0.5, 1.152), (0.55, 1.212), (0.6, 1.243), (0.65, 1.332),
              (0.7, 1.384), (0.75, 1.486), (0.8, 1.638), (0.85, 1.867), (0.9, 2.178)]
    table2 = [(0.00, 1.000), (0.05, 1.001), (0.10, 1.002), (0.15, 1.004), (0.20, 1.009), (0.25, 1.022), (0.30, 1.032),
              (0.35, 1.054), (0.40, 1.072), (0.45, 1.108), (0.50, 1.130), (0.55, 1.635), (0.60, 1.195), (0.65, 1.265),
              (0.70, 1.330), (0.75, 1.433), (0.80, 1.530), (0.85, 1.704), (0.90, 1.937)]
    table3 = [(0.00, 1.000), (0.05, 1.001), (0.10, 1.004), (0.15, 1.007), (0.20, 1.014), (0.25, 1.022), (0.30, 1.042),
              (0.35, 1.063), (0.40, 1.081), (0.45, 1.114), (0.50, 1.136), (0.55, 1.178), (0.60, 1.221), (0.65, 1.294),
              (0.70, 1.357), (0.75, 1.447), (0.80, 1.578), (0.85, 1.765), (0.90, 2.018)]
    table4 = [(0.00, 1.001), (0.05, 1.004), (0.10, 1.009), (0.15, 1.015), (0.20, 1.023), (0.25, 1.036), (0.30, 1.050),
              (0.35, 1.069), (0.40, 1.097), (0.45, 1.130), (0.50, 1.153), (0.55, 1.195), (0.60, 1.237), (0.65, 1.308),
              (0.70, 1.388), (0.75, 1.503), (0.80, 1.630), (0.85, 1.859), (0.90, 2.170)]
    table5 = [(0.00, 1.000), (0.05, 1.001), (0.10, 1.002), (0.15, 1.003), (0.20, 1.011), (0.25, 1.020), (0.30, 1.029),
              (0.35, 1.053), (0.40, 1.076), (0.45, 1.105), (0.50, 1.127), (0.55, 1.167), (0.60, 1.203), (0.65, 1.369),
              (0.70, 1.328), (0.75, 1.430), (0.80, 1.532), (0.85, 1.724), (0.90, 1.936)]
    table6 = [(0.00, 1.000), (0.05, 1.001), (0.10, 1.002), (0.15, 1.009), (0.20, 1.014), (0.25, 1.027), (0.30, 1.037),
              (0.35, 1.067), (0.40, 1.086), (0.45, 1.113), (0.50, 1.138), (0.55, 1.181), (0.60, 1.221), (0.65, 1.289),
              (0.70, 1.355), (0.75, 1.449), (0.80, 1.568), (0.85, 1.783), (0.90, 2.012)]
    table7 = [(0.00, 1.000), (0.05, 1.001), (0.10, 1.001), (0.15, 1.009), (0.20, 1.014), (0.25, 1.027), (0.30, 1.037),
              (0.35, 1.067), (0.40, 1.086), (0.45, 1.113), (0.50, 1.138), (0.55, 1.181), (0.60, 1.221), (0.65, 1.289),
              (0.70, 1.355), (0.75, 1.449), (0.80, 1.568), (0.90, 2.012)]
    table8 = [(0.00, 1.000), (0.05, 1.001), (0.10, 1.004), (0.15, 1.006), (0.20, 1.007), (0.25, 1.014), (0.30, 1.022),
              (0.35, 1.032), (0.40, 1.045), (0.45, 1.060), (0.50, 1.075), (0.55, 1.101), (0.60, 1.124), (0.65, 1.157),
              (0.70, 1.193), (0.75, 1.247), (0.80, 1.315), (0.85, 1.422), (0.90, 1.564)]
    table9 = [(0.00, 1.000), (0.05, 1.001), (0.10, 1.004), (0.15, 1.011), (0.20, 1.017), (0.25, 1.022), (0.30, 1.030),
              (0.35, 1.045), (0.40, 1.056), (0.45, 1.075), (0.50, 1.092), (0.55, 1.126), (0.60, 1.152), (0.65, 1.197),
              (0.70, 1.241), (0.75, 1.319), (0.80, 1.399), (0.85, 1.545), (0.90, 1.709)]

    b = []
    for i in range(1, 10):
        for q, F in eval("table" + str(i)):
            b.append(eval("Sifator" + str(i))(q=q, F=F))
    print(b)
    db.session.add_all(b)
    db.session.commit()
    # a = Siftable.query.all()
