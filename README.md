# Anti-Captcha Python3 Wrapper

## How to install
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
Returns the solution to the submited captcha

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
