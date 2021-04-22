from selenium import webdriver
import time
import kullaniciBilgileri as kb

class Browser:
    def __init__(self,link):
        self.link = link
        self.browser = webdriver.Chrome("/Users/senol/Desktop/chromedriver")
        Browser.goInstagram(self)
    def goInstagram(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.login(self)
        Browser.getFollowers(self)

    def getFollowers(self):
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(4)
        Browser.scrollDown(self)
        takipciler = self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
        
        sayac = 0
        followersList = []
        for takipci in takipciler:
            sayac +=1
            followersList.append(takipci.text)
            print(str(sayac) + "-->" + takipci.text)
            with open("followers.txt", "w", encoding="UTF-8") as file:
                for fol in followersList:
                    file.write(fol + "\n")

    def scrollDown(self):
        jsKomut = """
        sayfa = document.querySelector('.isgrP');
        sayfa.scrollTo(0,sayfa.scrollHeight);
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu;
        """
        sayfaSonu = self.browser.execute_script(jsKomut)
        while True:
            son = sayfaSonu
            time.sleep(2)
            sayfaSonu = self.browser.execute_script(jsKomut)
            # indirilecek sayfa kalamdıysa
            if son == sayfaSonu:
                break
    def login(self):
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")
        # dosyadaki kullanıcı bilgielrimiz gönderdik
        username.send_keys("Username")
        password.send_keys("Password")
        loginBtn = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div")
        loginBtn.click()
        time.sleep(4)

        self.browser.get(self.link + "/" + kb.userName)
        time.sleep(3)

kur = Browser("https://www.instagram.com")
print(kur)