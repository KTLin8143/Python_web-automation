import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
br.open('http://e3.nctu.edu.tw/NCTU_EASY_E3P/LMS3/login.aspx?ReturnUrl=/NCTU_Easy_E3P/lms3/enter_course_index.aspx')
br.select_form(nr=0)
br.form['txtLoginId'] = '0553441'
br.form['txtLoginPwd'] = 'apjw184'
sub = br.submit()
x = br.response().get_data()

soup = BeautifulSoup(x, 'html.parser')
print soup
