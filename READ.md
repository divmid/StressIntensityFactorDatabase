## 操作步骤
1. 安装python3.7版本
2. 进入虚拟环境
```
cd StressIntensityFactorDatabase
venv\Scripts\activate
```
3. 安装python依赖
```
pip install -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```
4.启动环境
```
python app.py

```

5.启动代码的解释
```
# port是可修改的端口，启动之后是本机ip
app.run(host="0.0.0.0", port="5001")
访问的url: http://localhost:5001/sitf?k=0.82
只需要改变k的值就可以得到F的值, k的取值范围是[0,0.95]
访问错误会返回code=400，正确是code=200
{
  "F": 1.867,
  "code": 200
}
{
  "code": 400,
  "msg": "参数异常"
}
```

6.python调用接口
```
pip install requests
r = requests.get('http://localhost:5001/sitf?k=0.82')
r.json()
```

7.调用文件 test.py
```
cd StressIntensityFactorDatabase
venv\Scripts\activate

python test.py
```


项目效果：先选择 裂纹模式 1,2,3  然后输入 a1[0-20],a2[0-40],d[0.0-100.0],  返回出k值

 a.数据库与表的对应关系：
 1 对应表sifable1,sifable2,sifable3
 2 对应表sifator4,sifable5,sifble6
 3 对应表sifator7,sifator8,sifator9

b.值与表的关系：
    a1比a2=0时  sifable1
    a1比a2=10时  sifable2
    a1比a2=20时  sifable3

    a1比a2=0时  sifable4
    a1比a2=10时  sifable5
    a1比a2=20时  sifable6

    a1比a2=11时  sifable7
    a1比a2=3时  sifable8
    a1比a2=5时  sifable9
 c.单个表内公式计算：输入a1,a2,d，得到q,
      q=(a1+a2)/d; //得到q
   通过q所在区间查询 f  //q得f
   k=f*根号(3.14*a1)   //f 通过计算的k(3)保留三位小数
 返回出k值

注: 第一张表的应该是sifaor ，已经把k  换成q  名字也改成了sifable1
       取值 q为0.00时取0.00的值 为0.00-0.10时取0.5的值  为0.10时取0.10的值
                0.80-0.90取0.85  0.90取0.90的值