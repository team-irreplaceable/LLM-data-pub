from chromadb import PersistentClient
import json
import uuid

# 1. ChromaDB 설정 - PersistentClient 사용!
chroma_client = PersistentClient(path="news_chroma_db")  # 이 경로에 DB가 저장됨

# 2. 컬렉션 생성 또는 불러오기
collection = chroma_client.get_or_create_collection(name="news_articles")

# 3. JSON 파일 로드
with open("sports_news.json", "r", encoding="utf-8") as f:
    news_data = json.load(f)

# 4. 데이터 삽입
for item in news_data:
    uid = str(uuid.uuid4())  # 고유 ID 생성
    collection.add(
        documents=[item["content"]],
        metadatas=[{
            "title": item["title"],
            "date": item["date"],
            "link": item["link"],
            "journal": item["journal"]
        }],
        ids=[uid]
    )

print("✅ ChromaDB에 저장 완료")

# DB 불러오기
client = PersistentClient(path="news_chroma_db")
collection = client.get_collection("news_articles")

# 예: 골프 관련 검색
results = collection.query(query_texts=["골프"], n_results=3)

for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
    print(f"제목: {meta['title']} / 날짜: {meta['date']} / 언론사: {meta['journal']}")
    print(f"내용: {doc[:100]}...\n")