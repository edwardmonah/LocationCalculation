# <u>**Location Calculation**

A Cloud Computing mini project

This is a simple app that informs a user of a location's corrdinates through LocationIQ's Geocoding
 
# Overview
  
The user is prompted to input the name of a location into a html page, as shown on the screenshot of the user interface below. The user's location search is then put through a search query in the external API. The result of the query is then flashed on the HTML page and added to the Cassandra database.

![image](https://user-images.githubusercontent.com/96924468/162692092-f5b3aa55-e05a-4a5f-b03d-51e36436179e.png)
 
# Cassandra 

Cassandra is a database system which stores data across multiple services to avoid data loss, it is effectively data redundancy system with similar syntax to SQL.
 
To build image

Sudo docker build .-tag-cassandrarest:v1
 
To run it as a service, exposing the deployment to get an external IP:
 
sudo docker run --cass_cluster, cassandra:latest

sudo docker run -p 80:80 cassandrarest:v1

sudo docker run -p 443:443 cassandrarest:v1 for https

# Kubernetes

Kubernetes was used as a container management and load balancing tool

![image](https://user-images.githubusercontent.com/96924468/162695851-4400c7ef-b2e1-4456-b52c-39354b44f676.png)
 


