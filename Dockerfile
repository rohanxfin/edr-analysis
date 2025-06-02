# Use NVIDIA PyTorch Image (CUDA + Python included)
FROM nvcr.io/nvidia/pytorch:23.08-py3

# Set working directory
WORKDIR /app

# Copy dependency file first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy application files

COPY app.py constants.py emails.py last_uid_progress.json prompts.py streamlit.py ./  
COPY data ./data


# Expose the port Flask runs on
EXPOSE 8080

# Command to run the application
CMD ["sh", "-c", "streamlit run streamlit.py --server.port=${PORT:-8080} --server.address=0.0.0.0"]