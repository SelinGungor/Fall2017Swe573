FROM python:3.6

RUN git clone https://github.com/SelinGungor/Fall2017Swe573.git

COPY requirements.txt /Fall2017Swe573

WORKDIR /Fall2017Swe573

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

WORKDIR /Fall2017Swe573/myapp/swe573

CMD ["python", "manage.py", "runserver"]