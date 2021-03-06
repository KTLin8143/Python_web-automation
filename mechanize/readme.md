# Web automation

Web automation using mechanize

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 2.7版本
注意:若你使用的為python 3.xx版本，請使用MechanicalSoup

### Installing

1. 安裝 mechanize
用 easy_install 或 pip 就可以安裝 python 版的 mechanize：
```
easy_install mechanize
pip install mechanize
```
安裝完成後，import mechanize 試試看:
```
Python 2.7.13 |Anaconda 4.3.1 (64-bit)| (default, Dec 19 2016, 13:29:36) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> import mechanize
>>>
```

### Strating

mechanize.Browser() 建立一個 Browser 物件
set_handle_robots(False)有些網站會要求機器人不能來瀏覽，這邊設成 False 的話就會忽略網站的設定
br.addheaders 加上 User-Agent 的設定

```
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
```

執行 open() 可以瀏覽你想登入之URL
這邊以我想登入的學校網站入口為例

```
br.open('http://e3.nctu.edu.tw/NCTU_EASY_E3P/LMS3/login.aspx?ReturnUrl=/NCTU_Easy_E3P/lms3/enter_course_index.aspx')
```

在login前，必須讓 mechanize 知道要對哪個表單做事
這邊就要用 select_form() 這個函式來指定
nr 代表的是第幾個表單 (從 0 開始)

```
br.select_form(nr=0)
```

對你的輸入帳號欄位點選右鍵 -->檢查
就可以看到你所需登入頁的欄位分別為何
這此我們的網頁所需欄位為: txtAccount、txtPwd

```
<input name="txtAccount" type="text" id="txtAccount" value="Account" style="width:180px;">
<input name="txtPwd" type="password" id="txtPwd" style="width:180px;">
```

用 br['欄位名稱'] 就可以取得/填入值，然後用 br.submit() 送出表單：

```
br.form['txtLoginId'] = 'your account'
br.form['txtLoginPwd'] = 'your pwd'
sub = br.submit()
```
現在已經進入了學校系統
使用 br.response().get_data() 存的就是進入後網頁的內容

```
print br.response().get_data()
```

目前在研究，如何點選Javasript button with__doPostBack 

```
href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvCourse$ctl02$lnkCourseName','')"
```
