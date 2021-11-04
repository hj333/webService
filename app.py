import get_news

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# 화면에 접속


@app.route("/")
def home():
    return render_template("index.html")

# STEP 03-2 : json 띄우기


@app.route("/json")
def json():
    return jsonify({"message": "Hello, JSON!"})

# STEP 04 : json 형식으로 db의 뉴스데이터 보내주기


keywords = []


@app.route("/keyword", methods=["GET", "POST"])
def get_keyword():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':

        # 입력받은 keyword
        temp = request.args.get('keyword')
        keywords.append(temp)

        # 입력받은 키워드를 원래 페이지로 리다이렉트
        return render_template('index.html', keyword=temp)


@app.route("/api/news")
def send_news():
    naver_news_items = []
    naver_news_items = get_news.save_navernews(keywords)

    if len(keywords) != 0:
        keywords.pop()

    return jsonify({"news": naver_news_items})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True, threaded=True)
