from flask import Flask, render_template, request, jsonify
import naver_crawler
from chatgpt import ask_chatgpt

app = Flask(__name__)

@app.route('/')
def index():
    city_list = naver_crawler.get_sido_info()
    # 다른 필요한 데이터들을 가져오는 코드가 있다면 여기에 추가하세요.
    return render_template('index.html', city_list=city_list)

@app.route('/get_gu_list', methods=['POST'])
def get_gu_list():
    city_cortar_no = request.form.get('city_cortar_no')
    gu_list = naver_crawler.get_gungu_info(city_cortar_no)
    return jsonify(gu_list)

@app.route('/get_dong_list', methods=['POST'])
def get_dong_list():
    gu_cortar_no = request.form.get('gu_cortar_no')
    dong_list = naver_crawler.get_dong_info(gu_cortar_no)
    return jsonify(dong_list)

@app.route('/get_officetel_list', methods=['POST'])
def get_officetel_list():
    dong_code = request.form.get('dong_code')
    officetel_list = naver_crawler.get_officetel_list(dong_code)
    return jsonify(officetel_list)

@app.route("/search", methods=["POST"])
def search():
    dong_code = request.form.get("dongCode")
    min_price = int(request.form.get("minPrice"))
    max_price = int(request.form.get("maxPrice"))
    
    if not dong_code or min_price is None or max_price is None:
        return "모든 필드를 입력해주세요.", 400
    
    results = naver_crawler.get_all_articles(dong_code, min_price, max_price)
    return jsonify(results)

@app.route('/ask_chatgpt', methods=['POST'])
def ask_chatgpt_route():
    question = request.form['question']
    text_data = get_text_data()  # text_data 가져오는 함수입니다. 이미 구현되어 있다고 가정합니다.
    answer = ask_chatgpt(f"{text_data}\n\n{question}")
    return jsonify(answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
