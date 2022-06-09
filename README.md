# BANK APPLICATION 
##### This app allows you to manage a bank.
###### Things that the app do:
*Add new client to the banking system

*Update client charges 

# BACKEND

![image](https://user-images.githubusercontent.com/95073733/165377014-78256d8b-2c31-42a4-a246-58957f781b5a.png)
## HOW TO RUN
 1.Inside to the project directory with the command: cd "PROJECTDIRECTORY"
 2.Inside to the folder backend
 3.Run the Dockerfile with the following commands:
 
  ```docker build -t backend ./ -f Dockerfile```
  
  ```docker run -p 8000:8000 backend```

Now the server is running and you can see this on the following url: ```http://localhost:8000/docs```

# TESTS -Backend

to run the tests run on the your shell : `pytest`

# Frontend

1.Inside to the project directory with the command: cd "PROJECTDIRECTORY"
 2.Inside to the folder frontend
 3.Run the Dockerfile with the following commands:

 ```docker build -t frontend ./ -f Dockerfile```
  
  ```docker run -p 8501:8501 frontend```

Now the server is running and you can see the page on the following url: ```http://localhost:8501```


