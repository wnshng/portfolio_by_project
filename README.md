# 프로젝트별 포트폴리오 (웹 + PDF)

이 폴더는 프로젝트를 독립적으로 보는 구조입니다.

## 파일 구조
- `index.html`: 프로젝트 목록 메인
- `project-*.html`: 프로젝트별 상세 페이지(설명 + PDF 뷰어)
- `project-*.pdf`: 배포용 표준 PDF 파일명(영문/숫자)
- `site.css`: 공통 스타일 (이전 웹사이트 톤 유지)
- `build_project_site.py`: 웹 페이지 자동 생성 스크립트

## 사용 방법
1. 이 폴더 안의 `project-*.pdf` 파일을 교체합니다.
2. 아래 명령으로 웹 페이지를 재생성합니다.

```bash
. ../.venv/bin/activate
python ./build_project_site.py
```

3. `index.html`을 열어 프로젝트별로 확인합니다.

## 매칭 규칙
- 기본 규칙: `project-*.pdf` 표준 파일명을 우선 사용합니다.
- 예전 한글 원본 파일명만 있을 경우, 프로젝트별 키워드로 fallback 매칭 후 표준 파일명으로 복사합니다.
- macOS 한글 파일명(NFC/NFD) 차이를 고려해 정규화 처리되어 있습니다.

## 참고
- 기존 `project_page_map.csv`는 이전 작업 산출물로 남겨두었습니다.
