import google.generativeai as genai
import requests

# 1. API 키 및 텔레그램 설정
GEMINI_API_KEY = "AQ.Ab8RN6KmQ9cTr-mOnR2pqyv9JmKjIeVHXeRmGS_IAsSk40Xogg"
TELEGRAM_BOT_TOKEN = "8240561559:AAFORNq32K7qRCnB8fxECIEIcbcJDUBiEKM"
TELEGRAM_CHAT_ID = "8975967544"

genai.configure(api_key=GEMINI_API_KEY)

# 2. 최신 제미나이 모델 설정
model = genai.GenerativeModel('gemini-2.5-flash')

# 3. 명지 e편한세상 분석 데이터
market_data = """
[명지 e편한세상 35평 매도 판단용 5대 지표]
1. 전세가율: 매매가 4.6억 / 전세가 3.0억 (전세가율 65.2%), 전세 매물 감소세
2. 에코델타시티 입주: 잔금 납부율 상승 및 신축 전세 물량 소화 진행 중
3. 부산 상급지 시세: 수영구/해운대구 핵심 단지 거래량 증가 및 소폭 반등
4. 시중 대출 금리: 주택담보대출 혼합형 고정금리 3.5%대 유지
5. 지역 인프라: 하단-녹산선 관련 사업 진척 소식 발표
"""

# 4. 작성하신 맞춤형 AI 종합 판단 프롬프트
prompt = f"""
당신은 부산 명지국제신도시 부동산 시장의 흐름을 꿰뚫어 보는 전문 퀀트 분석가이자 자산관리 AI입니다.
제시된 5가지 지표를 바탕으로 '명지 e편한세상 35평' 소유자를 위한 월간 매매 전략 보고서를 작성하세요.

[입력 데이터]
{market_data}
매수가: 5.1억

[보고서 작성 필수 가이드라인]
1. 분석 도구 통합: '네이버 부동산(매물/호가)', '아실(전세잔여물량/거래량)', '호갱노노(실시간 방문자/외지인 투자비율)' 앱의 데이터를 어떻게 모니터링하고 해석해야 하는지 보고서에 반드시 포함하세요.
2. 금융 조언 배제: 개인적 대출 상황이나 상환 능력에 대한 언급은 철저히 배제하세요.
3. 핵심 임계점(Critical Point): 시장 지표 간 상관관계를 분석하여 가격 반등이 시작되는 수치적 임계점을 정밀하게 제시하세요.
4. 매도 시점 판정: (강력보유 / 관망 / 매도준비 / 매도 중 선택 + AI 종합 매력 점수 100점 만점)
5. 시나리오 예측: 향후 6~12개월 내 발생 가능한 강세/약세 시나리오를 데이터 기반으로 예측하세요.
6. 모니터링 지표: 이번 달 사용자가 상기 앱들(네이버, 아실, 호갱노노)을 통해 직접 확인해야 할 핵심 변화 포인트 2가지를 전략적으로 제시하세요.
"""

# 5. AI 분석 실행 및 텔레그램 발송
try:
    response = model.generate_content(prompt)
    report_text = response.text

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": report_text
    }
    res = requests.post(url, data=payload)
    if res.status_code == 200:
        print("\n✅ 텔레그램으로 정밀 보고서 전송이 완료되었습니다!")
    else:
        print("\n❌ 텔레그램 전송 실패:", res.text)
except Exception as e:
    print(f"\n❌ 분석 중 오류 발생: {e}")
