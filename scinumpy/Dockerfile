# Use an official Python runtime as a parent image
FROM python:3.6-slim

RUN pip install numpy scipy pandas matplotlib

# Run app.py when the container launches
#CMD ["python", "app.py"]
ENTRYPOINT ["/usr/local/bin/python"]
