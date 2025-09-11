# 📖 나만의 일기 & 명언 서비스

## 🚀 프로젝트 개요
"나만의 일기장"은 매일 일기를 작성하며 자신의 생각을 정리하고,  
명언과 자기성찰 질문을 랜덤으로 제공받아 꾸준한 성장과 기록 습관 을 도울 수 있는 개인화된 서비스입니다.  

사용자는 일기를 작성하고, 마음에 드는 명언을 북마크하며,  
알림을 통해 새로운 질문과 활동 내역을 확인할 수 있습니다.  

---

## ✨ 주요 기능
- **회원 관리**
  - 회원가입 / 로그인
  - 로그아웃 시 토큰 블랙리스트 처리
- **일기 관리**
  - 일기 작성 / 조회 / 수정 / 삭제
- **명언 제공 & 북마크**
  - 랜덤 명언 제공
  - 명언 북마크 저장
- **오늘의 질문**
  - 랜덤 자기성찰 질문 제공
  - 사용자별 질문 기록 관리
- **알림 기능**
  - 새로운 질문, 북마크, 일기 관련 알림 제공
  - 읽음 여부 관리

---

## 🛠 기술 스택
- **Backend**: FastAPI, SQLAlchemy, Alembic  
- **Database**: PostgreSQL
- **Scraping**: BeautifulSoup, Requests
- **Etc**: Aerich (마이그레이션), uv (패키지 관리)

---

## 📂 프로젝트 구조
```bash
.
├── README.md
├── activate/                  # 가상환경
├── app/                       # 애플리케이션 코드
│   ├── api/                   # API 엔드포인트 (v1)
│   │   └── v1/
│   │       ├── bookmark.py
│   │       ├── diary.py
│   │       ├── notification.py
│   │       ├── question.py
│   │       ├── quote.py
│   │       ├── token.py
│   │       ├── user.py
│   │       └── user_question.py
│   ├── auth.py
│   ├── config.py
│   ├── core/                  # 설정 및 보안 관련
│   ├── data.py
│   ├── database.py
│   ├── db/                    # DB 관련 설정 및 세션
│   ├── main.py
│   ├── models/                # ORM 모델
│   ├── repositories/          # DB 접근 레이어
│   ├── routes/                # 라우팅 모듈
│   ├── schemas/               # 요청/응답 DTO (Pydantic)
│   ├── scraping/              # 스크래핑 모듈 (명언/질문)
│   └── services/              # 서비스 로직
├── db.sqlite3                 # SQLite 테스트 DB
├── migrations/                # 마이그레이션 파일
├── pyproject.toml             # 프로젝트 메타정보
├── test.db                    # 추가 테스트 DB
├── uv.lock                    # uv 패키지 잠금 파일
└── uv.lock.bak

⚡️ 설치 및 실행 방법
# 1. 레포지토리 클론
git clone https://github.com/oz-union-be-13-team2/Web-Scraping-Project.git
cd Web-Scraping-Project

# 2. 가상환경 생성 & 실행
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)

# 3. 패키지 설치
pip install -r requirements.txt

# 4. 데이터베이스 초기화 (개발용 SQLite)
alembic upgrade head

# 5. 서버 실행
uvicorn app.main:app --reload


🗄️ ERD & 데이터베이스 구조
<img width="1640" height="872" alt="ERD 다이어그램" src="https://github.com/user-attachments/assets/6042d7e9-df0a-47b0-9542-662efe477494" />
🔗 테이블 관계

사용자 (users) ↔ 일기 (diaries) : 1:N

사용자 (users) ↔ 사용자 질문 기록 (user_questions) ↔ 질문 (questions) : N:M

사용자 (users) ↔ 명언 북마크 (bookmarks) ↔ 명언 (quotes) : N:M

사용자 (users) ↔ 토큰 블랙리스트 (token_blacklist) : 1:N

사용자 (users) ↔ 알림 (notifications) : 1:N

👥 Contributors

한손: 토큰 관리

경용: 일기 관리, 명언 API

윤혜: 알림 기능, 사용자 질문 기록, 명언 북마크

지선: 사용자 인증 AP