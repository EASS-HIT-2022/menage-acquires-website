# BACKEND

![image](https://user-images.githubusercontent.com/95073733/165377014-78256d8b-2c31-42a4-a246-58957f781b5a.png)
## HOW TO RUN
 1.Inside to the project directory with the command: cd "PROJECTDIRECTORY"
 2.Inside to the folder backend
 3.Run the Dockerfile with the following commands:
 
  ```docker build -t backend ./ -f Dockerfile```
  
  ```docker run -p 8000:8000 backend```

Now the server is running and you can see this on the following url: ```http://localhost:8000/docs```