FROM python:3.11
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]