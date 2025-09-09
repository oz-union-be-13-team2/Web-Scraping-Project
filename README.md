📖 일기 & 명언 서비스
🚀 프로젝트 개요

이 프로젝트는 사용자가 회원가입 후 일기를 작성하고, 명언과 질문을 통해 자기 성찰을 도울 수 있는 플랫폼입니다.
또한, 사용자는 마음에 드는 명언을 북마크할 수 있으며, 알림 기능을 통해 새로운 질문이나 활동 알림을 받을 수 있습니다.

✨ 주요 기능
회원가입 / 로그인
JWT 기반 인증
로그아웃 시 토큰 블랙리스트에 저장
일기 관리
일기 작성 / 조회 / 수정 / 삭제
명언 제공 & 북마크
랜덤 명언 제공
명언 북마크 저장
오늘의 질문
랜덤 자기성찰 질문 제공
사용자별 질문 기록 관리
알림 기능
새로운 질문, 북마크, 일기 관련 알림 제공
읽음 여부 관리

🗄️ 데이터베이스 테이블 구조
👤 사용자 (한손)
컬럼	타입	설명
user_id	INT, PK, AUTO_INCREMENT	사용자 ID
user_name	VARCHAR(100)	사용자 이름
password_hash	VARCHAR(100)	암호화된 비밀번호
📔 일기 (경용)
컬럼	타입	설명
diaries_id	INT, PK, AUTO_INCREMENT	일기 ID
user_id	INT, FK	사용자 ID (한손.user_id)
title	VARCHAR(100)	일기 제목
content	TEXT	일기 내용
created_at	TIMESTAMP	작성 시간 (기본 NOW)
📝 사용자 질문 기록 (윤혜)
컬럼	타입	설명
user_question_id	INT, PK, AUTO_INCREMENT	사용자 질문 기록 ID
user_id	INT, FK	사용자 ID (한손.user_id)
question_id	INT, FK	질문 ID (지선2.question_id)
answered_at	TIMESTAMP	답변 시간
answer_text	VARCHAR(255)	사용자 답변
⭐ 명언 북마크 (지선)
컬럼	타입	설명
bookmark_id	INT, PK, AUTO_INCREMENT	북마크 ID
quotes_id	INT, FK	명언 ID (경용2.quotes_id)
user_id	INT, FK	사용자 ID (한손.user_id)
bookmark_user_id	VARCHAR(255)	(예비 필드, 정리 필요)
🔑 토큰 블랙리스트 (한손)
컬럼	타입	설명
token_id	INT, PK, AUTO_INCREMENT	토큰 블랙리스트 ID
user_id	INT, FK	사용자 ID (한손.user_id)
token	VARCHAR(255)	JWT 토큰 값
expired_at	TIMESTAMP	만료 시간
💬 명언 (경용)
컬럼	타입	설명
quotes_id	INT, PK, AUTO_INCREMENT	명언 ID
content	TEXT	명언 내용
author	VARCHAR(100)	명언 작성자
language	VARCHAR(50)	언어
source	VARCHAR(100)	출처
❓ 질문 (지선)
컬럼	타입	설명
question_id	INT, PK, AUTO_INCREMENT	질문 ID
question_text	TEXT	질문 내용
🔔 알림 (윤혜)
컬럼	타입	설명
Notification_ID	INT, PK, AUTO_INCREMENT	알림 ID
user_id	INT, FK	사용자 ID (한손.user_id)
title	VARCHAR(255)	알림 제목
message	VARCHAR(255)	알림 메시지
is_read	VARCHAR(255)	읽음 여부
noti_time	TIMESTAMP	알림 생성 시간
🔗 테이블 관계

한손 (users) ↔ 경용 (diaries) : 1:N

한손 (users) ↔ 윤혜 (user_questions) ↔ 지선2 (questions) : N:M

한손 (users) ↔ 지선 (bookmarks) ↔ 경용2 (quotes) : N:M

한손 (users) ↔ 한손 (token_blacklist) : 1:N

한손 (users) ↔ 윤혜 (notifications) : 1:N