from datetime import UTC, datetime
from typing import Annotated

from fastapi import Cookie, Header, Response, status, APIRouter
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix='/posts')

fake_db = [
    {"title": "Criando uma aplicação com Django", "date": datetime.now(UTC), 'published': True},
    {"title": "Internacionalizando uma app FastAPI", "date": datetime.now(UTC), 'published': True},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(UTC), 'published': True},
    {"title": "Internacionalizando uma app Starlette", "date": datetime.now(UTC), 'published': False},
]

# CRIAR post - usa POST
@router.post('/',status_code=status.HTTP_201_CREATED, response_model=PostOut)  # 👈 Mudou de GET para POST
def create_post(post: PostIn):
    fake_db.append(post.model_dump())  # Adiciona ao banco fake
    return post

# LER posts - usa GET
@router.get('/', response_model=list[PostOut])
def read_posts(
    response: Response, 
    published: bool, 
    limit: int, 
    skip: int = 0, 
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str|None, Header()]= None,
):

    response.set_cookie(key='user', value='dan.ifsp11@outlook.com')
    print(f"Cookie: {ads_id}")
    print(f"User-agent: {user_agent}")
    tail = skip + limit
    return [post for post in fake_db[skip: tail] if post["published"] is published]

@router.get("/{framework}", response_model=PostOut)
def read_framework_posts(framework: str):
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
            {"title": f"Internacionalizando uma app {framework}", "date": datetime.now(UTC)},
        ]
    }