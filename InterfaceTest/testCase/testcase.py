from InterfaceTest.common.configEmail import sendMail
from InterfaceTest.util.util import runTest


def main():
    errorTest = runTest('../testFile/test.xlsx')
    if len(errorTest) > 0:
        html = '<html><body>接口自动化定期扫描，共有 ' + str(len(
            errorTest)) + ' 个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;">接口</th><th style="width:50px;">状态</th><th style="width:200px;">接口地址</th><th>接口返回值</th></tr>'
        for test in errorTest:
            html = html + '<tr><td>' + test.api_purpose + '</td><td>' + str(test.status_code) + '</td><td>' + test.request_url + '</td><td>' + test.text + '</td></tr>'
        html = html + '</table></body></html>'

        sendMail(html)


main()