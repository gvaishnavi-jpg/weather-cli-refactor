FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    vim \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default environment variables (users should override with real key)
ENV OPENWEATHER_API_KEY="your_api_key_here"
ENV WEATHER_UNITS="metric"
ENV WEATHER_TIMEOUT="10"

CMD ["/bin/bash"]
