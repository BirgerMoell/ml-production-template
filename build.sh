# Presentation
set -ex
docker build -t model .
docker run -ti -p 8000:8000 model uvicorn main:app --reload