from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.common.exceptions import NoSuchElementException
# desired_caps={
#     "platformName": "Android",
#     "platformVersion": "5.1.1",
#     "deviceName": "emulator-5554",
#     "appPackage": "com.netease.cloudmusic",
#     "appActivity": ".activity.MainActivity",
#     "unicodeKeyboard": True,
#     "resetKeyboard": True,
#     "automationName": "uiautomator2",
#     "noReset": True
# }
# driver= webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


class Application(object):
    """ app application class define attr driver only  once by getter setter """

    def __init__(self, app_driver=None):
        self.__driver = app_driver

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver):
        self.__driver = driver
        if self.__driver is None:
            raise ValueError("driver instance is {}".format(self.__driver))

    def access_id(self, access_id):
        return self.__driver.find_element_by_accessibility_id(access_id)

    def uiautomator_text(self, text):
        """
        @Uasge::
        函数返回   |      函数         | 说明      |        用法
        UiSelector| text(String text)|根据“控件text属性的内容”构造出UiSelector对象| UiSelector s = new UiSelector().text("发现");
        UiSelector|textContains(String text)|根据“控件text属性包含的内容”构造UiSelector对象 |UiSelector s = new UiSelector().textContains("现")
        UiSelector|textMatches(String regex) |根据“控件text属性正则表达式的内容”构造出UiSelector对象|正则表达式语法参考网上资料即可。
       UiSelector|textStartsWith(String text)|根据“控件text属性开始的内容”构造出UiSelector对象|UiSelector s = new UiSelector().textStartsWith("发");
        """
        return self.__driver.find_element_by_android_uiautomator("new UiSelector().text(\"{}\")".format(text))

    def uiautomator_descript(self, content_desc):
        """
        @Usage::类比 uiautomator_text:
        UiSelector|description(String desc)|根据“控件content-desc属性的内容”构造出UiSelector对象
        UiSelector|descriptionContains(String desc)|包含**
        UiSelector|descriptionMatches(String regex)|正则
        UiSelector|descriptionStartsWith(String desc)|开始
        """
        return self.__driver.find_element_by_android_uiautomator(
            "new UiSelector().description(\"{}\")".format(content_desc))

    def find_by(self, loc):
        """
        @:param : by
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector
        """
        return self.__driver.find_element(*loc)

    def finds_by(self, loc):
        return self.__driver.find_elements(*loc)

    def location_click(self, loc):
        """
        to locate element and click it
        @return None
        @:param : loc is  the location of web element like: (By.ID,'com.netease.cloudmusic:id/password')

        """
        self.find_by(loc).click()

    def location_input(self, loc, send_key=""):
        """
        to locate element and input something
        @:return None
        @:param: loc is the locator of element in web like:(By.ID,'com.netease.cloudmusic:id/password')
        @:param: send_key is the  content of function of send_keys(content)
        """

        self.find_by(loc).send_keys(send_key)

    def resource_id(self, idx):
        """
        :param idx: the location of element by resource_id like:
        (By.ID,'com.netease.cloudmusic:id/password')
        :return: web element  object
        """

        return self.__driver.find_element_by_id(idx)

    def exist_element(self,loc):
        """
        @:return  True if exist else False,default False .
        @:param loc is location of element like :
        (By.ID,'com.netease.cloudmusic:id/password')
        """
        exist = False
        try:
            exist = True if self.find_by(loc) else False
        except NoSuchElementException as e:
            print("{}".format("Not found trial netease element, so skip login... "))
        return exist

    def page_exists(self,target):
        sources = self.__driver.page_source
        result = True if target in sources else False
        return result

    def tap_point(self,position,times):
        """点击持续时间:
        tap([坐标]，持续点击时间)

        """
        self.__driver.tap(*position,times)

    def press_event(self,android_event_code:(str,int)):
        """
        Android only. Possible keycodes can be found
        in http://developer.android.com/reference/android/view/KeyEvent.html.
        example backspace:  press_event(66)
        :param android_event_code:
        :return:
        键名      ||         描述   || 键值
        KEYCODE_CALL        拨号键      5
        KEYCODE_ENDCALL     挂机键      6
        KEYCODE_HOME        按键Home    3
        KEYCODE_MENU        菜单键      82
        KEYCODE_BACK        返回键      4
        KEYCODE_SEARCH      搜索键      84
        KEYCODE_CAMERA      拍照键      27
        KEYCODE_FOCUS       拍照对焦键  80
        KEYCODE_POWER       电源键      26
        KEYCODE_NOTIFICATION 通知键      83
        KEYCODE_MUTE        话筒静音键   91
        KEYCODE_VOLUME_MUTE 扬声器静音键  164
        KEYCODE_VOLUME_UP   音量增加键   24
        KEYCODE_VOLUME_DOWN 音量减小键   25
        """
        self.__driver.press_keycode(android_event_code)

    def start_app(self):
        """ start application """
        self.__driver.launch_app()

    def stop_app(self):
        """ kill application """
        self.__driver.close_app()

    def get_winSize(self):
        """
        @:return: screen (width,height) :
        """
        x = self.__driver.get_window_size()['width']
        y = self.__driver.get_window_size()['height']
        return (x, y)

    def get_text(self,element):
        return element.text

    def all_contexts(self):
        """get all contexts"""
        return self.__driver.contexts

    def current_context(self):
        return self.__driver.current_context

    def switch_to_context(self,ctx):
        """ change into  context"""
        self.__driver.switch_to.context(ctx)

    def set_netType(self,code:int):
        """
        @:type 设置网络类型
        | 值 (别名)           | 数据连接 | Wifi 连接 | 飞行模式 |
        | ------------------ | ---- | ---- | ------------- |
        | 0 (什么都没有)       | 0    | 0    | 0 |
        | 1 (飞行模式)         | 0    | 0    | 1 |
        | 2 (只有Wifi)        | 0    | 1    | 0 |
        | 4 (只有数据连接)     | 1    | 0    | 0 |
        | 6 (开启所有网络)     | 1    | 1    | 0 |
        """
        self.__driver.set_network_connection(code)

    def scroll(self,start,end):
        """滚动元素
        @:param: start,end -> 起始元素，结束元素
        """
        self.__driver.scroll(start,end)

    def multi_swipeScreen(self):
        """
        :return: None
        TouchAction对象包含（tab）、press（短按）、move_to（滑动到某个坐标）等方法
        通过TouchAction对象，添加tap、move_to等操作，然后perform()执行，可以实现解锁屏幕等功能
        规范中的可用事件有：
         * 短按 (press)
         * 释放 (release)
         * 移动到 (moveTo)
         * 点击 (tap)
         * 等待 (wait)
         * 长按 (longPress)
         * 取消 (cancel)
         * 执行 (perform)
        """
        action = TouchAction(self.__driver)
        action.press(x=220, y=700).move_to(x=840, y=700).move_to(x=220, y=1530).move_to(x=840,
                                                                                        y=1530).release().perform()

    def multi_action_event(self,el):
        """
        @:param: ().add()添加多个TouchAction操作，最后调用perform()一起执行这些操作
        MultiAction是针对多点触控操作的，是TouchAction的一个补充模块
        多点触摸对象是触摸动作的集合。
        多点触控手势只有两种方法，即添加和执行。
        add用于添加另一个触摸操作到多点触摸。
        当perform执行被调用时，添加到多点触摸的所有触摸动作都被发送到AppII，并执行，
        就像它们同时发生一样。appium首先执行所有触摸动作的第一个事件，然后执行第二个，等等。
        """
        action0 = TouchAction().tap(el)
        action1 = TouchAction().tap(el)
        self.__driver.MultiAction().add(action0).add(action1).perform()

    def swipe_to(self,x1,x2,y1,y2,duration):
        self.__driver.swipe(x1, y1, x2, y2,duration)

    def getSize(self):
        x = self.__driver.get_window_size()['width']
        y = self.__driver.get_window_size()['height']
        return (x, y)

    # 屏幕向上滑动
    def swipeUp(self,driver, t=1000):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipeDown(self,driver, t=1000):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipLeft(self,driver, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipRight(self,driver, t=1000):
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        driver.swipe(x1, y1, x2, y1, t)

    def open_notifications(self):
        self.__driver.open_notifications()