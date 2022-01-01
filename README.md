# SuperFlappyBird version alpha (0.1)
Simple Flappy Bird like game in Python using PyGame for Linux, Windows, MacOS, and Android

## PyGame lib
pip install pygame

## Building game for Android using Buildozer
pip install buildozer
pip install cython==0.29.19
pip install kivymd
pip install python-for-android
sudo apt install lld

sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev

sudo apt-get install -y \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good

sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev 
zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev 
libreadline-dev libncursesw5-dev libffi-dev uuid-dev libffi6

sudo apt-get install libffi-dev

## Initializing Buildozer
buildozer init

## Bulding APK and pushing to mobile (connected to the PC, Developer mode enabled, USB Debbug enabled, all permission allowed)
buildozer -v android debug deploy


## Debbuging using ADB

sudo apt install adb

adb logcat *D|grep python