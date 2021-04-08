from selenium import webdriver
from time import sleep
import sched, time

s = sched.scheduler(time.time, time.sleep)


def bot(usr, pas):
    fp = webdriver.FirefoxProfile('Firefox profile path')#Firefox profile path , type "about:support" in Firefox to get all info
    br = webdriver.Firefox(executable_path='geckodriver', firefox_profile=fp)
    br.maximize_window()
    br.get("https://giris.eba.gov.tr/EBA_GIRIS/student.jsp")
    user = br.find_element_by_name("tckn")
    user.clear()
    user.send_keys(usr)
    pasd = br.find_element_by_name("password")
    pasd.clear()
    pasd.send_keys(pas)
    btn = br.find_element_by_css_selector(".nl-form-send-btn")
    btn.click()
    print("Login Successfully...")
    sleep(5)

    br.get("https://ders.eba.gov.tr/ders/proxy/VCollabPlayer_v0.0.797/liveMiddleware/eba.html")
    sleep(5)
    btn2 = br.find_element_by_link_text("Hemen Katıl").click()
    print("Joining to lesson.")
    btn3 = br.find_element_by_xpath('//*[@id="join"]').click()
    print("Joined successfully.")
    btn4 = br.find_element_by_id("cancel").click()
    sleep(3)
    print("Cancel clicked..")

    s.enter(2430, 1, bot, (usr, pas,))
    sleep(75)
    br.quit()


bot("ID Number", "EBA-password")
s.enter(2430, 1, bot, (s,))
s.run()

