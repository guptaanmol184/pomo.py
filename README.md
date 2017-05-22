# pomo.py

A simple python script for a audio based pomodoro timer to be used on linux systems

**_pomo.py_** runs a pomodoro timer on linux systems and provides audio alerts for starting and stopping of the timer.

The timer settings for individual preferences can be easily set by changing respective values of **workTime** and **breakTime** variables in the script.

_**Requires a working internet connection for gtts to work.**_

_This was created just for fun purposes and learning about python._

Tested on Linux (Ubuntu)

## Dependencies

### [mpg123](https://www.mpg123.de)

```
sudo apt-get install mpg123
```

### [gTTS](https://github.com/pndurette/gTTS)

```
sudo pip3 install gtts
```

## Run

### Make script executable and run

```
chmod +x ./pomo.py
./pomo.py
```

## LICENSE

MIT

_Happy working!_
