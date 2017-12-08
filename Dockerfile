COPY Fall2017Swe573/swe573/requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

RUN git clone https://github.com/SelinGungor/Fall2017Swe573.git

EXPOSE 8000

WORKDIR /Fall2017Swe573/swe573

CMD ["python", "manage.py", "runserver"]
