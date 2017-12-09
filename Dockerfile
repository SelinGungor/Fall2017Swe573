FROM python:3.6

RUN git clone https://github.com/SelinGungor/Fall2017Swe573.git

RUN cd Fall2017Swe573

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /Fall2017Swe573/swe573

CMD ["python", "manage.py", "runserver"]
