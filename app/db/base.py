import os
from dotenv import load_dotenv
from tortoise import Tortoise

# .env 파일에서 환경 변수를 불러옵니다.
load_dotenv()

# Tortoise ORM 설정을 정의합니다.
TORTOISE_CONFIG = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            # 모델 파일 경로를 명시합니다. 예: "app.models"
            "models": ["app,modles","aerich.models"],
            "default_connection": "default",
        }
    },
}

async def init_db():
    """Tortoise ORM을 초기화하고 DB 연결을 설정합니다."""
    await Tortoise.init(config=TORTOISE_CONFIG)
    print("DB connection established! 🚀")