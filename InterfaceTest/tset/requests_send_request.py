import requests
import json

def getToken():
    url = 'http://apitest.kuaiwen.cn/api/doctor/requiretoken'
    data = {
        "phone": "18617359868",
        "password": "123"
    }
    result = requests.post(url, data)
    return result.json().get('data').get('token')


def getPrescription():
    url = 'http://apitest.kuaiwen.cn/api/doctor/prescription/V2/indexnew?s=NewSubmit&page=1&flag=NewSubmit'
    headers = {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjU5MzQsImlzcyI6Imh0dHA6Ly9hcGl0ZXN0Lmt1YWl3ZW4uY24vYXBpL2RvY3Rvci9yZXF1aXJldG9rZW4iLCJpYXQiOjE1OTQxODAyMjcsImV4cCI6MTU5NDc4NTAyNywibmJmIjoxNTk0MTgwMjI3LCJqdGkiOiJ0Y0ViOFV0bWQ0bzg3TDZhIn0.kSNDHt5iIsi3e3Ab6M3wZ77SReerTmph62m-0-YDAcQ'}

    print(headers)
    httpbin_get = requests.get(url, headers)
    print('httpbin_get: ', httpbin_get.text)


def storePublicPrescription():
    url = 'http://apitest.kuaiwen.cn/api/doctor/prescription/v3/storePublicPrescription'
    data ={
	"keep_secret": "N",
	"is_expedite": "N",
	"medicine_pharmacy_id": "29",
	"usage_others": "需注意少起急，少生气，规律睡眠。",
	"cpms": "",
	"comment": "",
	"usage_medicine_timing": "饭后1小时服",
	"manufacture_id": "4",
	"sex": "M",
	"estimate_day": "2",
	"usage_taboo": ["无"],
	"manufacturePrice": "25",
	"herbs": "[{\"pack_num\":150,\"unit\":\"克\",\"special_manufacture\":\"\",\"is_weight_consistent\":\"Y\",\"id\":\"139\",\"pack_size\":1,\"weight\":150,\"pinyin\":\"gancao, gc, shenggancao_guolao_lingcao_micao_fencao_tiancaogen_tiangancao_tiangenzi_tiancao, sgc_gl_lc_mc_fc_tcg_tgc_tgz_tc\",\"pack_unit\":\"克\",\"alias\":\"生甘草、国老、灵草、蜜草、粉草、甜草根、甜甘草、甜根子、甜草\",\"is_poison\":\"N\",\"pharmacy_herb_id\":3872,\"htcnt\":135391,\"isspecial\":\"N\",\"price\":\"7.01930\",\"l_stockout\":false,\"name\":\"甘草\",\"l_height\":0}]",
	"name": "李圆月",
	"is_save_tpl": "N",
	"price": "0.00",
	"from_pr_id": "1169986",
	"daily_times": "2",
	"diagnoses": "测试",
	"usage_unit": "g",
	"herbPrice": "1052.895",
	"medicinePrice": "0",
	"service_comment": "",
	"cpmPrice": "0",
	"consultPrice": "0.00",
	"age_month": "18,",
	"age": "18",
	"herb_usage": "外用",
	"pharmacy_id": "2",
	"phone": "13692714848",
	"medicines": "",
	"everytimes_usage": "50",
	"shippingInfo": {
		"shipping_city": "广州市",
		"shipping_name": "李圆月",
		"shipping_province_id": "60",
		"shipping_address": "静宁街头的",
		"shipping_city_id": "664",
		"shipping_zone": "李圆月",
		"shipping_province": "广东省",
		"shipping_zone_id": "6255",
		"shipping_phone": "13692714848"
	}
}

    headers = {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjU5MzQsImlzcyI6Imh0dHA6Ly9hcGl0ZXN0Lmt1YWl3ZW4uY24vYXBpL2RvY3Rvci9yZXF1aXJldG9rZW4iLCJpYXQiOjE1OTQxODAyMjcsImV4cCI6MTU5NDc4NTAyNywibmJmIjoxNTk0MTgwMjI3LCJqdGkiOiJ0Y0ViOFV0bWQ0bzg3TDZhIn0.kSNDHt5iIsi3e3Ab6M3wZ77SReerTmph62m-0-YDAcQ",
        "Content-Type":"application/json",
        "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjU5MzQsImlzcyI6Imh0dHA6Ly9hcGl0ZXN0Lmt1YWl3ZW4uY24vYXBpL2RvY3Rvci9yZXF1aXJldG9rZW4iLCJpYXQiOjE1OTM3NDI4NDMsImV4cCI6MTU5NDM0NzY0MywibmJmIjoxNTkzNzQyODQzLCJqdGkiOiJja2RkeFQ4WFZ6R2RyQk9iIn0.zNhHE4O3Fio6z3T8vBk5zZIjcAFWfL4Qhk6EYrceY2c",
        "Cookie":"laravel_session=eyJpdiI6IkJ0c3g1K0tGVFhVN2U5aWRUS21BVWc9PSIsInZhbHVlIjoiM01ZMDFwTlF2bHRMWklHMzFCRXBESTdzT2dDdm5DUjgzVnFQSTR5NzV1V2tTYTFNK0RaWWtHQSsyaTFjRWN3Y3V1WVNCVDVYRExTK1NLUzRnejJZM0E9PSIsIm1hYyI6Ijg5M2YwMThmYzQ0YjFjYTE2NDRmMWFjY2ZhNTdkMjE4MmI0NWQ3YzJkZTExYjI4Yzg1ODMwM2VmMGM0MDg2NmMifQ%3D%3D"
    }
    data = json.dumps(data)
    print(type(data))
    httpbin_post = requests.post(url,headers=headers,data = data)
    print(httpbin_post.text)







storePublicPrescription()