import random
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config import i, b, link, name_input, gmail_input, wallet_input, tg_input, login_button,\
    _1_mission_click, _1_mission_confirm, _1_mission_link, _1_mission_input,\
    _2_mission_click, _2_mission_confirm, _2_mission_link, _2_mission_input,\
    _3_mission_click, _3_mission_confirm, _3_mission_link, _3_mission_input,\
    _4_mission_click, _4_mission_confirm, _4_mission_link, _4_mission_input,\
    _5_mission_click, _5_mission_confirm, _5_mission_link, _5_mission_input,\
    _6_mission_click, _6_mission_confirm, _6_mission_link, _6_mission_input,\
    _7_mission_click, _7_mission_confirm, _7_mission_link, _7_mission_input,\
    _8_mission_click, _8_mission_confirm, _8_mission_link, _8_mission_input,\
    _9_mission_click, _9_mission_confirm, _9_mission_link, _9_mission_input,\
    _10_mission_click, _10_mission_confirm, _10_mission_link, _10_mission_input,\
    _11_mission_click, _11_mission_confirm, _11_mission_link, _11_mission_input,\
    _12_mission_click, _12_mission_confirm, _12_mission_link, _12_mission_input,\
    _13_mission_click, _13_mission_confirm, _13_mission_link, _13_mission_input
from gmail import email_list
from usernames import username_list
from wallet import wallet_list

