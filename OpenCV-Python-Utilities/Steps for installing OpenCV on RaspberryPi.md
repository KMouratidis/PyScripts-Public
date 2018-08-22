#### Enter as superuser, and update the system
```
su
apt-get update
apt-get upgrade
```

#### Get OpenCV files and other necessary dependencies
```
apt-get install build-essential cmake pkg-config
apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
apt-get install libxvidcore-dev libx264-dev
apt-get install libgtk2.0-dev
apt-get install libatlas-base-dev gfortran
apt-get install python2.7-dev python3-dev
apt-get install --reinstall libqtcore4
apt-get install libqt4-dev
cd
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.4.1.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.4.1.zip
unzip opencv_contrib.zip
pip install virtualenv virtualenvwrapper
```

#### Make a Python 3 virtual envornment
```
echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.profile
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
source ~/.profile
mkvirtualenv cv -p python3
source ~/.profile
workon cv
```

#### Build OpenCV
```
cd ~/opencv-3.4.1/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.4.1/modules -D BUILD_EXAMPLES=ON ..
make
make install
ldconfig
```

#### For python 3, inside the v.env
```
pip install numpy
pip install opencv-python
```

#### For python 2
```
source ~/.profile
apt-get install python-opencv
```
