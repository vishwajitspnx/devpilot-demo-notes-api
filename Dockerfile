# syntax=docker/dockerfile:1.7
# Demo Notes API in one small image. Build from the repository root.
FROM python:3.13.7-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /srv
RUN useradd --create-home --uid 10001 notes

FROM base AS test
COPY requirements.txt requirements-dev.txt ./
RUN pip install -r requirements-dev.txt
COPY pytest.ini ./
COPY app ./app
COPY tests ./tests
USER notes
CMD ["pytest", "-q"]

FROM base AS app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app ./app
USER notes
EXPOSE 8000
HEALTHCHECK --interval=15s --timeout=3s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
