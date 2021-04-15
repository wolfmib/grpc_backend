## Howmework_03: Golang and Access MongoDB 
#### Auth: Jean
---

- on va faire la simple server pour 
    - add data
    - edit data
    - get data
    - delete data 

- user_data 
    - id         int
    - name       srting
    - wallet_id  int

- wallet_data
    - wallet_id  int
    - id with    int (from user)
    - balance    int

---

### Step Un: Faire la MongoDB 
---

- install mongodb 
- launch mongod
- enter mongo prompt
    - create database ja_platform
    - create collection user
        - user_data
    - create collection wallet 
        - wallet_data

### Step De: Faire la User Server avec simple afficher message log (sans mongodb access)

---

- rpc methods:
    - user-server
        - GetUser (id ) return user data , nil
        - ChangeUser (id , string name ) return changed_name
        - DelteUser(id) return id
        - AddUser(string name ) return id , name

---

### Step Tr: Faire la Client pour checking response
---

- client.go
    - api.getuser()
    - api.changeuse()
    - api.deleteuser()
    - api.adduser()