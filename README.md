###selenium+python学习

[codeception]("https://codeception.com", "自动化测试参考网址")


根据商品id获取属于哪个店铺可以获取到，在抓取的时候，使用curl函数库，
学习到了curl可以模拟HTTP请求，并且得到响应，返回html，如果需要获取
指定的元素，则可以使用正则表达式，匹配元素，如果不想写的话可以使用一些PHP解析dom
插件，比如。

[simple_html_dom]("https://github.com/samacs/simple_html_dom", "php-dom解析插件")

但是根据商铺获取商品时候，商品是ajax异步加载过来的，异步的时候如果没登录，无法抓取。

但是想法是，模拟登陆之后，把HTTP的response响应中的head中的cookie存起来，下次请求的时候把cookie放大HTTP请求头中
想法是使用一个账号，模拟请求登录接口时候，使用curl模拟HTTP登录请求，需要设置HTTP请求head的User-Agent，请求类型content-type：form-encode方式
可以进去，但是下一步需要验证身份，输入手机号获取验证码。不知道怎么整了。

但是可以摸索的过程中，了解了web自动化测试。

###selenium+Chromedriver+python+Chrome测试


自动化测试工具：

一、pip是一个Python包管理工具。pip install selenium时报错 pip版本太低。
更新pip版本命令使用：python -m pip install --upgrade pip


安装pip时，需要有两种安装方式：
1. 一种在线安装， 就是pip install selenium
2. 第二种离线安装，先把pip下载到本地,[pip下载地址]("https://pypi.python.org/pypi/pip", "下载地址")

3. 升级pip

    pip.exe install -U pip-9.0.2-py2.py3-none-any.whl

4. 安装selenium

pip.exe install selenium-3.11.0-py2.py3-none-any.whl

二、Cromedriver[下载地址]("https://npm.taobao.org/mirrors/chromedriver", "chromedriver下载地址")

选择版本的时候要和Chrome浏览器版本一致。安装完需要把Chromedriver放到环境变量中。

<一>写一个python脚本(hello.py)：

    from selenium import webdriver

    browser = webdriver.Chrome()
    browser.get('http://www.qq.com/')

运行python hello.py，这样，会启动Chrome浏览器，自动打开Tencent官网



selenium通过Chromedriver驱动打开Chrome浏览器。这样的测试脚本的客户端必须和浏览器的客户端在一块。

所以说，如果脚本是在Linux上运行，如果Linux没有安装Chrome的话、或者Linux没有安装图形安装界面。这种方法就没办法实现测试了。这样可以使用另一种方法。安装selenium-server版（这版本的话是个jar包，需要安装jdk）+Chromedriver+Chrome（这样启动selenium服务）
测试脚本中通过链接selenium服务的端口就可以，远程测试了。

###selenium-server版+Chromedriver+Chrome+python

去selenium官网下载selenium的server版，我在这里下载的是2.46，下载的是个jar包，所以需要jdk启动它。
正好在安装NetBeans的时候也需要安装jdk，所以不用安装了，但是进入cmd输入java --version报错未知的命令。应该是jdk不在
环境变量中，所以把java的加到path环境变量中。

开启selenium服务可以使用下面的命令：

    java -jar F:\chromedriver_win32\selenium-server-standalone-2.46.0.jar ^
    -timeout=20 ^
    -browserTimeout=60 ^
    -Dwebdriver.chrome.driver=F:\chromedriver_win32\chromedriver.exe

输入这个命令后，会启动selenium服务，命令会输出
jdk版本信息
会监听：http://127.0.0.1:4444/wd/hub


DOS中的清除屏幕命令cls相当于Unix中的clear，在Linux中如果一个命令长了可以使用\斜线换行，但是在DOS中这个不好使，需要使用^符号。


学习到了python中注释方法。单行注释，可以使用#号，多上注释可以使用三个引号，可以是三个单引号也可以是三个双引号。


我想每次脚本启动时打开多个回话（即浏览器，感觉不太好，在网上搜索到如下代码）
但是我想服用这个session回话的话，怎么使用可以使用
写一个python脚本（selenium_common2.py）。

但是这样会重新打开一个空白的回话。在网上查询是python的Remote类每次实例化的时候，会执行start_session()
所以会重新打开一次空白回话。

看网上是重写了一个Remote类

写一个python脚本（selenium_common.py）代码如下：

    from selenium import webdriver
    driver = webdriver.Chrome()
    executor_url = driver.command_executor._url
    session_id = driver.session_id
    print(session_id)
    print(executor_url)
    driver.get("http://www.spiderpy.cn/")




支持一个打开一个浏览器回话的python程序，但是会出现一个空白回话。

    from selenium import webdriver

    driver = webdriver.Chrome()
    executor_url = driver.command_executor._url
    session_id = driver.session_id
    driver.get("http://www.spiderpy.cn/")

    print(session_id)
    print(executor_url)

    driver2 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver2.session_id = session_id
    print(driver2.current_url)


但是这样会重新打开一个空白的回话。在网上查询是python的Remote类每次实例化的时候，会执行start_session()
所以会重新打开一次空白回话。

看网上是重写了一个Remote类

    class ReuseChrome(Remote):

        def __init__(self, command_executor, session_id):
          self.r_session_id = session_id
          Remote.__init__(self, command_executor=command_executor, desired_capabilities={})

        def start_session(self, capabilities, browser_profile=None):
           """
           重写start_session方法
           """
           if not isinstance(capabilities, dict):
             raise InvalidArgumentException("Capabilities must be a dictionary")
           if browser_profile:
           if "moz:firefoxOptions" in capabilities:
                capabilities["moz:firefoxOptions"]["profile"] = browser_profile.encoded
           else:
                capabilities.update({'firefox_profile': browser_profile.encoded})

          self.capabilities = options.Options().to_capabilities()
          self.session_id = self.r_session_id
          self.w3c = False





