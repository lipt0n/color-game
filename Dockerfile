FROM duffn/python-poetry:3.10-slim

WORKDIR /app

COPY . ./
RUN poetry install


CMD [ "poetry", "run", "python", "color_game/main.py"]