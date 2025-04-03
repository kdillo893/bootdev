# Asteroids game from Boot.dev
This is a game following the tutorials available at boot.dev

Check out the tutorial here:
[Boot.dev Python Asteroids](https://www.boot.dev/courses/build-asteroids-python)

## Install
Set up a virtual python environment for the dependencies to install:

```
python3 -m venv /path/to/venv/
```

Activate the virtual environment when installing and running to 
ensure the dependencies are local to your project's virtual environment:
```
source /path/to/venv/bin/activate
```

This should put an identifier for your virtual environment in the running
terminal emulator, like below:

```
(venv)
userPrompt $ 
```

In this state, run the following:
```
pip install -r requirements.txt
```

Exit the virtual environment like this:
```
deactivate
```

## Running
Enter the virtual environment like above
```
source /path/to/venv/bin/activate
```

When in the virtual environment, execute the following:
```
python3 main.py
```

### Controls
WASD or Arrow Keys: moves the spaceship
SpaceBar: fires a shot
