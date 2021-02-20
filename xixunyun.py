

import requests
import json
import time 

#习讯云签到脚本
   
data={'account':'15362105907',#账号
      'app_id':'cn.vanber.xixunyun.saas',
      'app_version':'4.1.5',
      'key':'',
      'model':'SM-G955N',
      'password':'Aa85595698',#密码
      'platform':'2',
      'registration_id':'160a3797c8437218079',
      'request_source':'3',
      'school_id':'177',#学校代码
      'system':'4.4.2',
      'uuid':'48:45:20:B9:D7:19'}
login_header={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '227',
        'Host': 'api.xixunyun.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.8.1',

}
login_url=' https://api.xixunyun.com/login/api?from=app&version=4.1.5&platform=android&entrance_year=0&graduate_year=0'
request=requests.post(url=login_url,headers=login_header,data=data)
login_data=json.loads(request.text)#登陆成功后返回的信息
token=login_data['data']['token']
time.sleep(1)
#经纬度地址
latitude=''#维度
longitude=''#经度
print(login_data)
sign_url='https://api.xixunyun.com/signin?token='+token+'&from=app&version=4.1.5&platform=android&entrance_year=0&graduate_year=0 '
sign_data={'address':'113.463549,22.549778',#签到地址
           'address_name':'张家边幼儿园',#签到地点名称
           'change_sign_resource':'0',
           'comment':'',
           'latitude':latitude,
           'longitude':longitude,
           'remark':'0',
    
    }
sign_request=requests.post(url=sign_url,data=sign_data,headers=login_header)
sign=json.loads(sign_request.text)
print(sign)





