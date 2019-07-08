From python

COPY . /app
WORKDIR /app
RUN pip install -r requirement.txt
EXPOSE 5000
CMD python app.py