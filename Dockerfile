# 1. Use a standard lightweight Python image
FROM python:3.11-slim

# 2. Set the folder inside the container
WORKDIR /app

# 3. Install 'uv' (The tool you are using)
RUN pip install uv

# 4. Copy your dependency files first (for caching speed)
COPY pyproject.toml uv.lock* /app/

# 5. Install dependencies
# --system means "install to the main python", not a virtualenv
RUN uv pip install --system -r pyproject.toml || uv pip install --system .

# 6. Copy the rest of your code
COPY . /app

# 7. Open the web port
EXPOSE 8000

# 8. Run the server
CMD ["uv", "run", "server.py"]