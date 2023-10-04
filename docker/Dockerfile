FROM mcr.microsoft.com/playwright/python:v1.35.0-jammy

ENV PYTEST_MARK=""
ENV BROWSER="firefox"
ENV DEVICE="Desktop Firefox"

VOLUME ["/src/outputs"]
WORKDIR /src

COPY requirements.txt requirements.txt
RUN python -m pip install --root-user-action=ignore --upgrade pip
RUN pip install --root-user-action=ignore --no-cache-dir -r requirements.txt

COPY . .

CMD if [ -z "$PYTEST_MARK" ]; then \
       pytest --browser=${BROWSER} \
              --device="${DEVICE}"; \
    else \
       pytest --browser=${BROWSER} \
              --device="${DEVICE}" \
              -m ${PYTEST_MARK}; \
    fi
