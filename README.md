<h1 align="center">Welcome to basicpy2captcha python module👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.2-blue.svg?cacheSeconds=2592000" />
</p>

> A basic python 2captcha.com module

## Install

```sh
pip install basicpy2captcha
```

## Usage

```py
import base64
import basicpy2captcha


py2c = captcha.py2c("YOUR_2CAPTCHA_API_KEY")

#Text Image:
with open("captcha.png", "rb") as f:
    img_b64 = base64.b64encode(f.read())

solved = py2c.solveCaptcha(img_b64)
print(solved)


#ReCaptcha:
key = py2c.get_sitekey(driver) #driver - selenium webbrowser object
token = solveReCaptcha(key,driver.current_url)
if token:
  driver.execute_script(
      "document.getElementById('g-recaptcha-response').innerHTML='{}';".format(token)
  )
  
  
#getBalance:
balance = py2c.getBalance()
print(balance)

#report Correct resolve:
py2c.reportCorrect()

#report Incorrect resolve:
py2c.reportIncorrect()
```

## Show your support

Give a ⭐️ if this project helped you!
