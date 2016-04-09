from bs4 import BeautifulSoup
from time import sleep
from random import randint
import requests
import traceback


"""
Interface for loading pages using a url
"""
class PageLoader():

    @staticmethod
    def load(url, download_timeout=30, download_attempts=3, keep_alive=False):
        """
        Downloads the given url and returns in bs4 format
        :param: Page url to download
        :return: bs4 object
        """

        # get document in soup format
        headers = {'Connection':'close'} if not keep_alive else None
        document = PageLoader.__download_document(url, download_attempts, download_timeout, headers)

        # if document failed to download, then return None
        if not document:
            return None

        soup = BeautifulSoup(document.content)
        return soup


    @staticmethod
    def __download_document(url, attempts, download_timeout, headers):

        """
        Try to download the page 
        :param url:
        :param attempts:
        :return:
        """
        document = None
        for i in range(0,attempts):
            try:
                #try to download url
                document = requests.get(url, timeout=download_timeout, headers=headers)
                break
            except Exception:
                traceback.print_exc()

            if document is None:
                print('doc failed to download. Trying again')
                sleep(randint(1, 5))
            else:
                break

        return  document
