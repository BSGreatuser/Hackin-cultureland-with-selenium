from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter.font
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, random, sys, os, webbrowser

from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

def callback(url):
    webbrowser.open_new(url)

win = Tk()
s = Style()
win.title('컬쳐 핵킨툴ㅣ봉순#1234')
win.geometry('305x220')

font = tkinter.font.Font(family="나눔바른고딕", size=18)
afont = tkinter.font.Font(family="메이플스토리", size=10)
s.configure('W.TButton', font=('나눔바른고딕', 12), foreground='Black')

# ID LABEL
id_label = Label(win)
id_label.config(text='컬쳐랜드 ID', font=font)
id_label.pack()

# ID ENTRY
id_entry = Entry(win)
id_entry.pack()

# PW LABEL
pw_label = Label(win)
pw_label.config(text='컬쳐랜드 PW', font=font)
pw_label.pack()

# PW ENTRY
pw_entry = Entry(win)
pw_entry.config(show='*')
pw_entry.pack()

# AMOUNT LABEL
amount_label = Label(win)
amount_label.config(text='액수', font=font)
amount_label.pack()

# AMOUNT ENTRY
amount_entry = Entry(win)
amount_entry.pack()


def login():
    ID = id_entry.get()
    PW = pw_entry.get()
    money = amount_entry.get()
    options = ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument("disable-gpu")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("window-size=1920x1080")

    if getattr(sys, 'frozen', False): 
        chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
        browser = webdriver.Chrome("./chromedriver.exe")
    else:
        browser = webdriver.Chrome()

    browser.get('https://m.cultureland.co.kr/mmb/loginMain.do')

    browser.find_element_by_id('txtUserId').send_keys(ID)
    browser.find_element_by_id('passwd').click()
    rst = '-'.join(PW).split('-')

    for i in range(0, len(PW)):
        if rst[i].isdecimal():
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@alt=\"' + rst[i] + '\"]'))).click()
        if rst[i].isupper():
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_cp\"]/div/img"))).click()
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@alt=\"대문자' + rst[i] + '\"]'))).click()
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_cp\"]/div/img"))).click()
        if rst[i].islower():
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@alt=\"' + rst[i] + '\"]'))).click()
        if rst[i] == '~':
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@alt=\"물결표시\"]'))).click()
            if len(PW) == 12:
                pass
            else:
                WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
        if rst[i] == '@':
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@alt=\"골뱅이\"]'))).click()
            if len(PW) == 12:
                pass
            else:
                WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
        if rst[i] == '$':
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@alt=\"달러기호\"]'))).click()
            if len(PW) == 12:
                pass
            else:
                WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
        if rst[i] == '^':
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@alt=\"꺽쇠\"]'))).click()
            if len(PW) == 12:
                pass
            else:
                WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
        if rst[i] == '*':
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@alt=\"별표\"]'))).click()
            if len(PW) == 12:
                pass
            else:
                WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
        if rst[i] == '(':
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@alt=\"왼쪽괄호\"]'))).click()
            if len(PW) == 12:
                pass
            else:
                WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
        if rst[i] == ')':
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@alt=\"오른쪽괄호\"]'))).click()
            if len(PW) == 12:
                pass
            else:
                WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
        if rst[i] == '_':
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
            WebDriverWait(browser, 3).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@alt=\"밑줄\"]'))).click()
            if len(PW) == 12:
                pass
            else:
                WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
        if rst[i] == '+':
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//img[@alt=\"더하기\"]'))).click()
            if len(PW) == 12:
                pass
            else:
                WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mtk_sp\"]/div/img"))).click()
    if len(PW) < 12:
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='mtk_done']/div/img"))).click()
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "btnLogin"))).click()
    browser.get('https://m.cultureland.co.kr/csh/cshGiftCard.do')
    time.sleep(0.3)
    try:
        a = browser.find_element_by_css_selector('#blnAmtSub')
        b = browser.find_element_by_css_selector('#bnkAmtSub')
    except:
        al.config(text='[-] 입력하신 아이디 또는 비밀번호가 틀립니다', font=afont)
        browser.quit()
        return

    ableuse = str(a.get_attribute('outerHTML')).replace('<span id="blnAmtSub">', '').replace('</span>', '').replace(',', '')
    safeuse = str(b.get_attribute('outerHTML')).replace('<span id="bnkAmtSub">', '').replace('</span>', '').replace(',', '')
    time.sleep(0.1)
    amount = int(ableuse) + int(safeuse)
    before = format(int(amount), ',')

    for i in range(random.randint(2, 8)):
        time.sleep(random.randint(1, 5))
        browser.refresh()
    time.sleep(0.5)
    element = browser.find_element_by_css_selector('#blnAmtSub')
    money = format(int(money), ',')
    browser.execute_script('arguments[0].innerHTML = "{}";'.format(money), element)
    time.sleep(0.5)
    a = browser.find_element_by_css_selector('#blnAmtSub')
    b = browser.find_element_by_css_selector('#bnkAmtSub')
    ableuse = str(a.get_attribute('outerHTML')).replace('<span id="blnAmtSub">', '').replace('</span>', '').replace(',', '')
    safeuse = str(b.get_attribute('outerHTML')).replace('<span id="bnkAmtSub">', '').replace('</span>', '').replace(',', '')
    amount = int(ableuse) + int(safeuse)
    after = format(int(amount), ',')

    al.config(text='[+] 해킹성공', font=afont)
    al2.config(text='이전 잔액: {0}원 / 이후 잔액: {1}원'.format(before, after), font=afont)
    time.sleep(1)


def play():
    ID = id_entry.get()
    PW = pw_entry.get()
    money = amount_entry.get()
    if ID == '' or PW == '':
        messagebox.showerror("Error Example", "아이디 또는 비밀번호가 공백입니다")
        return
    if not money.isdecimal():
        messagebox.showerror("Error Example", "올바른 액수가 아닙니다")
        return
    login()

# PLAY BUTTON
btn = Button(win, text='실행', style='W.TButton', command=play)
btn.pack()

# al LABEL
al = Label(win)
al.config(text='이 프로그램은 무료인것!', font=afont)
al.pack()
al.bind("<Button-1>", lambda e: callback("https://github.com/BSGreatuser/Hackin-cultureland-with-selenium"))

# al2 LABEL
'''
- 하단 수정금지 -
'''
al2 = Label(win)
al2.config(text='https://봉순.com', font=afont, foreground='blue', background='#C0FFFF')
al2.pack()
al2.bind("<Button-1>", lambda e: callback("https://bs777.xyz"))


win.mainloop()
