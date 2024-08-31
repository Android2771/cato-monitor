FROM balenalib/rpi-raspbian

WORKDIR /cato-monitor

COPY token.txt .
COPY bot.py .
COPY requirements.txt .

RUN apt update -y
RUN apt install python3 python3-pip fswebcam ffmpeg -y
RUN pip3 install -r requirements.txt

RUN touch output.mov
RUN touch output.jpg

CMD ["python3", "bot.py"]