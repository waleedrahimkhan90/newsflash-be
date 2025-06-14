from fastapi import FastAPI

app = FastAPI()

news_data = [
    {"id": 1, "title": "First News", "content": "This is the first news item."},
    {"id": 2, "title": "Second News", "content": "This is the second news item."},
    {"id": 3, "title": "Second News", "content": "This is the third news item."},
    {"id": 4, "title": "Fourth News", "content": "This is the fourth news item."},
    {"id": 5, "title": "Fifth News", "content": "This is the fifth news item."},
    {"id": 6, "title": "Sixth News", "content": "This is the sixth news item."},
    {"id": 7, "title": "Seventh News", "content": "This is the seventh news item."},
    {"id": 8, "title": "Eighth News", "content": "This is the eighth news item."},
    {"id": 9, "title": "Ninth News", "content": "This is the ninth news item."},
    {"id": 10, "title": "Tenth News", "content": "This is the tenth news item."},
]

@app.get("/news")
def get_all_news():
    return news_data
