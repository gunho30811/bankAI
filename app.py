from flask import Flask, render_template, request, jsonify
import naver_crawler

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

if __name__ == '__main__':
    app.run(debug=True)
