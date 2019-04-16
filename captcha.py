import requests
import time


def getTaskResult(clientKey, taskId):
    clientKey = str(clientKey)
    taskId = int(taskId)
    postData = {
        "clientKey": clientKey,
        "taskId": taskId
    }
    while True:
        r = requests.post('https://api.anti-captcha.com/getTaskResult', json=postData)
        response = r.json()
        if response['status'] == 'ready':
            break
        elif response['status'] == 'processing':
            pass
        else:
            print(response['status'])
        time.sleep(5)
    return response['solution']


def getBalence(clientKey):
    clientKey = str(clientKey)
    postData = {
        "clientKey": clientKey
    }
    r = requests.post('https://api.anti-captcha.com/getBalance', json=postData)
    response = r.json()
    if response['errorId'] != 0:
        raise Exception(f'{response["errorCode"]} : {response["errorDescription"]}')
    else:
        balence = float(response['balance'])
        return balence


def ImageToTextTask(clientKey, body):
    clientKey = str(clientKey)
    body = str(body)
    postData = {
        "clientKey": clientKey,
        "task":
            {
                "type": "ImageToTextTask",
                "body": body
            }
    }
    r = requests.post('http://api.anti-captcha.com/createTask', json=postData)
    response = r.json()
    return response['taskId']


def NoCaptchaTask(clientKey, proxyType, proxy, websiteURL, websiteKey,  userAgent):
    proxy = str(proxy).split(":")
    proxyAddress = str(proxy[0])
    proxyPort = int(proxy[1])
    proxyType = str(proxyType)
    clientKey = str(clientKey)
    websiteKey = str(websiteKey)
    websiteURL = str(websiteURL)
    userAgent = str(userAgent)
    postData = {
        "clientKey": clientKey,
        "task":
            {
                "type": "NoCaptchaTask",
                "websiteURL": websiteURL,
                "websiteKey": websiteKey,
                "proxyType": proxyType,
                "proxyAddress": proxyAddress,
                "proxyPort": proxyPort,
                "userAgent": userAgent
            }
    }
    r = requests.post('http://api.anti-captcha.com/createTask', json=postData)
    response = r.json()
    return response['taskId']


def NoCaptchaTaskProxyless(clientKey, websiteURL, websiteKey):
    clientKey = str(clientKey)
    websiteKey = str(websiteKey)
    websiteURL = str(websiteURL)
    postData = {
        "clientKey": clientKey,
        "task":
            {
                "type": "NoCaptchaTaskProxyless",
                "websiteURL": websiteURL,
                "websiteKey": websiteKey
            }
    }
    r = requests.post('http://api.anti-captcha.com/createTask', json=postData)
    response = r.json()
    return response['taskId']


def FunCaptchaTask(clientKey, proxy, websiteURL, websitePublicKey, proxyType, userAgent):
    proxy = str(proxy).split(":")
    proxyAddress = str(proxy[0])
    proxyPort = int(proxy[1])
    proxyType = str(proxyType)
    clientKey = str(clientKey)
    websitePublicKey = str(websitePublicKey)
    websiteURL = str(websiteURL)
    userAgent = str(userAgent)
    postData = {
        "clientKey": clientKey,
        "task":
            {
                "type": "FunCaptchaTask",
                "websiteURL": websiteURL,
                "websitePublicKey": websitePublicKey,
                "proxyType": proxyType,
                "proxyAddress": proxyAddress,
                "proxyPort": proxyPort,
                "userAgent": userAgent
            }
    }
    r = requests.post('http://api.anti-captcha.com/createTask', json=postData)
    response = r.json()
    return response['taskId']


def FunCaptchaTaskProxyless(clientKey, websiteURL, websitePublicKey):
    clientKey = str(clientKey)
    websitePublicKey = str(websitePublicKey)
    websiteURL = str(websiteURL)
    postData = {
        "clientKey": clientKey,
        "task":
            {
                "type": "FunCaptchaTaskProxyless",
                "websiteURL": websiteURL,
                "websitePublicKey": websitePublicKey
            }
    }
    r = requests.post('http://api.anti-captcha.com/createTask', json=postData)
    response = r.json()
    return response['taskId']


def SquareNetTextTask(clientKey, body, objectName, rowsCount, columnsCount):
    clientKey = str(clientKey)
    body = str(body)
    objectName = str(objectName)
    rowsCount = int(rowsCount)
    columnsCount = int(columnsCount)

    postData = {
        "clientKey": clientKey,
        "task":
            {
                "type": "SquareNetTask",
                "body": body,
                "objectName": objectName,
                "rowsCount": rowsCount,
                "columnsCount": columnsCount
            }
    }
    r = requests.post('http://api.anti-captcha.com/createTask', json=postData)
    response = r.json()
    return response['taskId']


def GeeTestTask(clientKey, proxy, websiteURL, gt, challenge, proxyType, userAgent):
    proxy = str(proxy).split(":")
    proxyAddress = str(proxy[0])
    proxyPort = int(proxy[1])
    proxyType = str(proxyType)
    clientKey = str(clientKey)
    gt = str(gt)
    challenge = str(challenge)
    websiteURL = str(websiteURL)
    userAgent = str(userAgent)
    postData = {
        "clientKey": clientKey,
        "task":
            {
                "type": "GeeTestTask",
                "websiteURL": websiteURL,
                "gt": gt,
                "challenge": challenge,
                "proxyType": proxyType,
                "proxyAddress": proxyAddress,
                "proxyPort": proxyPort,
                "userAgent": userAgent
            }
    }
    r = requests.post('http://api.anti-captcha.com/createTask', json=postData)
    response = r.json()
    return response['taskId']


def GeeTestTaskProxyless(clientKey, websiteURL, gt, challenge):
    clientKey = str(clientKey)
    gt = str(gt)
    challenge = str(challenge)
    websiteURL = str(websiteURL)
    postData = {
        "clientKey": clientKey,
        "task":
            {
                "type": "GeeTestTaskProxyless",
                "websiteURL": websiteURL,
                "gt": gt,
                "challenge": challenge
            }
    }
    r = requests.post('http://api.anti-captcha.com/createTask', json=postData)
    response = r.json()
    return response['taskId']
