# 📰 LLM-data-pub

**LLM-data-pub**는 Naver 뉴스 검색 API를 기반으로 뉴스 데이터를 수집한 뒤, 각 뉴스 페이지의 실제 본문을 크롤링하여 벡터 DB(ChromaDB)에 저장하는 파이프라인입니다.  
이 데이터를 활용해 LLM 기반 질의응답, 요약, 검색 시스템을 구현할 수 있습니다.

---

## 📌 주요 기능 요약

- **뉴스 제목·링크 수집**: Naver 뉴스 검색 API 사용
- **본문 크롤링**: 각 뉴스 링크에서 BeautifulSoup으로 기사 본문 크롤링
- **텍스트 정제 및 벡터화**: 크롤링한 본문을 ChromaDB에 저장
- **벡터 검색 테스트**: ChromaDB 기반 유사도 검색 기능 구현

---

## 📂 프로젝트 구조 및 기능 설명

| 파일명 | 설명 | 
|--------|------|
| [.gitignore](https://github.com/team-irreplaceable/LLM-data-pub/blob/main/.gitignore) | Git에 포함시키지 않을 파일 목록 정의 |
| [chromadb_test.py](https://github.com/team-irreplaceable/LLM-data-pub/blob/main/chromadb_test.py) | ChromaDB에 저장된 데이터에 대해 질의(Query) 및 검색 테스트 수행 
| [create_chroma.py](https://github.com/team-irreplaceable/LLM-data-pub/blob/main/create_chroma.py) | ChromaDB 인스턴스를 생성하고, 초기 세팅을 진행하는 스크립트 | 
| [news_api2json.ipynb](https://github.com/team-irreplaceable/LLM-data-pub/blob/main/news_api2json.ipynb) | Naver 뉴스 검색 API로 뉴스 제목, 링크를 수집 → JSON 저장 | 
| [news_data.json](https://github.com/team-irreplaceable/LLM-data-pub/blob/main/news_data.json) | 뉴스 기사 제목, 링크 등 메타데이터 저장 샘플 |
| [news_json2ChromaDB.ipynb](https://github.com/team-irreplaceable/LLM-data-pub/blob/main/news_json2ChromaDB.ipynb) | JSON 파일에서 뉴스 링크를 불러와 본문 크롤링 (BeautifulSoup 사용) → 벡터로 변환하여 ChromaDB 저장 | 
| [requirements.txt](https://github.com/team-irreplaceable/LLM-data-pub/blob/main/requirements.txt) | 프로젝트 실행에 필요한 Python 라이브러리 목록 | 

---

## 🚀 사용 방법

### 1. 환경 설정

```bash
# 가상환경 (선택)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
