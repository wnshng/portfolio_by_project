from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List
import html
import unicodedata
import shutil

from pypdf import PdfReader


@dataclass
class Project:
    slug: str
    title: str
    subtitle: str
    pdf_match_terms: List[str]
    pdf_exclude_terms: List[str]
    focus: str
    kpis: List[str]
    summary: str
    method_steps: List[str]
    why_it_matters: str


PROJECTS: List[Project] = [
    Project(
        slug="project-01-lsight",
        title="L사 수수료 개편 및 개인화 대시보드",
        subtitle="문제정의 → 데이터 구조화(전문가ID) → 정책 설계 → 매출 효과 → 대시보드 실행",
        pdf_match_terms=["1차", "프로젝트", "발표"],
        pdf_exclude_terms=[],
        focus="데이터 설계력",
        kpis=["반기 추가 매출 약 1억 원", "등급별 수수료 정책", "전문가ID 기반 구조화"],
        summary=(
            "동일 거래 조건에서 수수료율이 다르게 적용된 사례를 확인한 뒤, 전문가ID 중심 데이터 구조와 "
            "등급별 수수료 정책 및 성과 대시보드 기획안을 제시한 프로젝트입니다."
        ),
        method_steps=[
            "문제정의 (p.4): 동일 거래 조건(판매자ID/서비스명/서비스가격/판매금액 동일)에서도 수수료율이 다르게 적용된 사례 약 18,537건(약 28%)을 확인하고, 현재 수수료 기준이 불명확하다고 정의함.",
            "현황 파악 (p.5): 프리랜서 Pain Point 조사 결과(수입 변동성, 일정·수익 예측 불확실성, 수주 기회 부족)를 바탕으로 성과 가시화 필요성을 제시함.",
            "목표 설정 (p.8): 수수료 매출 + 부가서비스 매출을 합쳐 2026년 목표 매출 약 37억 8천으로 설정하고, 부가서비스 목표 가입률을 기존 가입률(27%)로 설정함.",
            "수행 일정 (p.10): 과제 정의→데이터 분석→외부 데이터 수집(위시켓)→개선안→발표까지 주차별로 진행 계획을 명시함.",
            "데이터 수집성 평가 (p.13~15): 1/3/9 척도로 자사 플랫폼/매칭/로그/의뢰인/전문가 변수의 수집가능성·중요도를 평가함.",
            "변수 정의 (p.16~17): 내부 Customer/Log 변수와 판매자ID·서비스가격·거래취소율·판매주기·최근3개월 증감률 등 파생변수를 정의함.",
            "분석 계획 수립 (p.18): 파레토 시각화, 분위수 기반 등급 분류, 군집분석, 비교그룹 오차율 비교, 가설검정, 위시켓 크롤링 분석 계획을 명시함.",
            "수수료 분석 결과 (p.19~20): 판매건수 상위 22%, 판매금액 상위 29% 전문가가 누적 80%를 차지함을 확인하고, 가변 분위수 기반 등급 방안을 제시함.",
            "부가서비스 분석 결과 (p.21~24): 군집+등급+대분류 동시 고려 필요성, 비교그룹 오차율, 핵심요인 가설검정, 위시켓 프로젝트 수요 크롤링 결과를 도출함.",
            "인사이트 정리 (p.25): 명확한 수수료 기준, 성과 비교 인사이트, 데이터 기반 의사결정 지원이 필요하다는 결론을 도출함.",
            "수수료 개선안 (p.26~27): VIP/Platinum/Gold/Silver/Bronze 기준과 변경 수수료율을 제시하고, 2021년 H1 기준 반기 추가 매출 약 1억 원 기대효과를 제시함.",
            "대시보드 실행안 (p.28~33): 홈/등급/분석/트렌드 탭(매출·판매·경쟁자 비교·트렌드 Top5)과 월 5만원 가격안, 예상 가입자·예상 매출을 제시함.",
        ],
        why_it_matters=(
            "위 단계는 「[디지털 하나로] 3!4! _ 1차 프로젝트 발표.pdf」의 p.4~33 기준으로 정리했습니다."
        ),
    ),
    Project(
        slug="project-02-mvno",
        title="D사(MVNO) 이탈 감소 및 LTV 재설계",
        subtitle="목표(-24%) → LTV 재정의 → 이탈 예측 → 우선순위 운영 설계",
        pdf_match_terms=["8기", "3차조", "미니프로젝트"],
        pdf_exclude_terms=[],
        focus="데이터 설계력",
        kpis=["1년 내 이탈률 -24% 목표", "myLTV 재정의", "운영 플로우 설계"],
        summary=(
            "포화 시장 환경에서 이탈률 -24%를 목표로 이탈확률·잔존확률·유지기간·매출예측을 통합하고 "
            "myLTV 재정의와 운영 흐름을 제시한 프로젝트입니다."
        ),
        method_steps=[
            "프로젝트 목표 정의 (p.3): 1년 내 고객 이탈률 -24% 목표를 설정하고, 기존 LTV 신뢰도/이탈·매출 관리 모형 부재를 핵심 문제로 정의함.",
            "특성요인도 작성 (p.4~5): Product/Price/People/Promotion/Suppliers 축으로 요금제·결제·사용행태·이탈정보·공급망 요인을 구조화함.",
            "데이터 수집성 평가 (p.6~7): 상품/가격/프로모션/고객 변수별 수집가능성·중요도 총점을 정리하고 주요 변수 후보를 확정함.",
            "변수 정의 (p.8): 고객ID, 연령, 결혼여부, 부양자수, 추천횟수, 과금방식, 보안/백업/기술지원, 이탈가능점수, 만족도, 로밍사용료 등을 정의함.",
            "파생변수 설계 (p.9): 유지개월수, 예측 유지기간, 남은 예측 개월수, 월별 이탈률, myLTV, 30/180/365일 잔존확률, 기대잔존기간, 예상 이탈일자를 설계함.",
            "외부데이터 결합 (p.10): 환율(달러/위안/엔/유로), 소비자물가지수, 알뜰폰 검색량, 통신3사/알뜰폰 가입자 현황을 변수로 결합함.",
            "이탈예측모형 구축 (p.11): RandomForest/XGBoost/LightGBM 하이퍼파라미터 비교로 Precision·Recall·F1을 평가함.",
            "이탈확률 구간 분석 (p.12): 0.0~1.0 구간별 고객 수와 실제 이탈 고객 수를 비교하고, 예측 양성 중 실제 미이탈 고객을 방지 타겟으로 활용함.",
            "생존분석 적용 (p.13): Kaplan-Meier + Cox Proportional Hazards로 잔존확률/기대생존기간을 산출하고 C-index 0.77을 제시함.",
            "잔존확률 추세예측 (p.14): 관측구간은 Cox, 미래구간은 ARIMA/Prophet으로 예측하고 MAE/RMSE/MAPE 비교로 Prophet을 선택함.",
            "유지기간 예측 (p.15~16): 이탈가능점수 65점 이상·만족도 1/2점 고객에 가중치(5배)를 부여해 보수적으로 유지기간을 추정함.",
            "myLTV 재정의 (p.16): 총과금액, 예측 유지기간, 물가지수, 추천 가중치를 반영해 기존 LTV 대신 재정의한 LTV를 산출함.",
            "매출예측모형 구축 (p.17): 월별 매출 예측에서 SARIMAX/Prophet/Random Forest/LightGBM 성능 비교 후 Prophet 활용안을 제시함.",
            "운영 플로우 설계 (p.18): 모니터링→위기 타겟 식별→우선순위 결정→목표 달성의 4단계 사용자 흐름과 월별 재학습 운영안을 제시함.",
        ],
        why_it_matters=(
            "위 단계는 「디지털하나로 8기 3차조 - 미니프로젝트.pdf」의 p.3~18 기준으로 정리했습니다."
        ),
    ),
    Project(
        slug="project-03-onemart",
        title="원마트 못난이 PB 기획",
        subtitle="배경 → 도매가 데이터 융합 → 장바구니 분석 → 마진율 성과",
        pdf_match_terms=["하나로", "데이터", "분석", "미니프로젝트", "최종"],
        pdf_exclude_terms=[],
        focus="데이터 융합 역량",
        kpis=["마진율 약 70%", "외부 도매가 결합", "FP-Growth 장바구니 분석"],
        summary=(
            "못난이 농산품 원가와 외부 도매가를 결합하고, 월별 판매 특성과 FP-Growth 장바구니 분석으로 "
            "PB 묶음상품을 설계한 프로젝트입니다."
        ),
        method_steps=[
            "추진배경 정의 (p.3): 못난이 농산품(전체 생산량 20~30%)의 원가 경쟁력과 ESG 관점(폐기량 감소)을 근거로 PB 전략을 설정함.",
            "현황 및 개선기회 도출 (p.5): 인지부하/허기/쇼핑비선호 그룹의 묶음상품 구매율이 더 높다는 근거와 채소믹스 판매 증가 사례를 정리함.",
            "목표 설정 (p.6): PB 매출 비중 약 2.8%를 목표로 설정하고, 1년 후 총매출 4억 3,655만원 증가 목표를 산출함.",
            "특성요인도 작성 (p.7): 8P(Product/Place/Process/Physical Evidence/People/Price/Promotion/Performance) 관점으로 요인을 구조화함.",
            "데이터 수집성 평가 (p.8): 회원ID/공급일자/구매금액/타사 가격/물품 카테고리 등 변수의 수집가능성·중요도를 평가함.",
            "변수정의 및 데이터 융합 (p.9): 떠리몰·못난이마켓·도매시장 데이터와 내부 회원/구매 데이터를 연결하고, 도매가_환산금액·장바구니 변수 등을 정의함.",
            "분석계획 수립 (p.10): 외부 데이터 크롤링(떠리몰/못난이마켓), 도매가격 수집, 월/주/계절 파생변수 생성, 장바구니 분석 수행 계획을 수립함.",
            "월별 판매비율 검정 (p.11): 카이제곱 검정(P-value=0.00<0.05)으로 월별 채소/과실 판매비율 차이가 유의함을 확인함.",
            "장바구니 분석 (p.12): FP-Growth로 조합을 도출하고 support/confidence/lift 기준(lift>1.5 + 주력상품 포함)으로 묶음상품 후보를 선정함.",
            "가격·마진 검증 (p.13): 시금치(300g)+당근(500g) 못난이 세트 최소가 5,760원, 마진율 약 70% 계산 결과를 제시함.",
            "실행안 제시 (p.14~15): 7월 세트상품 구성안과 알림서비스/핫존 노출 전략을 함께 제시함.",
        ],
        why_it_matters=(
            "위 단계는 「[하나로 데이터 분석] 3!4!_미니프로젝트_최종.pdf」의 p.3~15 기준으로 정리했습니다."
        ),
    ),
    Project(
        slug="project-04-fast",
        title="FAST 기반 뇌졸중 조기 진단 캡스톤",
        subtitle="문제정의 → 특징 설계(얼굴/팔/음성) → 단계형 UI 결과",
        pdf_match_terms=["최종발표.pdf"],
        pdf_exclude_terms=["하이파이브팀"],
        focus="문제 해결력",
        kpis=["좌우 비대칭 기준 설계", "멀티모달(얼굴/팔/음성)", "단계형 UI"],
        summary=(
            "FAST 원칙 기반으로 얼굴/팔/음성 특징을 정의하고, MLP 판단과 단계형 UI 흐름을 구성한 캡스톤입니다."
        ),
        method_steps=[
            "주제 및 배경 정의 (p.2, p.4): FAST 기반 뇌졸중 감지 시스템을 주제로 선정하고, 골든타임 내 전조 증상 인지의 어려움을 문제로 정의함.",
            "시스템 플로우 제시 (p.6): 얼굴→팔→음성 순서로 측정하는 흐름을 시스템 플로우로 구성함.",
            "구현 방식 설계 (p.7): MediaPipe Face Mesh(얼굴 468좌표), MediaPipe Pose+Hands(팔/손 좌표), Praat+parselmouth(음성 특징), WebSocket 통신 구조를 사용함.",
            "얼굴 특징 설계 (p.8): Yaw/Roll, 입꼬리 거리·기울기, 좌우 비대칭 좌표를 특징으로 수집하고 MLP로 얼굴 비대칭 여부를 판단함.",
            "팔 특징 설계 (p.9): 어깨/팔꿈치/손목+손가락 좌표, 좌우 팔 벡터 각도 차, 손목 깊이·높이 차, 손 방향(손가락 3차원 좌표 포함)으로 MLP를 학습함.",
            "음성 특징 설계 (p.10): Jitter/Shimmer/Intensity를 추출하고 3 Hidden Layer + ReLU + Dropout(40%) 구조로 음성 이상 여부를 판단함.",
            "실시간 통신 구성 (p.11): WebSocket 기반 실시간 양방향 통신 구조를 적용함.",
            "UI 단계 구성 (p.12): 얼굴 감지→팔 측정→음성 측정→최종 결과 화면 순서의 단계형 UI를 제시함.",
        ],
        why_it_matters=(
            "위 단계는 「최종발표.pdf」의 p.2~12 기준으로 정리했습니다."
        ),
    ),
    Project(
        slug="project-05-hansum",
        title="한숨통신 주담대 2030 추천서비스",
        subtitle="타겟 정의 → KPI 설정 → 세그먼트 추천 → 앱 연계 → 사후관리",
        pdf_match_terms=["한숨통신"],
        pdf_exclude_terms=[],
        focus="CX 기획력",
        kpis=["전체 수수료 +10% 목표", "2030 세그먼트 추천", "대출 후속 앱 연계"],
        summary=(
            "주담대/전세대출 이후 2030 고객을 대상으로 타겟 추출·소득 세분화·앱 연계 추천·사후관리까지 설계한 프로젝트입니다."
        ),
        method_steps=[
            "추진배경 정의 (p.3): 충성고객 확보 필요성과 2030 초기관계 형성 필요성(연령대별 이탈경험 비율 포함)을 근거로 제시함.",
            "타겟 설정 근거 (p.4): 대출 실행 직후 소비 집중(가구/가전/인테리어 등)과 2030의 초개인화 선호를 연결해 타겟을 구체화함.",
            "현황 및 기회 파악 (p.5~6): 규제 이후 2030 생애최초 주택 구입 증가, 하나원큐의 대중형 탐색 구조, 후속 개인화 추천 부재를 문제로 정의함.",
            "경쟁사 벤치마킹 (p.7): 카카오페이의 대출/카드/수신 개인화 추천 구조와 비교해 개선 방향을 설정함.",
            "KPI 설정 (p.8): 전체 수수료 수익 +10%, 카드 수수료 +15%, 여신·외환 수수료 +10% 목표와 비대면 실적 회복 목표를 제시함.",
            "분석 계획 수립 (p.9): 타겟층 분류→소득분류 세분화→ANOVA/HSD 가설검정 순서로 분석 절차를 명시함.",
            "타겟층 추출 (p.10): 연령 20~39, 추정소득 4,000만원 이상, 대출액(1금융권) 8,000만원 이상, 신용점수 665점 이상, 연체 없음 기준으로 1,361명을 선별함.",
            "세그먼트 구성 (p.11~12): 소득분위 기반 상/중/하 분류와 가족원수·가구추정소득·TDR 지표로 고객군 특성을 정리함.",
            "통계 검정 (p.13): ANOVA/HSD 결과로 상·중·하 그룹 간 가족원수/가구추정소득/TDR 평균 차이의 유의성을 제시함.",
            "서비스 플로우 설계 (p.14): 영업점 QR·SMS 안내→대출 승인 직후 앱 자동팝업→내 대출관리 탭 연동의 3단계 UX 흐름을 제시함.",
            "세그먼트별 추천안 (p.15): 상/중/하 소득군별 카드·신용대출·수신상품 조합과 기대효과를 제시함.",
            "사후관리 설계 (p.16): 전월실적/급여이체/자동이체/수신유지 조건의 충족 여부를 월별 자동 점검·알림하는 우대금리 케어 프로세스를 제시함.",
        ],
        why_it_matters=(
            "위 단계는 「[디지털하나로] 한숨통신_최종발표자료.pdf」의 p.3~16 기준으로 정리했습니다."
        ),
    ),
    Project(
        slug="project-06-travelog",
        title="트래블로그 게이미피케이션 CX",
        subtitle="기회정의 → 군집설계 → 게이미피케이션 적용 → CX 여정 설계",
        pdf_match_terms=["하이파이브팀", "2차", "최종발표"],
        pdf_exclude_terms=[],
        focus="CX 기획력",
        kpis=["MAU 확대", "중도해지 완화 목표", "고객경험(CX) 여정 설계"],
        summary=(
            "트래블로그 여행 적금에 게이미피케이션을 결합하고, 군집 분석·해지예측·팝업스토어·앱 UI를 연결한 CX 기획 프로젝트입니다."
        ),
        method_steps=[
            "시장/고객 Pain Point 정의 (p.8): 여행자금 수요 증가, 단기 납입 선호 확대, 2030의 비용 중심 의사결정 특성을 근거로 트래블로그 여행 적금 집중 전략을 제시함.",
            "상품 진단 (p.9): 카드 연계 혜택은 있으나 납입 과정의 시각적 즐거움·동기부여가 부족하다는 현황을 정의하고, 26주적금 사례를 비교 근거로 제시함.",
            "게이미피케이션 근거 정리 (p.11~13): 개념 정의, 시장규모(CAGR), 2030 참여 영향 조사, 타사 성공사례를 정리해 도입 필요성을 제시함.",
            "목표 수치 설정 (p.15): MAU 120만명 증가, 중도해약률 2.4%p 감축, 3개월 내 신규가입 30만좌 목표, NIM 1.62% 목표를 제시함.",
            "수행 일정 명시 (p.18): 데이터 수집/정의, EDA/전처리, 고객군집화, 중도해지 예측, 인사이트 도출, 개선안 작성 순서를 일정표로 제시함.",
            "데이터 수집성 평가/변수정의 (p.21~23): 총점 12점 이상 변수 사용 기준, 고객·상품·채널 변수, Acc_ID/Deposit_Code/Cancellation 등 상세 변수 정의를 제시함.",
            "외부데이터 결합 (p.26): 한국관광데이터랩 해외여행객(960x5)과 서울 열린데이터광장 생활인구(760x9) 데이터를 분석 변수로 결합함.",
            "분석계획 수립 (p.27): K-means 군집분석(실루엣 기반 k 결정)과 중도해지 분류모델(RandomForest/Logistic/XGBoost/LightGBM) 계획을 명시함.",
            "군집분석 결과 (p.29): 전체 26,253행 데이터를 k=4로 분류하고, 소극적/고위험연체/충성/우호적마케팅수용 군집 특성을 도출함.",
            "중도해지 예측 결과 (p.31~32): 변수 파이프라인과 모델 성능 비교를 제시하고, 해지확률 0.3 이상 위험군 대상 활용 방안을 제시함.",
            "인사이트 도출 (p.34): 인지도·차별성 약함, 오프라인 접점 약화, 기존 적금 고객 락인 장치 부재를 핵심 과제로 정리함.",
            "앱 UI 개선안 (p.37~40): 비행기 진행형 메인화면, 군집별 맞춤 미션, 출석/랜덤미션, 홈 위젯(D-Day·납입현황) 등 화면 흐름을 제시함.",
            "오프라인 전략/비용 (p.42~44): 성수 팝업스토어 전략, 후보지 근거, 게임개발 외주(3,500만~4,500만원), 팝업 운영예산(7억5천만~10억)을 제시함.",
            "기대효과/CX 여정 (p.45~46): MAU·NIM·신규유입 기대효과와 인지→개인화→습관화→확산 4단계 고객감정선 여정을 제시함.",
        ],
        why_it_matters=(
            "위 단계는 「[디지털하나로] 하이파이브팀 2차 프로젝트 최종발표.pdf」의 p.8~46 기준으로 정리했습니다."
        ),
    ),
]

