# Deployment using docker

To build the docker file, make sure you are in the root of this task project. then:

```bash
sudo docker build -t bitpin_task .
```

and then run the container:

```bash
sudo docker run -p 8000:8000 bitpin_task
```