from api import app
from fastapi import Request
from database.postservice import get_exact_hashtag_db

# получить несколько хэштегов
@app.get('/api/hashtag')
async def get_some_hashtags(size: int=20, page: int=1):
    pass

# получить фото из определенного хэштега
@app.get('/api/hashtag/<str:hashtag_name>')
async def get_exact_hashtags(hashtag_name: str):
    if hashtag_name:
        exact_hashtags = get_exact_hashtags(hashtag_name)

        return {'status': 1, 'message': exact_hashtags}

    return {'status': 0, 'message': 'No hashtag provided'}