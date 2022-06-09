# Frontend

1.Inside to the project directory with the command: cd "PROJECTDIRECTORY"
 2.Inside to the folder frontend
 3.Run the Dockerfile with the following commands:

 ```docker build -t frontend ./ -f Dockerfile```
  
  ```docker run -p 8501:8501 frontend```

Now the server is running and you can see the page on the following url: ```http://localhost:8501```