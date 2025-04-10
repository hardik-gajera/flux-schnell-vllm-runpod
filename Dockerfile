FROM runpod/vllm:py310cu121

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "handler.py"]
