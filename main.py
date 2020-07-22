from selenium import webdriver
import configparser
import time

config = configparser.ConfigParser()
config.read("config.ini")

PATH = config["SETTINGS"]["PATH"]
ACCOUNT = config["LOGIN_INFO"]["ACCOUNT"]
PASSWORD = config["LOGIN_INFO"]["PASSWORD"]
URL_LOGIN = config["URL"]["LOGIN"]


def login(month, day):
    driver.find_element_by_xpath('//*[@id="logintStatus"]').click()

    # wait for the showing up of login box and try to login
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="account"]').send_keys(ACCOUNT)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(PASSWORD)

    # wait for the response of the new page
    driver.find_element_by_xpath('//*[@id="loginWindow"]/table/tbody/tr[4]/td/div/input[1]').click()
    time.sleep(2)

    # wait for the showing up of the window
    driver.find_element_by_xpath('//*[@id="menu"]/li[2]/a').click()
    time.sleep(1)

    for i in range(0, len(day)):
        for j in range(0, 2):
            if(j % 2 == 0):
                check_in = "09:30"
                check_out = "12:00"
            else:
                check_in = "13:00"
                check_out = "16:00"

            # wait for the showing up of the input box
            driver.find_element_by_xpath('//*[@id="AddButton"]').click()
            time.sleep(1)

            onduty = driver.find_element_by_xpath('//*[@id="OnDuty"]')
            onduty.clear()
            onduty.send_keys("2020/" + month + "/" + day[i] + " " + check_in)

            offduty = driver.find_element_by_xpath('//*[@id="OffDuty"]')
            offduty.clear()
            offduty.send_keys("2020/" + month + "/" + day[i] + " " + check_out)

            driver.find_element_by_xpath('//*[@id="JobContent"]').send_keys("協助壁畫修復作業")

            driver.find_element_by_xpath('//*[@id="SaveDetailButton"]').click()
            time.sleep(1)

        j = 0


if __name__ == '__main__':
    driver = webdriver.Chrome(PATH)
    driver.get(URL_LOGIN)
    month = "07"
    day = ["14", "15"]
    login(month, day)
    print("Mission Complete！")