try:
    while i < b:
        # options UserAgent
        useragent = UserAgent()
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-agent={useragent.chrome}")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("user-data-dir=C:\\Users\\ddd\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
        driver = webdriver.Chrome(
            executable_path='chromedriver/chromedriver.exe',
            options=options
        )
        print('?????????????? ????????????????')
        gmail = random.choice(email_list)
        wallet = random.choice(wallet_list)
        username = random.choice(username_list)
        driver.execute_script(
            "var s=window.document.createElement('script'); s.src='javascript.js';window.document.head.appendChild(s);")
        driver.get("chrome://settings/clearBrowserData")

        time.sleep(3)
        print('??????????????  ??????????????')
        driver.switch_to.window(driver.window_handles[0])


        driver.get(link)
        print(link + ' ??????????????????')
        element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.NAME, name_input))
        )
        name_in = driver.find_element_by_name(name_input)
        name_in.clear()
        name_in.send_keys(gmail)
        print('?????? ' + gmail + ' ??????????????')

        email_in = driver.find_element_by_name(gmail_input)
        email_in.clear()
        email_in.send_keys(gmail)
        print('?????????? ' + gmail + ' ??????????????')

        tg_in = driver.find_element_by_name(tg_input)
        tg_in.clear
        tg_in.send_keys(username)
        print('?????????????????? ' + username + ' ????????????')

        wallet_in = driver.find_element_by_name(wallet_input)
        wallet_in.clear()
        wallet_in.send_keys(wallet)
        print('?????????????? ' + wallet + ' ????????????')
        time.sleep(4)

        login_but = driver.find_element_by_id(login_button)
        login_but.click()
        print('?????????????????????? ?? ??????????????')
        time.sleep(5)

        # mission 1
        element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, _1_mission_click))
        )
        mis_1_clck = driver.find_element_by_id(_1_mission_click)
        mis_1_clck.click()
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _1_mission_link))
        )
        time.sleep(1)
        mis_1_link = driver.find_element_by_id(_1_mission_link)
        mis_1_link.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        mis_1_in = driver.find_element_by_id(_1_mission_input)
        mis_1_in.clear()
        mis_1_in.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _1_mission_confirm))
        )
        mis_1_verify = driver.find_element_by_id(_1_mission_confirm)
        mis_1_verify.click()
        print('?????????????? 1 ??????????????????')

        email_list.remove(gmail)
        print('?????????? ' + gmail + ' ?????????????? ???? ????????????')
        wallet_list.remove(wallet)
        print('?????????????? ' + wallet + ' ???????????? ???? ????????????')

        # mission 2
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _2_mission_click))
        )
        mis_2_clck = driver.find_element_by_id(_2_mission_click)
        mis_2_clck.click()
        time.sleep(1)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _2_mission_input))
        )
        mis_2_link = driver.find_element_by_id(_2_mission_link)
        mis_2_link.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        mis_2_in = driver.find_element_by_id(_2_mission_input)
        mis_2_in.clear()
        mis_2_in.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _2_mission_confirm))
        )
        mis_2_verify = driver.find_element_by_id(_2_mission_confirm)
        mis_2_verify.click()
        print('?????????????? 2 ??????????????????')


        # mission 3
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _3_mission_click))
        )
        mis_3_clck = driver.find_element_by_id(_3_mission_click)
        mis_3_clck.click()
        time.sleep(1)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _3_mission_link))
        )
        mis_3_link = driver.find_element_by_id(_3_mission_link)
        mis_3_link.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        mis_3_in = driver.find_element_by_id(_3_mission_input)
        mis_3_in.clear()
        mis_3_in.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _3_mission_confirm))
        )
        mis_3_verify = driver.find_element_by_id(_3_mission_confirm)
        mis_3_verify.click()
        print('?????????????? 3 ??????????????????')

        # mission 4
        element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, _4_mission_click))
        )

        mis_4_clck = driver.find_element_by_id(_4_mission_click)
        mis_4_clck.click()
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _4_mission_link))
        )
        time.sleep(1)
        mis_4_link = driver.find_element_by_id(_4_mission_link)
        mis_4_link.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        mis_4_in = driver.find_element_by_id(_4_mission_input)
        mis_4_in.clear()
        mis_4_in.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _4_mission_confirm))
        )
        mis_4_verify = driver.find_element_by_id(_4_mission_confirm)
        mis_4_verify.click()
        print('?????????????? 4 ??????????????????')


        # # mission 5
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _5_mission_click))
        )
        mis_5_clck = driver.find_element_by_id(_5_mission_click)
        mis_5_clck.click()
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _5_mission_link))
        )
        time.sleep(1)
        mis_5_link = driver.find_element_by_id(_5_mission_link)
        mis_5_link.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        mis_5_in = driver.find_element_by_id(_5_mission_input)
        mis_5_in.clear()
        mis_5_in.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _5_mission_confirm))
        )
        mis_5_verify = driver.find_element_by_id(_5_mission_confirm)
        mis_5_verify.click()
        print('?????????????? 5 ??????????????????')

        # mission 6
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _6_mission_click))
        )
        mis_6_clck = driver.find_element_by_id(_6_mission_click)
        mis_6_clck.click()
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _6_mission_link))
        )
        time.sleep(1)
        mis_6_link = driver.find_element_by_id(_6_mission_link)
        mis_6_link.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        mis_6_in = driver.find_element_by_id(_6_mission_input)
        mis_6_in.clear()
        mis_6_in.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _6_mission_confirm))
        )
        mis_6_verify = driver.find_element_by_id(_6_mission_confirm)
        mis_6_verify.click()
        print('?????????????? 6 ??????????????????')

        #mission 7
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _7_mission_click))
        )
        mis_7_clck = driver.find_element_by_id(_7_mission_click)
        mis_7_clck.click()
        time.sleep(1)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _7_mission_link))
        )
        mis_7_link = driver.find_element_by_id(_7_mission_link)
        mis_7_link.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        mis_7_in = driver.find_element_by_id(_7_mission_input)
        mis_7_in.clear()
        mis_7_in.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _7_mission_confirm))
        )
        mis_7_verify = driver.find_element_by_id(_7_mission_confirm)
        mis_7_verify.click()
        print('?????????????? 7 ??????????????????')

        # mission 8
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _8_mission_click))
        )
        mis_8_clck = driver.find_element_by_id(_8_mission_click)
        mis_8_clck.click()
        time.sleep(1)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _8_mission_link))
        )
        mis_8_link = driver.find_element_by_id(_8_mission_link)
        mis_8_link.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        mis_8_in = driver.find_element_by_id(_8_mission_input)
        mis_8_in.clear()
        mis_8_in.send_keys(username)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _8_mission_confirm))
        )
        mis_8_verify = driver.find_element_by_id(_8_mission_confirm)
        mis_8_verify.click()
        print('?????????????? 8 ??????????????????')

        # mission 9
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _9_mission_click))
        )
        mis_9_clck = driver.find_element_by_id(_9_mission_click)
        mis_9_clck.click()
        time.sleep(1)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _9_mission_link))
        )
        mis_9_link = driver.find_element_by_id(_9_mission_link)
        mis_9_link.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        # mis_9_in = driver.find_element_by_id(_9_mission_input)
        # mis_9_in.clear()
        # mis_9_in.send_keys(username)
        # element = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, _9_mission_confirm))
        # )
        # mis_9_verify = driver.find_element_by_id(_9_mission_confirm)
        # mis_9_verify.click()
        print('?????????????? 9 ??????????????????')

        # mission 10
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _10_mission_click))
        )
        mis_10_clck = driver.find_element_by_id(_10_mission_click)
        mis_10_clck.click()
        time.sleep(1)
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, _10_mission_link))
        )
        mis_10_link = driver.find_element_by_id(_10_mission_link)
        mis_10_link.click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        # mis_10_in = driver.find_element_by_id(_10_mission_input)
        # mis_10_in.clear()
        # mis_10_in.send_keys(username)
        # element = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, _10_mission_confirm))
        # )
        # mis_10_verify = driver.find_element_by_id(_10_mission_confirm)
        # mis_10_verify.click()
        print('?????????????? 10 ??????????????????')
        #
        # # mission 11
        # element = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, _11_mission_click))
        # )
        # mis_11_clck = driver.find_element_by_id(_11_mission_click)
        # mis_11_clck.click()
        # time.sleep(1)
        # element = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, _11_mission_link))
        # )
        # mis_11_link = driver.find_element_by_id(_11_mission_link)
        # mis_11_link.click()
        # driver.switch_to.window(driver.window_handles[-1])
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])
        # mis_11_in = driver.find_element_by_id(_11_mission_input)
        # mis_11_in.clear()
        # mis_11_in.send_keys(username)
        # element = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, _11_mission_confirm))
        # )
        # mis_11_verify = driver.find_element_by_id(_11_mission_confirm)
        # mis_11_verify.click()
        # print('?????????????? 11 ??????????????????')
        #
        # # mission 12
        # element = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, _12_mission_click))
        # )
        # mis_12_clck = driver.find_element_by_id(_12_mission_click)
        # mis_12_clck.click()
        # time.sleep(1)
        # element = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, _12_mission_link))
        # )
        # mis_12_link = driver.find_element_by_id(_12_mission_link)
        # mis_12_link.click()
        # driver.switch_to.window(driver.window_handles[-1])
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])
        # mis_12_in = driver.find_element_by_id(_12_mission_input)
        # mis_12_in.clear()
        # mis_12_in.send_keys(username)
        # element = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, _12_mission_confirm))
        # )
        # mis_12_verify = driver.find_element_by_id(_12_mission_confirm)
        # mis_12_verify.click()
        # print('?????????????? 12 ??????????????????')
        #
        # # mission 13
        # element = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, _13_mission_click))
        # )
        # mis_13_clck = driver.find_element_by_id(_13_mission_click)
        # mis_13_clck.click()
        # time.sleep(1)
        # element = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, _13_mission_link))
        # )
        # mis_13_link = driver.find_element_by_id(_13_mission_link)
        # mis_13_link.click()
        # driver.switch_to.window(driver.window_handles[-1])
        # driver.close()
        # driver.switch_to.window(driver.window_handles[0])
        # mis_13_in = driver.find_element_by_id(_13_mission_input)
        # mis_13_in.clear()
        # mis_13_in.send_keys(username)
        # element = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.ID, _13_mission_confirm))
        # )
        # mis_13_verify = driver.find_element_by_id(_13_mission_confirm)
        # mis_13_verify.click()
        # print('?????????????? 13 ??????????????????')

        print('?????? ?????????????? ??????????????????!')
        print('????????????????????...')
        time.sleep(8)

        driver.quit()
        # print('???????????? ????')
        # time.sleep(5)
        # time.sleep(10)
        # print('?????????????? ????')
        # time.sleep(10)
        i += 1
        if i == 5:
            print('?????????? IP')
            time.sleep(15)
            print('???????????????? ?????????? ????????????')
            time.sleep(15)




except Exception as ex:
    print(ex)
    pass

finally:
    driver.close()
    driver.quit()