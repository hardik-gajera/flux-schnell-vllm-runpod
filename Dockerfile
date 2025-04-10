FROM runpod/worker-v1-vllm:v2.3.0stable-cuda12.1.0

WORKDIR /app

# Copy your handler and any additional files
COPY handler.py /app/handler.py

# Set the command to run your handler
CMD ["python3", "/app/handler.py"]
