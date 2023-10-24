# This could also be another Ubuntu or Debian based distribution
# This could also be another Ubuntu or Debian based distribution
FROM ubuntu:22.04
# Install Open3D system dependencies 
ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    curl \
    gcc \
    libegl1 \
    libgl1 \
    libgomp1 \
    wget \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Size reduction by removing unnecessary things
RUN apt-get autoremove -y
# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
# Set the path for Poetry
ENV PATH /root/.local/bin:$PATH

# Prevent Poetry from creating a virtual environment
RUN poetry config virtualenvs.create false

# Create project directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

# Copy code for experimentation
COPY . .
