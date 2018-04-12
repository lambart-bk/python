#! /usr/bin/env python3


import uuid
import base64
import json
import urllib.request
import sys

asr_server = 'http://vop.baidu.com/server_api'
access_token = '24.952433cf7122c73ef25c2cfa4b51def1.2592000.1486526856.282335-9179275'
mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]


def baidu_asr(speech_file):
    with open(speech_file, 'rb') as f:
        speech_data = f.read()
    speech_base64 = base64.b64encode(speech_data).decode('utf-8')
    speech_length = len(speech_data)
    data_dict = {'format': 'wav', 'rate': 8000, 'channel': 1, 'cuid': mac_address,
                 'token': access_token, 'lan': 'zh', 'speech': speech_base64, 'len': speech_length}
    json_data = json.dumps(data_dict).encode('utf-8')
    json_length = len(json_data)

    request = urllib.request.Request(url=asr_server)
    request.add_header("Content-Type", "application/json")
    request.add_header("Content-Length", json_length)
    fs = urllib.request.urlopen(url=request, data=json_data)

    result_str = fs.read().decode('utf-8')
    json_resp = json.loads(result_str)
    return json_resp

json_resp = baidu_asr(sys.argv[1])
print(json_resp)
print (json_resp['err_msg'])
if json_resp['err_msg'] == 'success.':
    print(json_resp['result'])
