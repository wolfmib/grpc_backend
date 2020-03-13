# grpc_backend
grpc, protobuf


## !! 😓..

---

Jean: Try use local host: 172.17.42.1

---

Finiah the docker-compose build and up for gate, user, mongodb
---
- docker-compose build
- docker-compose up
- check the docker-compose.yml file
- mongodb is mounting to ja_mongodb folder and working fine.

---

![result](img/docker_all.jpg)



---

- source ja_create_mongodb.sh  (automation done)
    - create ja_mongodb folder
    - move mongod.conf to ja_mongodb folder

- source ja_run_db.sh        
    - run mongod with target_db

- type mongo start your table (not auto deploy yet)


---


## Status report:
---

![Status](./img/status.jpg)

