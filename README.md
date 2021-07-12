# StoryWory
short video app 

## Backend API
Microservices based backend Application. Authentication/User Profile app using Python Django RF & MySQL and Stories/posts app using Spring boot & MongoDB.
used Apache Kafka as Event Bus which shares data between both apps using consumers and producers.Swagger UI docs for DRF app.

## Features (Django RF)
### User APIs
```
1. Registration with email
2. Verify-Email
3. Login with Email
4. refresh-token
5. Logout
```
### Profile APIs
```
1. GET My profile
2. PUT,DEL,PATCH My profile
3. GET Profile by Username
```
### Posts APIs
```
1. Add Post
2. Like & Dislike Post
```
## Features (Spring Boot)
### Posts APIs
```
1. GET all Posts
2. GET Post by Keywords(Text,Location)
3. Like & Dislike Post
```
### Kafka Topics
```
1. Addpost
```
## Working of APIs
user & Profile APIs
![user & profile](https://github.com/[robiee97]/[storywory]/screenshots/User&profileApis.jpg?raw=true)
Post APIs
![post](https://github.com/[robiee97]/[storywory]/screenshots/PostApis.jpg?raw=true)