DISPLAY_ORDER = [
    "project-06-travelog",
    "project-01-lsight",
    "project-03-onemart",
    "project-04-fast",
    "project-02-mvno",
    "project-05-hansum",
]


CSS = """@import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Noto+Sans+KR:wght@400;500;700&display=swap");

:root {
  --bg: #f6f4ef;
  --ink: #10182b;
  --muted: #44506a;
  --brand: #0f766e;
  --brand-2: #ff7a18;
  --card: #ffffff;
  --line: #d7dde8;
  --chip: #eaf8f6;
  --shadow: 0 14px 36px rgba(16, 24, 43, 0.09);
  --radius: 18px;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: "Noto Sans KR", sans-serif;
  color: var(--ink);
  background:
    radial-gradient(circle at 8% 15%, rgba(15, 118, 110, 0.1) 0, rgba(15, 118, 110, 0) 35%),
    radial-gradient(circle at 93% 8%, rgba(255, 122, 24, 0.12) 0, rgba(255, 122, 24, 0) 33%),
    linear-gradient(135deg, #fdfbf7 0%, var(--bg) 60%, #f4f9ff 100%);
  line-height: 1.6;
}

.wrap {
  width: min(1120px, 92vw);
  margin: 0 auto;
  padding: 28px 0 60px;
}

.hero {
  background: linear-gradient(135deg, #072f2d 0%, #0f4c81 55%, #ff7a18 120%);
  color: #fefefe;
  border-radius: 24px;
  padding: 34px 32px 28px;
  box-shadow: var(--shadow);
  position: relative;
  overflow: hidden;
}

.hero::after {
  content: "";
  position: absolute;
  inset: auto -70px -120px auto;
  width: 280px;
  height: 280px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.14);
  filter: blur(2px);
}

.hero h1 {
  margin: 0 0 10px;
  font-family: "Space Grotesk", sans-serif;
  font-size: clamp(1.5rem, 2.8vw, 2.25rem);
  line-height: 1.25;
  letter-spacing: -0.02em;
}

.hero p {
  margin: 0;
  font-size: 0.98rem;
  color: rgba(255, 255, 255, 0.92);
  max-width: 760px;
}

.meta {
  margin-top: 16px;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.meta span {
  background: rgba(255, 255, 255, 0.16);
  border: 1px solid rgba(255, 255, 255, 0.22);
  border-radius: 999px;
  padding: 5px 12px;
  font-size: 0.82rem;
}

.section {
  margin-top: 16px;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 18px;
  box-shadow: var(--shadow);
}

.section h2 {
  margin: 0 0 10px;
  font-family: "Space Grotesk", sans-serif;
  letter-spacing: -0.015em;
  font-size: 1.18rem;
}

.headline {
  margin: 0 0 12px;
  color: var(--muted);
  font-size: 0.93rem;
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
  gap: 14px;
}

.card {
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 14px;
  background: #fff;
}

.card h3 {
  margin: 0 0 6px;
  font-size: 0.98rem;
  line-height: 1.35;
}

.card p {
  margin: 0;
  color: var(--muted);
  font-size: 0.92rem;
  line-height: 1.52;
}

.project-card {
  background: linear-gradient(180deg, #ffffff 0%, #fbfdff 100%);
  border: 1px solid #cfdaed;
  box-shadow: 0 8px 18px rgba(16, 24, 43, 0.05);
}

.project-title {
  margin: 0 0 7px;
  font-size: 1.18rem;
  font-weight: 800;
  color: #0e1f3e;
  line-height: 1.48;
  letter-spacing: -0.01em;
}

.project-focus {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  background: #f0f8ff;
  color: #0b4d79;
  border: 1px solid #cfe3ff;
  padding: 4px 10px;
  font-size: 0.79rem;
  font-weight: 700;
  margin-bottom: 8px;
}

.project-summary {
  margin: 0 0 8px;
  color: #2c3f60;
  font-size: 0.9rem;
  line-height: 1.6;
}

.flow-list {
  margin: 0 0 10px;
  padding-left: 18px;
  color: #16253f;
  font-size: 0.9rem;
  line-height: 1.56;
}

.flow-list li {
  margin-bottom: 3px;
}

.kpi {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 8px 0 12px;
}

.kpi span {
  background: var(--chip);
  color: #064e48;
  border: 1px solid #bde7df;
  border-radius: 999px;
  padding: 5px 10px;
  font-size: 0.82rem;
  font-weight: 700;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  border-radius: 11px;
  font-weight: 700;
  padding: 10px 14px;
  font-size: 0.88rem;
  border: 1px solid rgba(0, 0, 0, 0.08);
  background: #fff;
  color: #123;
}

.btn.primary {
  background: #102645;
  color: #fff;
}

.btns {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 10px;
}

.method-list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 10px;
}

.method-item {
  border: 1px solid #d6deec;
  border-radius: 14px;
  background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
  padding: 12px 14px;
}

.method-head {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin-bottom: 6px;
}

.method-no {
  min-width: 32px;
  text-align: center;
  border-radius: 999px;
  background: #eaf2ff;
  border: 1px solid #c8daf7;
  color: #0b4178;
  font-family: "Space Grotesk", sans-serif;
  font-size: 0.78rem;
  font-weight: 700;
  padding: 3px 8px;
  line-height: 1.2;
}

.method-head h3 {
  margin: 1px 0 0;
  font-size: 0.98rem;
  line-height: 1.45;
  color: #0f2347;
  letter-spacing: -0.005em;
}

.method-item p {
  margin: 0;
  font-size: 0.93rem;
  line-height: 1.72;
  color: #2d3e5f;
  word-break: keep-all;
}

.pdf-wrap {
  margin-top: 12px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: #fff;
  overflow: hidden;
}

iframe {
  width: 100%;
  height: min(76vh, 980px);
  border: 0;
}

.small {
  font-size: 0.82rem;
  color: #54627c;
}

footer {
  margin-top: 20px;
  font-size: 0.84rem;
  color: #4e5b75;
  text-align: center;
}

@media (max-width: 760px) {
  .hero {
    padding: 24px 20px;
  }
  .section {
    padding: 14px;
  }
}"""


