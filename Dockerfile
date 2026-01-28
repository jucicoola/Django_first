# 파이썬 3.12 버전 사용
FROM python:3.12-slim

# 필요한 도구 설치
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# 작업 폴더 설정
WORKDIR /code

# Poetry 대신 requirements.txt를 사용하도록 설정 (이게 핵심!)
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# 현재 폴더의 모든 파일을 서버로 복사
COPY . /code/

# 서버 실행 명령어
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]