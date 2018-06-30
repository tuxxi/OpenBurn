# OpenBurn

OpenBurn is an open-source solid rocket engine simulation and design platform designed from the ground up for 
the amateur rocketry community. 
OpenBurn is based on Qt5 and Python 3, and has support across all major platforms (Windows, OSX, Linux).

## Building

OpenBurn requires:
- Qt 5.6 or newer, preferably the newest version (currently 5.11).
- Python 3.6+
- PyQt5 or PySide2<sup>[1]</sup>

<sup>[1]</sup>OpenBurn uses the [QtPy](https://pypi.org/project/QtPy/) abstraction layer for Python Qt bindings,
so you can use either PySide2 or PyQt5

To check out the ongoing development:

```bash
git clone https://github.com/tuxxi/OpenBurn
sudo pip install -r requirements.txt
python3 main.py
```