import requests
from lxml import etree
from client.driver import Driver

class Base:

    def __init__(self):
        self.session = requests.Session()

    def request(self, url, encoding='gbk'):
        response = self.session.get(url, verify=False)
        if encoding:
            response.encoding = encoding
        if response.status_code != 200:
            return response.status_code
        return response

    def parse(self, html, xpath):
        return etree.HTML(html).xpath(xpath)

    def output(self, url, xpath):
        return self.parse(self.request(url).text, xpath)





if __name__ == '__main__':
    instance = Driver()
    instance.get("https://www.baidu.com")
    print(instance.get_title())
