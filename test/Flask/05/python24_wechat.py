# coding=utf-8
from flask import Flask,request,make_response
import hashlib
import xmltodict
import time

app = Flask(__name__)


# 对接微信服务器流程
@app.route('/wechat8004',methods=['GET','POST'])
def wechat():
    if request.method == 'GET':
        token = 'python'
        # 获取参数
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
        # 对参数进行检查,字典序排序/字符串拼接/sha1加密
        temp = [token,timestamp,nonce]
        temp.sort()
        data = ''.join(temp)
        if hashlib.sha1(data).hexdigest() == signature:
            return make_response(echostr)
        else:
            return 'error',666
    else:
        # 文本消息处理,获取xml格式数据
        xml_data = request.data
        req = xmltodict.parse(xml_data)['xml']
        # 获取参数的数据类型
        type = req.get('MsgType')
        if 'text' == type:
            resp = {
                'ToUserName':req.get('FromUserName'),
                'FromUserName':req.get('ToUserName'),
                'CreateTime':int(time.time()),
                'MsgType':'text',
                'Content':req.get('Content')
            }
            # 把响应数据转成xml格式
            data = xmltodict.unparse({'xml':resp})
            return data
        elif 'voice' == type:
            resp = {
                'ToUserName':req.get('FromUserName'),
                'FromUserName': req.get('ToUserName'),
                'CreateTime': int(time.time()),
                'MsgType': 'text',
                'Content': req.get('Recognition',u'口音比较重')
            }
            data = xmltodict.unparse({'xml':resp})
            return data
        else:
            resp = {
                'ToUserName':req.get('FromUserName'),
                'FromUserName': req.get('ToUserName'),
                'CreateTime': int(time.time()),
                'MsgType': 'text',
                'Content': 'I LOVE PYTHON24'
            }
            data = xmltodict.unparse({'xml':resp})
            return data

import datetime
import urllib
import json
import urllib2

"""
appID
wx4225092f2c6ae20a
appsecret
48c298be298ea1a82c61d91b6a9a735d

"""
WECHAT_APPID = 'wx4225092f2c6ae20a'
WECHAT_SECRET = '48c298be298ea1a82c61d91b6a9a735d'

# 获取全局唯一票据
class AccessToken(object):
    _access_token = {
        'token':'',
        'updatetime':datetime.datetime.now(),
        'expires_in':''
    }

    # 封装的思想,对外提供公共接口,隐藏实现过程
    @classmethod
    def get_access_token(cls):
        # 如果全局唯一票据不存在,或者临近过期时间
        if not cls._access_token['token'] or (datetime.datetime.now() - cls._access_token['updatetime']).seconds >= 6800:
            return cls.__update_access_token()
        else:
            return cls._access_token['token']

    # 实现主要业务逻辑,获取全局唯一票据
    @classmethod
    def __update_access_token(cls):
        # 拼接url的参数
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (WECHAT_APPID,WECHAT_SECRET)
        # 发送get请求,获取响应数据
        data = urllib.urlopen(url).read()
        # 把json数据转成字典
        resp_data = json.loads(data)
        # 获取字典中全局唯一票据
        cls._access_token['token'] = resp_data.get('access_token')
        return cls._access_token['token']

# print AccessToken.get_access_token()

# 获取ticket用来换取二维码
@app.route('/scene_id=<id>')
def get_ticket_code(id):
    access_token = AccessToken.get_access_token()
    url = 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s' % access_token
    # 构造请求体
    req_body = {
        'action_name':'QR_SCENE',
        'action_info':{'scene':{'scene_id':id}},
        'expire_seconds':''
    }
    # 把请求体转成json字符串
    data = json.dumps(req_body)
    # 构造请求对象
    req = urllib2.Request(url,data)
    # 发送post请求
    resp = urllib2.urlopen(req).read()
    # 判断返回结果
    if 'errcode' in resp:
        return 'error',666
    else:
        # 把响应数据转成字典
        resp_data = json.loads(resp)
        ticket = resp_data.get('ticket')
        return '<img src="https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s">' % ticket




if __name__ == '__main__':
    app.run(debug=True,port=8004)


