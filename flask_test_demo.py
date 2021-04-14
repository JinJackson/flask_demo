# 1. 导入Flask扩展
from flask import Flask, render_template

# 2.创建Flask应用程序实例，固定传入__name__，作用是为了确定资源所在路径
app = Flask(__name__)

# 3.通过装饰器定义路由
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test')
def test():
    return 'test'

#返回一个网页
@app.route('/website')
def testweb():
    return render_template('index.html')  #默认就在templates的目录下


if __name__ == '__main__':
    # 4.启动程序，flask会提供一个简易的本地服务器
    app.run()