def normalize_name(name: str) -> str:
    return unicodedata.normalize("NFKD", name).replace(" ", "").lower()


def resolve_pdf_path(out_dir: Path, match_terms: List[str], exclude_terms: List[str]) -> Path:
    candidates = [p for p in sorted(out_dir.glob("*.pdf")) if not p.name.startswith("._")]
    terms = [normalize_name(t) for t in match_terms]
    exclude = [normalize_name(t) for t in exclude_terms]
    for file in candidates:
        name = normalize_name(file.name)
        if all(term in name for term in terms) and not any(term in name for term in exclude):
            return file
    raise FileNotFoundError(f"Missing PDF by terms: {match_terms}, exclude: {exclude_terms}")


def render_index(projects: List[Project], out_dir: Path) -> None:
    cards = []
    for i, project in enumerate(projects, start=1):
        pdf_name = f"{project.slug}.pdf"
        flow_steps = [s.strip() for s in project.subtitle.split("→")]
        flow_items = "".join([f"<li>{step}</li>" for step in flow_steps if step])
        cards.append(
            f"""
      <article class="card project-card">
        <h3 class="project-title">{i:02d}. {project.title}</h3>
        <span class="project-focus">Focus: {project.focus}</span>
        <p class="project-summary">{project.summary}</p>
        <ol class="flow-list">{flow_items}</ol>
        <div class="kpi">{''.join([f'<span>{k}</span>' for k in project.kpis])}</div>
        <div class="btns">
          <a class="btn primary" href="./{project.slug}.html">프로젝트 설명 보기</a>
          <a class="btn" href="./{pdf_name}">PDF 열기</a>
        </div>
      </article>
"""
        )

    index_html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>프로젝트별 포트폴리오</title>
  <link rel="stylesheet" href="./site.css" />
