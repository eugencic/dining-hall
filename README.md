# Network Programming laboratory Nr.1

## Dining Hall

This is the `dining hall` of the restaurant simulation of the first laboratory work at Network Programming course.
The `kitchen` part: https://github.com/eugencic/kitchen

## Main Task

The purpose of this task is to write a simulation of how a restaurant works.
    
The general idea is that there is the `dining hall` and the `kitchen`.
The `dining hall` generates `orders` and sends them to the `kitchen`, which prepares them and returns the prepared orders back to the `dining hall`.

## Technologies

* Code editor : Visual Studio Code
* Programming language : Python 3.10
* Software : Docker

### Clone the repository
```bash
$ git clone https://github.com/eugencic/dining-hall
```

### Docker  
```bash
 docker build -t dininghall .
 docker run --name=dininghall -e PYTHONUNBUFFERED=1 -d dininghall
 docker compose up
```