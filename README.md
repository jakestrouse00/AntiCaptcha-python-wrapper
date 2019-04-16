# Anti-Captcha Python3 Wrapper

## How to implement
Drag and drop captcha.py into your project folder

Using the API in your project:
```python
from captcha import *
```

## Get Balence
To get an account's balence:
```python
from captcha import *
bal = getBalence('399f26620d1f4c6dc65b182876cb9')
print(bal)
```
This will return a float

## getTaskResult
#### Paramaters

| Paramater        | Type           | Value  |
| -------------|-------------| -----|
| clientKey| String | The client's API key |
| taskId| Integer| ID which was obtained in createTask methods|

How this is used with the API:

```python
from captcha import *
clientKey = ' '
taskId = 1234
response = getTaskResult(clientKey,taskId)
print(response)
```
Returns the solution to the submited captcha in json

## CreateTask Methods

### ImageToTextTask
#### Paramaters

| Paramater        | Type           | Value  |
| -------------|-------------| -----|
| clientKey| String | The client's API key |
| body| String| File body encoded in base64. Make sure to send it without line breaks.|

How this is used with the API:

```python
from captcha import *
clientKey = ' '
body = 'ImageFileInBase64'
response = ImageToTextTask(clientKey,body)
print(response)
```
Returns the taskId

### NoCaptchaTask
#### Paramaters

| Paramater        | Type           | Value  |
| -------------|-------------| -----|
| clientKey| String | The client's API key |
| proxy| String| Proxy for solving. (must be in the format: proxy:port)|
| proxyType| String| Proxy type for the above proxy|
| websiteURL| String| URL on which the captcha is located|
| websiteKey| String| Recaptcha website key <div class="g-recaptcha" data-sitekey="THAT_ONE"></div> |
| userAgent| String| 	Browser's User-Agent which is used in emulation. It is required that you use a signature of a modern browser, otherwise Google will ask you to "update your browser".|


How this is used with the API:

```python
from captcha import *
clientKey = ' '
proxyType = 'http'
proxy = '8.8.8.8:8080'
websiteURL = 'http:\/\/mywebsite.com\/recaptcha\/test.php'
websiteKey = 'Lc_aCMTAAAAABx7u2N0D1XnVbI_v6ZdbM6rYf16'
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
response = NoCaptchaTask(clientKey,proxyType,proxy,websiteURL,websiteKey,userAgent)
print(response)
```
Returns the taskId

### NoCaptchaTaskProxyless
#### Paramaters

| Paramater        | Type           | Value  |
| -------------|-------------| -----|
| clientKey| String | The client's API key |
| websiteURL| String| URL on which the captcha is located|
| websiteKey| String| Recaptcha website key <div class="g-recaptcha" data-sitekey="THAT_ONE"></div> |


How this is used with the API:

```python
from captcha import *
clientKey = ' '
websiteURL = 'http:\/\/mywebsite.com\/recaptcha\/test.php'
websiteKey = 'Lc_aCMTAAAAABx7u2N0D1XnVbI_v6ZdbM6rYf16'
response = NoCaptchaTask(clientKey,websiteURL,websiteKey)
print(response)
```
Returns the taskId


### FunCaptchaTask
#### Paramaters

| Paramater        | Type           | Value  |
| -------------|-------------| -----|
| clientKey| String | The client's API key |
| proxy| String| Proxy for solving. (must be in the format: proxy:port)|
| proxyType| String| Proxy type for the above proxy|
| websiteURL| String| URL on which the captcha is located|
| websitePublicKey| String| Funcaptcha public key <div id="funcaptcha" data-pkey="THIS_ONE"></div>|
| userAgent| String| 	Browser's User-Agent which is used in emulation. It is required that you use a signature of a modern browser, otherwise Google will ask you to "update your browser".|


How this is used with the API:

```python
from captcha import *
clientKey = ' '
proxyType = 'http'
proxy = '8.8.8.8:8080'
websiteURL = 'http:\/\/mywebsite.com\/recaptcha\/test.php'
websitePublicKey = 'DE0B0BB7-1EE4-4D70-1853-31B835D4506B'
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
response = FunCaptchaTask(clientKey,proxyType,proxy,websiteURL,websitePublicKey)
print(response)
```
Returns the taskId


### FunCaptchaTaskProxyless
#### Paramaters

| Paramater        | Type           | Value  |
| -------------|-------------| -----|
| clientKey| String | The client's API key |
| websiteURL| String| URL on which the captcha is located|
| websitePublicKey| String| Funcaptcha public key <div id="funcaptcha" data-pkey="THIS_ONE"></div>|


How this is used with the API:

```python
from captcha import *
clientKey = ' '
websiteURL = 'http:\/\/mywebsite.com\/recaptcha\/test.php'
websitePublicKey = 'DE0B0BB7-1EE4-4D70-1853-31B835D4506B'
response = FunCaptchaTask(clientKey,websiteURL,websitePublicKey)
print(response)
```
Returns the taskId


### SquareNetTextTask
#### Paramaters

| Paramater        | Type           | Value  |
| -------------|-------------| -----|
| clientKey| String | The client's API key |
| body| String| File body encoded in base64. Make sure to send it without line breaks.|
| objectName| String| Name of the object. Example: banana|
| rowsCount| Integer| Number of grid rows. Min 2, max 5|
| columnsCount| Integer| Number of grid columns. Min 2, max 5|

returns the taskId
### GeeTestTask
#### Paramaters

| Paramater        | Type           | Value  |
| -------------|-------------| -----|
| clientKey| String | The client's API key |
| proxy| String| Proxy for solving. (must be in the format: proxy:port)|
| proxyType| String| Proxy type for the above proxy|
| websiteURL| String| URL on which the captcha is located|
| gt| String| The domain key|
|challenge|String| Changing token key. Make sure to grab fresh one for each captcha, otherwise you will be charged for error task.|
| userAgent| String| 	Browser's User-Agent which is used in emulation. It is required that you use a signature of a modern browser, otherwise Google will ask you to "update your browser".|

Returns the taskId

### GeeTestTaskProxyless
#### Paramaters

| Paramater        | Type           | Value  |
| -------------|-------------| -----|
| clientKey| String | The client's API key |
| websiteURL| String| URL on which the captcha is located|
| gt| String| The domain key|
|challenge|String| Changing token key. Make sure to grab fresh one for each captcha, otherwise you will be charged for error task.|

Returns the taskId

## Example
### NoCaptchaTaskProxyless full example
```python
from captcha import *

clientKey = 'dce6bcbb1a728ea8d871de6d169a2057'
websiteURL = 'http:\/\/mywebsite.com\/recaptcha\/test.php'
websiteKey = 'Lc_aCMTAAAAABx7u2N0D1XnVbI_v6ZdbM6rYf16'
response = NoCaptchaTask(clientKey, websiteURL, websiteKey)

result = getTaskResult(clientKey, response)
# result is returned as json

solution = result['gRecaptchaResponse']
print(solution)
```