</head>
<body>
  <div class="wrap">
    <header class="hero">
      <h1>프로젝트별 포트폴리오<br />Independent Project View</h1>
      <p>이전 포트폴리오 스타일을 유지하면서, 프로젝트를 섞지 않고 각각 독립적으로 볼 수 있도록 구성했습니다. 각 프로젝트 페이지에는 수행 방식(데이터 설계/분석/실행)을 함께 정리했습니다.</p>
      <div class="meta">
        <span>총 {len(projects)}개 프로젝트</span>
        <span>프로젝트별 독립 페이지</span>
        <span>설명 + PDF 동시 제공</span>
      </div>
    </header>

    <section class="section">
      <h2>프로젝트 목록</h2>
      <p class="headline">원하는 프로젝트만 골라서 보면 흐름이 끊기지 않습니다.</p>
      <div class="cards">
        {''.join(cards)}
      </div>
      <p class="small">파일명을 바꾸지 않고 PDF만 교체하면 같은 링크에서 새 내용으로 열립니다. 파일명을 바꿨다면 빌드 스크립트를 다시 실행하세요.</p>
    </section>

    <footer>
      생성 파일: index.html, project-*.html, site.css
    </footer>
  </div>
</body>
</html>
"""
    (out_dir / "index.html").write_text(index_html, encoding="utf-8")


def render_project_page(project: Project, page_count: int, pdf_name: str, out_dir: Path) -> None:
    rendered_steps = []
    for i, step in enumerate(project.method_steps, start=1):
        if ":" in step:
            step_title, step_body = step.split(":", 1)
        else:
            step_title, step_body = step, ""
        rendered_steps.append(
            f"""
        <li class="method-item">
          <div class="method-head">
            <span class="method-no">{i:02d}</span>
            <h3>{html.escape(step_title.strip())}</h3>
          </div>
          <p>{html.escape(step_body.strip())}</p>
        </li>
