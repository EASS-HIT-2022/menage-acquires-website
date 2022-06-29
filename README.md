# Menage Acquires Website
### This app allows you to manage your aqcuires.
#### Things that the app do:
*Add new client to the system


*Add new client acquire 


## How TO Run The Project:
### Backend + Frontend + DB :

1.Download the repository to your pc 


2.Inside to the project directory with the command: cd "MenageAcquiresWebsite"


3.Run the docker compose file with the following commands:
 
```bash
docker-compose up
```

After the docker copmpose finished, you can see the backend running on port 8000  
you can see the backend by [click here](http://localhost:8001/) or copy the url: `http://localhost:8000/docs` to your browser.
When you clicking on the url you will see: 

![image](https://user-images.githubusercontent.com/95073733/175815655-7e0de6b0-42f8-4793-b5f0-d61530d68f6e.png)

You also can see the frontend, which running on port 8501, you can access it by [click here](http://localhost:8501/) or copy the url: `http://localhost:8501` to your browser.
When you clicking on the url you will see:

![image](https://user-images.githubusercontent.com/95073733/175999560-95f227f9-d50f-4d8c-b36c-e9777591fb67.png)

If you want to see details aboout the containers, you can run on your shell `docker ps` and you will get the output:
![image](https://user-images.githubusercontent.com/95073733/176356015-25b28fe0-6232-4f54-9c96-05bd918175d1.png)


# TESTS -Backend
To run tests nevigate to backend directory using `cd` command in your shell, and run `pytest`.



