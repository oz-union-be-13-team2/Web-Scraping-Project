📖 일기 & 명언 서비스
🚀 프로젝트 개요

이 프로젝트는 사용자가 회원가입 후 일기를 작성하고, 명언과 질문을 통해 자기 성찰을 도울 수 있는 플랫폼입니다.<br>
또한, 사용자는 마음에 드는 명언을 북마크할 수 있으며, 알림 기능을 통해 새로운 질문이나 활동 알림을 받을 수 있습니다.<br>

✨ 주요 기능<br>
회원가입 / 로그인<br>
JWT 기반 인증<br>
로그아웃 시 토큰 블랙리스트에 저장<br>
일기 관리<br>
일기 작성 / 조회 / 수정 / 삭제<br>
명언 제공 & 북마크<br>
랜덤 명언 제공<br>
명언 북마크 저장<br>
오늘의 질문<br>
랜덤 자기성찰 질문 제공<br>
사용자별 질문 기록 관리<br>
알림 기능<br>
새로운 질문, 북마크, 일기 관련 알림 제공<br>
읽음 여부 관리<br>

🗄️ 데이터베이스 테이블 구조<br><br>
👤 사용자 (한손)<br>
컬럼	타입	설명<br>
user_id	INT, PK, AUTO_INCREMENT	사용자 ID<br>
user_name	VARCHAR(100)	사용자 이름<br>
password_hash	VARCHAR(100)	암호화된 비밀번호<br><br>
📔 일기 (경용)<br>
컬럼	타입	설명<br>
diaries_id	INT, PK, AUTO_INCREMENT	일기 ID<br>
user_id	INT, FK	사용자 ID (한손.user_id)<br>
title	VARCHAR(100)	일기 제목<br>
content	TEXT	일기 내용<br>
created_at	TIMESTAMP	작성 시간 (기본 NOW)<br><br>
📝 사용자 질문 기록 (윤혜)<br>
컬럼	타입	설명<br>
user_question_id	INT, PK, AUTO_INCREMENT	사용자 질문 기록 ID<br>
user_id	INT, FK	사용자 ID (한손.user_id)<br>
question_id	INT, FK	질문 ID (지선2.question_id)<br>
answered_at	TIMESTAMP	답변 시간<br>
answer_text	VARCHAR(255)	사용자 답변<br><br>
⭐ 명언 북마크 (지선)<br>
컬럼	타입	설명<br>
bookmark_id	INT, PK, AUTO_INCREMENT	북마크 ID<br>
quotes_id	INT, FK	명언 ID (경용2.quotes_id)<br>
user_id	INT, FK	사용자 ID (한손.user_id)<br>
bookmark_user_id	VARCHAR(255)	(예비 필드, 정리 필요)<br><br>
🔑 토큰 블랙리스트 (한손)<br>
컬럼	타입	설명<br>
token_id	INT, PK, AUTO_INCREMENT	토큰 블랙리스트 ID<br>
user_id	INT, FK	사용자 ID (한손.user_id)<br>
token	VARCHAR(255)	JWT 토큰 값<br>
expired_at	TIMESTAMP	만료 시간<br><br>
💬 명언 (경용)<br>
컬럼	타입	설명<br>
quotes_id	INT, PK, AUTO_INCREMENT	명언 ID<br>
content	TEXT	명언 내용<br>
author	VARCHAR(100)	명언 작성자<br>
language	VARCHAR(50)	언어<br>
source	VARCHAR(100)	출처<br><br>
❓ 질문 (지선)<br>
컬럼	타입	설명<br>
question_id	INT, PK, AUTO_INCREMENT	질문 ID<br>
question_text	TEXT	질문 내용<br><br>
🔔 알림 (윤혜)<br>
컬럼	타입	설명<br>
Notification_ID	INT, PK, AUTO_INCREMENT	알림 ID<br>
user_id	INT, FK	사용자 ID (한손.user_id)<br>
title	VARCHAR(255)	알림 제목<br>
message	VARCHAR(255)	알림 메시지<br>
is_read	VARCHAR(255)	읽음 여부<br>
noti_time	TIMESTAMP	알림 생성 시간<br><br>
🔗 테이블 관계<br>

한손 (users) ↔ 경용 (diaries) : 1:N<br><br>

한손 (users) ↔ 윤혜 (user_questions) ↔ 지선2 (questions) : N:M<br><br>

한손 (users) ↔ 지선 (bookmarks) ↔ 경용2 (quotes) : N:M<br><br>

한손 (users) ↔ 한손 (token_blacklist) : 1:N<br><br>

한손 (users) ↔ 윤혜 (notifications) : 1:N<br><br>


<img width="1640" height="872" alt="일기 작성 서비스" src="https://github.com/user-attachments/assets/6042d7e9-df0a-47b0-9542-662efe477494" />

