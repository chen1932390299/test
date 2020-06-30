from  appium import  webdriver
import  json
from homepage import *
from finds import *
import time
import threading

# app.driver=driver
# uiautomator_text("网易云音乐",driver).click()


def test_case(device_name,server_port):
    desired_caps = {
        "platformName": "Android",  # IOS,Andriod
        "platformVersion": "5.1.1",  # 平台安卓版本
        "deviceName": device_name,  # get from adb devices
        "appPackage": "com.netease.cloudmusic",  # package Name
        "appActivity": ".activity.MainActivity",  # app activity Name
        "unicodeKeyboard": True,  # set unicode keyboard
        "resetKeyboard": True,  # set each time reset keyboard
        "automationName": "Uiautomator2",  # automation setting choice in ['Appium' and 'Uiautomator2']
        "noReset": True,  # keep last session of user  login
        "autoLaunch": False  # allow auto launch False
    }
    print("-->>>>>>desired_caps:\n", json.dumps(desired_caps, indent=2))
    driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(server_port), desired_caps)
    driver.implicitly_wait(25)
    # driver.close_app()
    driver.launch_app()
    app = Application(app_driver=driver)
    if app.exist_element(enjoy_first):
        app.location_click(agree_protol)
        app.location_click(login_btn)
        app.location_input(phoneNum_input,"18676743129")
        app.location_click(Next_btn)
        app.location_input(password_input,"498858336.abc")
        app.location_click(submit_loginbtn)
    app.location_click(search_btn)
    app.location_input(search_input,send_key="虚拟")
    app.press_event(66)
    time.sleep(4)
    app.uiautomator_text("单曲").click()
    time.sleep(6)
    driver.quit()


class AppThread(threading.Thread):

    def __init__(self,device,server_port):
        super(AppThread, self).__init__()
        self.device=device
        self.server_port=server_port

    def run(self) -> None:
        print("current device and port :",self.device,self.server_port)
        test_case(self.device,self.server_port)


if __name__ == '__main__':
    conf=[("emulator-5554","4728"),("emulator-5556","4725")] # ,
    app_task=[AppThread(device,port) for device,port in conf]
    pool=[]
    for task in app_task:
        task.start()
        pool.append(task)
    for j in pool:
        j.join()
    print("exit main .......")




