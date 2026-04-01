# 프로젝트별 포트폴리오 (웹 + PDF)

이 폴더는 프로젝트를 독립적으로 보는 구조입니다.

## 파일 구조
- `index.html`: 프로젝트 목록 메인
- `project-*.html`: 프로젝트별 상세 페이지(설명 + PDF 뷰어)
- `site.css`: 공통 스타일 (이전 웹사이트 톤 유지)
- 원본 PDF들: 각 프로젝트 발표 원본
- `build_project_site.py`: 웹 페이지 자동 생성 스크립트

## 사용 방법
1. 이 폴더 안의 원본 PDF를 교체합니다.
2. 아래 명령으로 웹 페이지를 재생성합니다.

```bash
. ../.venv/bin/activate
python ./build_project_site.py
```

3. `index.html`을 열어 프로젝트별로 확인합니다.

## 매칭 규칙
- 스크립트는 파일명을 완전일치로 찾지 않고, 프로젝트별 키워드로 PDF를 자동 매칭합니다.
- macOS 한글 파일명(NFC/NFD) 차이를 고려해 정규화 처리되어 있습니다.

## 참고
- 기존 `project_page_map.csv`는 이전 작업 산출물로 남겨두었습니다.
