import requests
import time


class py2c():
    URL_POST = "https://2captcha.com/in.php"
    URL_GET = "https://2captcha.com/res.php"

    _request = None
    _api_key = None

    def __init__(self,api_key):
        self._api_key = api_key

    def getBalance(self):
        payload = {
            'key': self._api_key,
            'action': 'getbalance',
            'json': 1,
        }
        try:
            r = requests.get(self.URL_GET, params=payload).json()
            if r['status'] == 1:
                return r['request']
            else:
                raise Exception
        except Exception as e:
            print("[py2captcha] > Failed getting balance. [{}]".format(e))
            return False

    def reportIncorrect(self):
        payload = {
            'key': self._api_key,
            'action': 'reportbad',
            'id': self._request,
            'json': 1,
        }
        r = requests.get(self.URL_GET, params=payload).json()
        if r['status'] == 1:
            print("[py2captcha] > Sucessfully reported Incorrect resolve.")
        else:
            print("[py2captcha] > Failed reporting Incorrect. [{}]".format(r['request']))
            return False

    def reportCorrect(self):
        payload = {
            'key': self._api_key,
            'action': 'reportgood',
            'id': self._request,
            'json': 1,
        }
        r = requests.get(self.URL_GET, params=payload).json()
        if r['status'] == 1:
            print("[py2captcha] > Sucessfully reported Correct resolve.")
        else:
            print("[py2captcha] > Failed reporting Correct. [{}]".format(r['request']))
            return False

    def checkResolve(self):
        if self._request:
            payload = {
                'key': self._api_key,
                'action': 'get',
                'id': self._request,
                'json': 1,
            }
            r = requests.get(self.URL_GET, params=payload).json()
            while r['status'] != 1:
                if r['request'] != "CAPCHA_NOT_READY":
                    print("[py2captcha] > Failed getting Resolve. [{}]".format(r['request']))
                    return False
                time.sleep(5)
                r = requests.get(self.URL_GET, params=payload).json()
            return r['request']

    def solveCaptcha(self,img_base64):
        payload = {
            'key': self._api_key,
            'body': img_base64,
            'method': 'base64',
            'json': 1,
            'soft_id': 8942337,
        }
        r = requests.post(self.URL_POST, data=payload).json()
        if r['status'] == 1:
            self._request = r['request']
            time.sleep(5)
            return self.checkResolve()
        else:
            print("[py2captcha] > Failed sending solve request. [{}]".format(r['request']))
            return False

    def solveReCaptcha(self,key,url):
        payload = {
            'key': self._api_key,
            'googlekey': key,
            'pageurl': url,
            'method': 'userrecaptcha',
            'json': 1,
            'soft_id': 8942337,
        }
        r = requests.post(self.URL_POST, data=payload).json()
        if r['status'] == 1:
            self._request = r['request']
            time.sleep(15)
            return self.checkResolve()
        else:
            print("[py2captcha] > Failed sending solve request. [{}]".format(r['request']))
            return False
