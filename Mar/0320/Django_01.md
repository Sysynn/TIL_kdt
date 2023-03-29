# Framwork
- 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
 (개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공)

## 왜 프레임워크를 사용하는가?
- 0부터 개발하는 것이 어렵다는 사실도 있지만 기본적인 구조와 규칙을 제공하기 때문에 개발에만 집중 가능
- 개발 속도를 빠르게 도와주고 유지보수와 확장에 용이
- 프론트엔드 프레임워크(vue js, react 등)과 백엔드 프레임워크(Django 등)이 있음

# Django
- Python 기반의 프레임워크 중 가장 높은 점유율

# Client와 Server
## Client
- 서비스를 요청하는 주체(사용자) : 웹 사용자의 인터넷이 연결된 장치, 웹 브라우저

## Server
- 클라이언트의 요청에 응답하는 주체 : 웹 페이지, 앱을 저장하는 컴퓨터

# 가상환경 생성 루틴
1. 가상환경 생성 
- python3 -m venv venv
2. 가상환경 활성화
- source venv/bin/activate
3. django 설치
- pip install django==3.2.18
4. 의존성 파일 생성 (패키지 설치시마다 진행)
- pip freeze > requirements.txt
5. git 저장소 생성
6. .gitignore 파일 생성
7. django 앱 생성
- django-admin startproject 'firstpjt' . (맨 뒤에 .을 안붙이면 동일명의 폴더가 하위에 생성됨)
8. app 생성
- python3 manage.py startapp 'app_name'
- settings에 app 이름 추가
<!-- 서버 끄는건 컨트롤 c
cmd+shift+P -> vscode에서 실행검색  -->

- pip install -r requirements.txt
  다른 페어가 올린 설정집에 있는 프로그램들을 한번에 설치
- 새로운 것을 설치할 때 마다 freeze 명령어로 requirements.txt를 업데이트