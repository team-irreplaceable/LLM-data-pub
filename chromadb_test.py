import chromadb
from chromadb import PersistentClient
from chromadb.config import Settings

client = PersistentClient(path="news_chroma_db")
print(client.list_collections())

# DB 불러오기
client = PersistentClient(path="news_chroma_db")
collection = client.get_collection("news_articles")

# 예: 골프 관련 검색
results = collection.query(query_texts=["골프"], n_results=3)

for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
    print(f"제목: {meta['title']} / 날짜: {meta['date']} / 언론사: {meta['journal']}")
    print(f"내용: {doc[:100]}...\n")

