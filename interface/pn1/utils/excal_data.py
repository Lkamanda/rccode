class ExcelVariable:
    caseID = 0
    title = 1
    url = 2
    request_data = 3
    expect = 4
    result: int = 5


def getCaseID():
    return ExcelVariable.caseID


def getUrl():
    return ExcelVariable.url


def get_request_data():
    return ExcelVariable.request_data


def getExcept():
    return ExcelVariable.expect


def getResult():
    return ExcelVariable.result

def getHeaderValue():
    """获取请求头"""
    headers = {
        "Content-Type": "text/html;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/73.0.3683.86 Safari/537.36",
        "Referer": "https://www.lagou.com/jobs/list_%E6%8E%A5%E5%8F%A3%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95?px"
                   "=default&gj=%E4%B8%8D%E8%A6%81%E6%B1%82&city=%E5%8C%97%E4%BA%AC",
        "Cookie": "_ga=GA1.2.397646582.1553783320; user_trace_token=20190328222838-c742d80d-5165-11e9-b87d-5254005c3644; LGUID=20190328222838-c742df34-5165-11e9-b87d-5254005c3644; _gid=GA1.2.801452657.1553783321; gate_login_token=edf5fc8a1ce43b2337c0adb1e42b4b6d1882a223aff640a70281e8672512b01a; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=ABAAABAAAGGABCBFCA63D3A42D4A73D2C59C1E16F344C18; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1553783320,1553816756; _putrc=1B2EB510BFC137E6123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B73553; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; _gat=1; LGSID=20190329184518-be9f5f7a-520f-11e9-b8d4-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fmycenter%2Fdelivery.html%3Ftag%3D0; hasDeliver=7; TG-TRACK-CODE=index_search; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1553856482; LGRID=20190329184918-4d829b3f-5210-11e9-8591-525400f775ce; SEARCH_ID=df76fba54fa9439a8499e5c0f8f2b045"
    }
    return headers
