<div align="center"> <h1>The South German Bank Web Application </h1> </div>
<div align="left">
    Welcome to the South German Bank project.
This project is currently based on monolithic architecture. but soon it will be migrated over to microservices 
architecture with at least 2 microservices ie. :- <br><br> 1. Identity Access Management <br> 2. SouthGermanBank

<br>
<h3>
IAM
</h3>
This module handles all the communication related to user login, password management, token access, api access,
module permissions, request logs etc.
</div>
<h3>
SouthGermanBank
</h3>
This module (currently) handles all the business logic related to the bank. Currently, it has three main applications :- 
<br>
1. Customers <br> 2. Visitors <br> 3. Data Cleaner <br> 4. Data Reader
<br> <br> <br>
<h3>
Tasks
</h3>
<h5>

1. In the coming time I will be uploading a django project for payments which will handle all the payment transactions since it is a high velocity and high veracity data.
<br><br>

2. Next task will be to separate these modules into separate microservices using gRPC and protocol buffers and move the solution on a different branch. 
<br><br>

3. Then will be containerising this whole project.
<br><br>

4. Then will integrate blockchain for transactions on a separate microservice. 


</h5>


