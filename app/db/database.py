import os
from dotenv import load_dotenv
from tortoise import Tortoise

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models.user", "app.models.diary","aerich.models"],  # 모델 등록
            "default_connection": "default",
        },
    },
}

async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    # 자동 테이블 생성 (개발 단계에서만)
    await Tortoise.generate_schemas()