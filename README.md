# ALCwithMICROSOFT ADVANCED ASSESSMENT 

## Requirements : 
*Docker* and *python3* is required to run commands.py script

## Instructions : 

Docker needs to be run as root, so enter root mode
```
sudo su
```

Next, build docker containers:
```
python commands.py --build
```

To start UserManager and mongo-db containers : 
```
python commands.py --start
```

To stop running containers :
```
python commands.py --stop
```

To get help:
```
python commands.py --help
```
