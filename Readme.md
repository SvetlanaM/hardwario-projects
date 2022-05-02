# Hardwario dongle button example

This code was created as a part of the 2 day workshop in collaboration with
[Czechitas](https://www.czechitas.cz/) and
[Hardwario](https://www.hardwario.com/cs/) during Future Tech Conference in
Prague.

The main purpose of this workshop was show, how easy it is use Hardwario
prepared [Hardwario Button](https://eshop.fengoo.cz/starter-bundle/) on simple
use case - **Meal Notification** . When you push the button, based on a time in
a day, kids will receive a notification about meal time (breakfast, lunch,
dinner time).

Demonstation for this workshop was in:

1. Hardwario platform where you can configure in nocode platform the whole
   button functionality, including communications with the button via MQTT
   queues.
2. Python script for notifications based on specified time periods and bridge
   between the platform and the real users.

### Requirements

1. Python 3.4 || Python 3.5
2. [pip](https://pypi.python.org/pypi/pip/1.0.2) - tool for installing and
   managing Python packages
3. [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) (not
   required) - tool to keep the dependencies required by different projects in
   separate places

### Installation

Run this code it is possible only when you have a button and cofiguration in
Hardwario platform.

1. Create virtual environment in your project folder <code>python3 -m venv
   venv</code>
2. Install required libraries and packages <code>pip3 install -r
   requirements.txt</code>
3. Add your button to Hardwario platform
4. Configurate in Hardwario platform communication via MQTT
5. Edit <code>broker</code> and <code>client</code> in this code example based
   on your values
6. Run code: <code>python3 notification.py</code>
