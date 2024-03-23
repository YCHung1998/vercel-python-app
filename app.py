import json
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/about')
def about():
    return 'The about page to show that smthing your might to know'



@app.route('/api')
def api():
    return "api link is working" 


message_kv = {"@傳送類別排序和文章數": "@傳送類別排序和文章數", 
                "@數位時代五日內熱搜類別": "@數位時代五日內熱搜類別", 
                "@傳送圖片": "@傳送圖片", 
                "@回傳我的Uid": "@回傳我的Uid", 
                "@keyword": "@keyword",
                }


@app.route('/messages', methods=['GET'])
def get_messages():
    # 将字典转换为JSON字符串
    message_json = json.dumps(message_kv)
    # 返回JSON响应
    return jsonify(messages=message_json)
