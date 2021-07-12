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
user & Profile APIs ![](https://github.com/robiee97/storywory/blob/main/screenshots/User&profileApis.JPG)
Post APIs ![](https://github.com/robiee97/storywory/blob/main/screenshots/PostApis.JPG)

Registeration REQ ![](https://github.com/robiee97/storywory/blob/main/screenshots/authRegisterReq.JPG)
Registeration RES ![](https://github.com/robiee97/storywory/blob/main/screenshots/authRegisterRes.JPG)
Registeration Email REQ ![](https://github.com/robiee97/storywory/blob/main/screenshots/regemail.JPG)
Registeration Email RES ![](https://github.com/robiee97/storywory/blob/main/screenshots/regemailres.JPG)
Login REQ ![](https://github.com/robiee97/storywory/blob/main/screenshots/loginreq.JPG)
Login RES ![](https://github.com/robiee97/storywory/blob/main/screenshots/loginres.JPG)
Authorization Using Access Token ![](https://github.com/robiee97/storywory/blob/main/screenshots/authorizationBearer.JPG)
Add Post REQ ![](https://github.com/robiee97/storywory/blob/main/screenshots/addpostreq.JPG)
Add Post RES ![](https://github.com/robiee97/storywory/blob/main/screenshots/addpostres.JPG)
Like REQ ![](https://github.com/robiee97/storywory/blob/main/screenshots/likereq.JPG)
Like RES ![](https://github.com/robiee97/storywory/blob/main/screenshots/likeres.JPG)
GET My Profile REQ ![](https://github.com/robiee97/storywory/blob/main/screenshots/getmyprofilereq.JPG)
GET My Profile RES ![](https://github.com/robiee97/storywory/blob/main/screenshots/getmyprofileres.JPG)
PUT My Profile REQ ![](https://github.com/robiee97/storywory/blob/main/screenshots/putmyprofilereq.JPG)
PUT My Profile RES ![](https://github.com/robiee97/storywory/blob/main/screenshots/putmyprofileres.JPG)
GET Profile By Username REQ ![](https://github.com/robiee97/storywory/blob/main/screenshots/getprofilebyusernamereq.JPG)
GET Profile By Username RES ![](https://github.com/robiee97/storywory/blob/main/screenshots/getprofilebyusernameres.JPG)
Logout REQ ![](https://github.com/robiee97/storywory/blob/main/screenshots/logoutreq.JPG)
GET ALL Posts ![](https://github.com/robiee97/storywory/blob/main/screenshots/getAllpost.JPG)
GET POSTs By Keyword ![](https://github.com/robiee97/storywory/blob/main/screenshots/getpostbyloc.JPG)








