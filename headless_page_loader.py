__author__ = 'waf04'
from selenium import webdriver  # pip install selenium
from bs4 import BeautifulSoup  # pip install beautifulsoup
from pyvirtualdisplay import Display
import selenium.webdriver.support.ui as ui
import traceback


class HeadlessBrowser():

    V_DISPLAY = None
    BROWSER = None

    def __init__(self, onLinux):

        #init display
        if onLinux:
            self.V_DISPLAY = Display(visible=0, size=(800, 600))
            self.V_DISPLAY.start()

        #init browser
        self.BROWSER = webdriver.Firefox()
        self.BROWSER.set_page_load_timeout(15)  # seconds

    def getJsPageAsSoupFromUrl(self, requestUrl):

        """
        Renders a JS page on a headless browser and returns a SOUP object
        :rtype : BeautifulSoup
        :param requestUrl:
        :return:
        """
        sourceSoup = None
        try:
            self.BROWSER.get(requestUrl)

            #convert to string and then to a soup object
            page = self.BROWSER.page_source.encode('utf-8', 'ignore')
            sourceSoup = BeautifulSoup(page)

        except Exception:
            traceback.print_exc()
        return sourceSoup

    def getJsPageAsHTMLStringFromUrl(self, requestUrl):

        """
        Renders a JS page on a headless browser and returns a HTML string
        :param requestUrl:
        :rtype : str
        :return:
        """
        self.BROWSER.get(requestUrl)

        #convert to string and then to a soup object
        page = self.BROWSER.page_source.encode('utf-8', 'ignore')
        return page

    def getJsPageAsSoupFromUrlWaitUntilLoaded(self, requestUrl):

        """
        Renders a JS page on a headless browser and returns a SOUP object
        :rtype : BeautifulSoup
        :param requestUrl:
        :return:
        """
        #start headless browser if on Linux

        sourceSoup = None

        try:
            self.BROWSER.get(requestUrl)
            wait = ui.WebDriverWait(self.BROWSER, 40)  # timeout after 40 seconds

            #convert to string and then to a soup object
            page = self.BROWSER.page_source.encode('utf-8', 'ignore')
            sourceSoup = BeautifulSoup(page)

        except Exception as e:
            print(e)
            traceback.print_exc()

        return sourceSoup

    def cleanUp(self):

        if self.BROWSER is not None:
            self.BROWSER.close()
            self.BROWSER.quit()
            self.BROWSER = None

        if self.V_DISPLAY is not None:
            self.V_DISPLAY.stop()
            self.BROWSER = None











