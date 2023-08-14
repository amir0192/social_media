from api import app

# получить все посты
@app.get('/api/posts')
async def get_all_or_exact_post(post_id: int=0, user_id: int=0):
    pass

# изменить пост профиля
@app.put('/api/post')
async def change_file_post():
    pass

# удалить определенную пост
@app.delete('/api/post')
async def delete_user_post():
    pass