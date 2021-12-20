FROM ubuntu:21.04

WORKDIR '/usr/app'


RUN apt-get update && apt-get install -y python3.9

RUN apt-get install -y python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev


RUN apt-get install -y python3-pip



#RUN apt-get install -y python39-pip

#RUN /usr/bin/python3.9 -m pip install --upgrade python3.9 -m pip



RUN /usr/bin/python3.9 -m pip install flask

RUN  /usr/bin/python3.9 -m  pip install opencv-python
RUN  /usr/bin/python3.9 -m pip install -U flask-cors
RUN  /usr/bin/python3.9 -m pip install  tensorflow==2.5.0rc0
#RUN  /usr/bin/python3.9 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.12.0-py3-none-any.whl
RUN  /usr/bin/python3.9 -m pip install keras
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN apt update
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
RUN /usr/bin/python3.9 -m pip install Pillow
RUN /usr/bin/python3.9 -m pip install Flask-Restful
COPY . .

#CMD ["sh"]
#EXPOSE 8080
CMD ["python3.9","main.py"]

#23351970c60d

