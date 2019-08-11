# Image
FROM alpine:3.7

# Pre-build
RUN pip install poetry

# Vars
ARG ENV=${ENV:-dev}

# Copy / Move Files
WORKDIR /statsapiclient
COPY . /statsapiclient
RUN cd /statsapiclient

# Dependencies / Build
RUN poetry install

# Start Up
EXPOSE 8080
CMD npm run start:${ENV}
