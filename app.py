from flask import Flask, render_template
import loan
import naver_crawler

app = Flask(__name__)

@app.route('/')
def home():
    loan_data = loan.get_loan_data()
    naver_df = naver_crawler.get_naver_data()
    naver_data = naver_df.to_dict('records')  # 데이터프레임을 리스트로 변환합니다.
    return render_template('index.html', loan_data=loan_data, naver_data=naver_data)


if __name__ == '__main__':
    app.run(debug=True)

