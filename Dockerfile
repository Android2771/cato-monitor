FROM balenalib/rpi-raspbian

WORKDIR /cato-monitor

COPY token.txt .
COPY bot.py .
COPY requirements.txt .
COPY capture.sh .

RUN apt update -y
RUN apt install python3 python3-pip fswebcam ffmpeg pulseaudio -y
RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]