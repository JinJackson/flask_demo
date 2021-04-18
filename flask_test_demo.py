# 1. 导入Flask扩展
from flask import Flask, render_template

# 2.创建Flask应用程序实例，固定传入__name__，作用是为了确定资源所在路径
app = Flask(__name__)

# 3.通过装饰器定义路由, 默认都是post请求
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test')
def test():
    return 'test'

# 返回一个网页
@app.route('/website')
def testweb():
    return render_template('index.html')  #默认就在templates的目录下

# 使用post请求
@app.route('/postTest', methods=['POST'])
def testPost():
    return 'This is a test for post'


# 使用同一个视图参数，显示不同用户的信息
# <>定义路由参数
@app.route('/orders/<order_id>')
def get_order_id(order_id):  #参数名和路由参数同名
    return 'order_id %s' % order_id

# 有时，希望对参数类型有所限制
# 将参数强转int
@app.rout('/orders2/<int:order_id>')
def get_order_id2(order_id):
    return 'order_id %s' % order_id

if __name__ == '__main__':
    # 4.启动程序，flask会提供一个简易的本地服务器
    app.run()