from fastapi import FastAPI

app = FastAPI()

news_data = [
    {"id": 1, "title": "First News", "content": "This is the first news item."},
    {"id": 2, "title": "Second News", "content": "This is the second news item."},
    {"id": 3, "title": "Second News", "content": "This is the third news item."},
]

@app.get("/news")
def get_all_news():
    return news_data