"""
        )
    method_items = "".join(rendered_steps)
    kpis = "".join([f"<span>{k}</span>" for k in project.kpis])

    page_html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{project.title}</title>
  <link rel="stylesheet" href="./site.css" />
</head>
<body>
  <div class="wrap">
    <header class="hero">
      <h1>{project.title}</h1>
      <p>{project.subtitle}</p>
      <div class="meta">
        <span>Focus: {project.focus}</span>
        <span>{page_count}p</span>
        <span>{pdf_name}</span>
      </div>
      <div class="btns">
        <a class="btn" href="./index.html">목록으로</a>
        <a class="btn primary" href="./{pdf_name}">PDF 열기</a>
      </div>
    </header>

    <section class="section">
      <h2>프로젝트 요약</h2>
      <p class="headline">{project.summary}</p>
      <div class="kpi">{kpis}</div>
    </section>

    <section class="section">
      <h2>어떤 식으로 진행했는지</h2>
      <ol class="method-list">
        {method_items}
      </ol>
      <p class="small">{project.why_it_matters}</p>
    </section>

    <section class="section">
      <h2>프로젝트 PDF 바로보기</h2>
      <p class="headline">페이지 내에서 바로 확인하고, 필요하면 원본 PDF를 별도 탭으로 열어보세요.</p>
      <div class="pdf-wrap">
        <iframe src="./{pdf_name}" title="{project.title} PDF"></iframe>
      </div>
    </section>
  </div>
</body>
</html>
"""
    (out_dir / f"{project.slug}.html").write_text(page_html, encoding="utf-8")


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    (out_dir / "site.css").write_text(CSS, encoding="utf-8")

    for project in PROJECTS:
        safe_pdf_name = f"{project.slug}.pdf"
        safe_pdf_path = out_dir / safe_pdf_name
        # Prefer already-normalized ASCII PDF names for deployment stability.
        if safe_pdf_path.exists():
            source_pdf = safe_pdf_path
        else:
            source_pdf = resolve_pdf_path(out_dir, project.pdf_match_terms, project.pdf_exclude_terms)
            if source_pdf.resolve() != safe_pdf_path.resolve():
                shutil.copy2(source_pdf, safe_pdf_path)
        page_count = len(PdfReader(str(source_pdf)).pages)
        render_project_page(project, page_count, safe_pdf_name, out_dir)

    project_by_slug = {project.slug: project for project in PROJECTS}
    ordered_projects = [project_by_slug[slug] for slug in DISPLAY_ORDER if slug in project_by_slug]
    render_index(ordered_projects, out_dir)
    print("generated: index.html, site.css, project pages")


if __name__ == "__main__":
    main()
