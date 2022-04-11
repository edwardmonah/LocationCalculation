# <u>**Location Calculation**

A Cloud Computing mini project

This is a simple app that informs a user of a location's corrdinates through LocationIQ's Geocoding
 
# Overview
  
The user is prompted to input the name of a location into a html page, as shown on the screenshot of the user interface below. The user's location search is then put through a search query in the external API. The result of the query is then flashed on the HTML page and added to the Cassandra database. The backend of the app was written in Python, using the Flask micro web framework, the front-end is written in HTML and CSS and uses the Bootstrap CSS framework for responsive design. A Cassandra image was pulled using docker and containerized to store user queries.

![image](https://user-images.githubusercontent.com/96924468/162692092-f5b3aa55-e05a-4a5f-b03d-51e36436179e.png)
 
# Cassandra 

Cassandra is a database system which stores data across multiple services to avoid data loss, it is effectively data redundancy system with similar syntax to SQL. After installation The Cassandra database can be run as follows:
 
```
sudo docker run --name cass_cluster cassandra:latest --> Creates and runs writable container
```

```
sudo docker start 4e780b0a9909488ffdc0ccb61df31f09643ce00e1fd4311a8494552ad5bda459 ---> starts container instance
```
 
``` 
docker exec -it cass_cluster cqlsh ---> executes cassandra and allows us to interact with the database
```
 
# Kubernetes

Kubernetes was used as a container management and load balancing tool as shown below. We use one cluster in which there are three nodes.

![image](https://user-images.githubusercontent.com/96924468/162695851-4400c7ef-b2e1-4456-b52c-39354b44f676.png)
 
 
 # Setup
 
 This repository can be clones in your own virtual machine using the following command:
 
 ```
 git clone https://github.com/edwardmonah/LocationCalculation.git
 ```
Building and deploying the repository requires the folowing commands:
 
```
 $ sudo docker build . --tag=tester
 sudo docker run -p 80:80 tester
```
'tester' is of course an arbitrary tag and can be edited to any other phrase of your liking.
 (note: This application as it is will not run without a Cassandra database. After deploying your Cassandra Database, the IP and port number can be added to the app2.py file replacing the default values - 172.17.0.1:9042)
 
 #Creating Docker image and pushing to Dockerhub
 
 The following commands were used to create the docker image
 ```
 gcloud projects list
```
 was used to check for the ID of this project.
 
 The project was then exported using:
 <pre>
 export PROJECT_ID= <b>enter your ID from the last step here</b>
 </pre>
 This command was used to create the Docker image:
 
 <pre>
 sudo docker build -t <b>enter your prefered tag here</b> .
 </pre>
 You can check to see id the image was built with this command:
 ```
 sudo docker images
 ```
 
 A dockerhub repository needs to made for the next step.
 This can be made by simply making a dockerhub account and making a blank repository. A repository called **location** was made for this project and it is referenced in the code as **myrepo/location** where **myrepo** is the name of the dockerhub account
 
 Pushing the image to the dockerhub goes as follows:
 ```
sudo docker image tag MyApp:latest myrepo/MyApp:latest
sudo docker login 
sudo docker push myrepo/MyApp:latest
 ```
You will be prompted to enter your login credentials at the second step.
 
If successful, your image will be available in your repository under the 'Tags' heading
 
 ![image](https://user-images.githubusercontent.com/68447389/162817499-e002014a-6869-4c5f-be59-bececc6b9c69.png)

 
 
 
 
 
 
 
 
