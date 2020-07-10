import base64
import hashlib
import http.client
import json
import os

import sys
import InterfaceTest.common.log
import requests
import xlrd
import pyDes

from InterfaceTest.common.configEmail import sendMail
from InterfaceTest.common.log import LOG
from InterfaceTest.util.testCase import testCase


def runTest(testCaseFile):
    # 获取绝对路径
    testCaseFile = os.path.join(os.getcwd(), testCaseFile)
    log = LOG


    if not os.path.exists(testCaseFile):
        log.error('测试用例文件不存在！！！')
        sys.exit()
    errorcase = []

    data = xlrd.open_workbook(testCaseFile)
    # 获取所有工作表名
    names = data.sheet_names()
    # 获取表的内容
    for i in range(len(names)):
        table = data.sheet_by_name(names[i])
        # 有数据才执行
        if (table.nrows > 1):
            for i in range(1, table.nrows):
                testcase = testCase()
                testcase.active = table.cell(i, 10).value
                # 判断是否需要执行
                if testcase.active.replace('\n', '').replace('\r', '') != 'Yes':
                    continue
                testcase.num = str(int(table.cell(i, 0).value))
                testcase.api_purpose = table.cell(i, 1).value
                testcase.api_host = table.cell(i, 2).value
                testcase.request_url = table.cell(i, 3).value
                testcase.request_method = table.cell(i, 4).value
                testcase.request_data_type = table.cell(i, 5).value
                if table.cell(i, 6).value != '':
                    testcase.request_data = json.loads(table.cell(i, 6).value)
                else:
                    testcase.request_data = table.cell(i, 6).value
                testcase.encryption = table.cell(i, 7).value
                testcase.check_point = table.cell(i, 8).value
                if table.cell(i, 9).value != '':
                    testcase.correlation = json.loads(table.cell(i, 9).value)
                else:
                    testcase.correlation = table.cell(i, 9).value

                # 判断传值类型
                if testcase.request_data_type == 'Form':
                    # 判断是否需要编码
                    if testcase.encryption == 'No':
                        # 判断方法
                        if testcase.request_method == 'POST':
                            try:
                                # 判断是否需要请求关联
                                if testcase.correlation == '':
                                    result = requests.post(url=testcase.api_host + testcase.request_url,
                                                           data=testcase.request_data)
                                    testcase.status_code=result.status_code
                                    testcase.text = result.text
                                    # 判断请求是否成功
                                    if result.status_code == 200:

                                        if testcase.check_point in result.text:
                                            print(testcase.api_purpose + ":成功")

                                            log.info(testcase.num + ' ' + testcase.api_purpose + ' 成功, ')
                                        else:

                                            errorcase.append(testcase)

                                            log.error(
                                                testcase.num + ' ' + testcase.api_purpose + "[ check_point ], 校验失败!!!")
                                            continue
                                    elif result.status_code != 200:
                                        errorcase.append(testcase)
                                        log.error(
                                            testcase.num + ' ' + testcase.api_purpose + ' ' + str(
                                                result.status_code) + ' 请求出错，请检查!!!')
                                        continue
                                else:
                                    result = requests.post(url=testcase.api_host + testcase.request_url,
                                                           data=testcase.request_data, headers=testcase.correlation)
                                    testcase.status_code = result.status_code
                                    testcase.text = result.text
                                    if result.status_code == 200:
                                        if testcase.check_point in result.text:
                                            print("成功")
                                            log.info(testcase.num + ' ' + testcase.api_purpose + ' 成功, ')
                                        else:

                                            errorcase.append(testcase)

                                            log.error(
                                                testcase.num + ' ' + testcase.api_purpose + "[ check_point ], 校验失败!!!")
                                            continue
                                    elif result.status_code != 200:
                                        errorcase.append(testcase)
                                        log.error(
                                            testcase.num + ' ' + testcase.api_purpose + ' ' + str(
                                                result.status_code) + ' 请求出错，请检查!!!')
                                        continue

                            except Exception as e:
                                errorcase.append(testcase)
                                log.error(
                                    testcase.num + ' ' + testcase.api_purpose + ' 请求的数据有误，请检查[correlation]字段!!!')
                                continue
                        elif testcase.request_method == 'GET':
                            try:
                                # 判断是否需要请求关联
                                if testcase.correlation == '':
                                    result = requests.get(testcase.api_host + testcase.request_url
                                                          )
                                    testcase.status_code = result.status_code
                                    testcase.text = result.text
                                    # 判断请求是否成功
                                    if result.status_code == 200:

                                        if testcase.check_point in result.text:

                                            log.info(testcase.num + ' ' + testcase.api_purpose + ' 成功, ')
                                        else:

                                            errorcase.append(testcase)

                                            log.error(
                                                testcase.num + ' ' + testcase.api_purpose + "[ check_point ], 校验失败!!!")
                                            continue
                                    elif result.status_code != 200:
                                        errorcase.append(testcase)
                                        log.error(
                                            testcase.num + ' ' + testcase.api_purpose + ' ' + str(
                                                result.status_code) + ' 请求出错，请检查!!!')
                                        continue
                                else:

                                    result = requests.get(testcase.api_host + testcase.request_url,
                                                          testcase.correlation)
                                    testcase.status_code = result.status_code
                                    testcase.text = result.text

                                    if result.status_code == 200:
                                        if testcase.check_point in result.text:
                                            print(testcase.api_purpose + ":成功")
                                            log.info(testcase.num + ' ' + testcase.api_purpose + ' 成功, ')
                                        else:

                                            errorcase.append(testcase)

                                            log.error(
                                                testcase.num + ' ' + testcase.api_purpose + "[ check_point ], 校验失败!!!")
                                            continue
                                    elif result.status_code != 200:
                                        errorcase.append(testcase)
                                        log.error(
                                            testcase.num + ' ' + testcase.api_purpose + ' ' + str(
                                                result.status_code) + ' 请求出错，请检查!!!')
                                        continue

                            except Exception as e:
                                errorcase.append(testcase)
                                log.error(
                                    testcase.num + ' ' + testcase.api_purpose + ' 请求的数据有误，请检查[correlation]字段!!!')
                                continue
                        else:
                            errorcase.append(testcase)
                            log.error(testcase.num + ' ' + testcase.api_purpose + "[ request_method ], 不识别!!!")
                            continue
                    elif testcase.encryption == 'MD5':
                        print('MD5未完成')
                    elif testcase.encryption == 'DES':
                        print('DES未完成')
                    else:
                        errorcase.append(testcase)
                        log.error(testcase.num + ' ' + testcase.api_purpose + "[ encryption ], 不识别!!!")
                        continue
                elif testcase.request_data_type == 'Data':
                    print('Data未完成')
                elif testcase.request_data_type == 'File':
                    print('File未完成')
                else:
                    errorcase.append(testcase)
                    log.error(testcase.num + ' ' + testcase.api_purpose + "[ request_data_type ], 不识别!!!")
                    continue
    return errorcase

# 获取md5验证码
def getMD5(url, postData):
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'X-Requested-With': 'XMLHttpRequest'}
    conn = http.client.HTTPConnection('this.ismyhost.com')
    conn.request('POST', '/get_isignature', postData, headers=headers)
    response = conn.getresponse()
    return response.status, response.read()


# hash1加密
def hash1Encode(codeStr):
    hashobj = hashlib.sha1()
    hashobj.update(codeStr.encode('utf-8'))
    return hashobj.hexdigest()


# DES加密
def desEncode(desStr):
    k = pyDes.des('secretKEY')
    encodeStr = base64.b64encode(k.encrypt(json.dumps(desStr)))
    return encodeStr


# 字典排序
def encodePostStr(postData):
    keyDict = {'key': 'secretKEY'}
    mergeDict = dict(postData, **keyDict)
    mergeDict = sorted(mergeDict.items())
    postStr = ''
    for i in mergeDict:
        postStr = postStr + i[0] + '=' + i[1] + '&'
    postStr = postStr[:-1]
    hashobj = hashlib.sha1()
    hashobj.update(postStr.encode('utf-8'))
    token = hashobj.hexdigest()
    postData['token'] = token
    return desEncode(postData)


# 发送通知邮件



