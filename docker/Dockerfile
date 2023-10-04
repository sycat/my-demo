FROM mcr.microsoft.com/playwright/python:v1.35.0-jammy

ARG SCOPE

ENV ENVIRONMENT="beta"
ENV BROWSER="firefox"
ENV DEVICE="Desktop Firefox"

VOLUME ["/src/outputs"]
WORKDIR /src

COPY requirements.txt requirements.txt
RUN python -m pip install --root-user-action=ignore --upgrade pip
RUN pip install --root-user-action=ignore --no-cache-dir -r requirements.txt

COPY . .

CMD if [ "$SCOPE" = "facebook" ]; then \
       pytest --env=${ENVIRONMENT} \
              --browser=${BROWSER} \
              --device="${DEVICE}" \
              -m facebook; \
    else \
       pytest --env=${ENVIRONMENT} \
              --browser=${BROWSER} \
              --device="${DEVICE}"; \
    fi
