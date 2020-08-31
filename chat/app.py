# -*- encoding: utf-8 -*-
from flask import Flask, request
from flask import render_template, jsonify
from flask_cors import *
import requests
import json
import urllib.request
app = Flask(__name__)
CORS(app, supports_credentials=True)

api_url = "http://www.tuling123.com/openapi/api/v2"
json_path = '/app/req.json'

@app.route("/", methods=["GET", "POST"])
def temp():
    return render_template('index.html')

@app.route("/chat", methods=["GET", "POST"])
def chat_user():
    input_json = request.get_json()
    msg = input_json['info']
    print(msg + "---chat_user------")
    data = send_msg(msg)
    print("-------after chat ---------")
    print(data)
    print("--------after chat--------")
    return jsonify(data)


def send_msg(msg):
    print("---inside send_msg----")
    data = urllibRequestResponse(msg)
    intent_code = data.get('intent')['code']
    results_text = data.get('results')[0]['values']['text']
    # print('Turing的回答：')
    # print('code：' + str(intent_code))
    # print('text：' + results_text)
    return results_text

def readJson(json_path):
    '''获取json文件'''
    with open(json_path,'r',encoding='utf-8') as f_json:
        json_data = json.load(f_json)
    return json_data

def textInput(json_path,msg):
    '''用变量msg替换text的value值'''
    req = readJson(json_path)
    req['perception']['inputText']['text'] = msg
    print("req-----------")
    print(req)
    print("req-----------")
    return req

def dumpsJson(json_path,input):
    '''将json字符串转化成dict格式'''
    req = textInput(json_path,input)
    req = json.dumps(req,sort_keys=True,indent=4,).encode('utf8')
    return req

def urllibRequestResponse(msg):
    req = dumpsJson(json_path,msg)
    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)# 在urlopen()方法中传入字符串格式的url地址，则此方法会访问目标网址，然后返回访问的结果。
    response_str = response.read().decode('utf8')
    response_dict = json.loads(response_str) # 将字符串response_str转成字典
    return response_dict

if __name__ == '__main__':
    app.run(
      host='0.0.0.0',
      port= 329,
      debug=True
    )

