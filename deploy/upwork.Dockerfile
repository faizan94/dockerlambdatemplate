FROM public.ecr.aws/lambda/python:3.7

# Copy code files
COPY requirements.txt ./

# Install requirements
RUN python3.7 -m pip install -r requirements.txt -t .

# Copy code files
COPY src/app.py ./
COPY src ./src

# Execute code
# ENTRYPOINT ["python", "-m", "src"]
ENTRYPOINT ["bash"]
# CMD ["app.lambda_handler"]
