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
 
