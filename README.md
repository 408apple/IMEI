<a href="#">
    <img src="https://raw.githubusercontent.com/pedromxavier/flag-badges/main/badges/TR.svg" alt="made in TR">
</a>

# IMEI Query System
This application is a tool that makes it easy to query the IMEI numbers of devices with sim cards and retrieve information.

<h1 align="center">IMEI Query System Logo</h1>

<p align="center">
  <img src="imeilo.png" alt="IMEI Logo" width="150" height="150">
</p>


----------------------

# Linux Screenshot
![Linux(pardus)](screenshot/imei_linux.gif)  

--------------------
Install Git Clone and Python3

Github Package Must Be Installed On Your Device.

git
```bash
sudo apt install git -y
```

Python3
```bash
sudo apt install python3 -y 

```

pip
```bash
sudo apt install python3-pip

```

# Required Libraries

PyQt5
```bash
pip install PyQt5
```
PyQt5-sip
```bash
pip install PyQt5 PyQt5-sip
```

PyQt5-tools
```bash
pip install PyQt5-tools
```

Required Libraries for Debian/Ubuntu
```bash
sudo apt-get install python3-pyqt5
sudo apt-get install qttools5-dev-tools
sudo apt-get install python3-pillow
sudo apt-get install python3-pypdf2
```
pillow
```bash
pip3 install pillow
```
requests
```bash
pip3 install requests
```

beautifulsoup4
```bash
pip3 install beautifulsoup4
```

urllib3
```bash
pip3 install urllib3
```

----------------------------------


# Installation
Install IMEI

```bash
sudo git clone https://github.com/cektor/IMEI.git
```
```bash
cd IMEI
```

```bash
python3 imei.py

```

# To compile

NOTE: For Compilation Process pyinstaller must be installed. To Install If Not Installed.

pip install pyinstaller 

Linux Terminal 
```bash
pytohn3 -m pyinstaller --onefile --windowed imei.py
```

MacOS VSCode Terminal 
```bash
pyinstaller --onefile --noconsole imei.py
```

# To install directly on Linux





Linux (based debian) Terminal: Linux (debian based distributions) To install directly from Terminal.
```bash
wget -O Setup_Linux64.deb https://github.com/cektor/IMEI/releases/download/1.00/Setup_Linux64.deb && sudo apt install ./Setup_Linux64.deb && sudo apt-get install -f -y
```


Release Page: https://github.com/cektor/IMEI/releases/tag/1.00

----------------------------------

