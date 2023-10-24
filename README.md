<div align="center"> <h1>The South German Bank Web Application </h1> </div>
<div align="left">
    Welcome to the South German Bank project.
This project is being built on microservice architecture. 
currently the focus is on 2 microservices ie. :- <br><br> 1. Identity Access Management <br> 2. SouthGermanBank

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

1. Create a GRPC reflection for IAM and SGB microservices so that each service can communicate using the reflection.
<br><br>

2. Creation of message queue system to make microservices (excluding IAM) less coupled.
<br><br>

</h5>
<h3>
Dev Notes
</h3>
<br>
Please read the System debugging IMPORTANT file on local machine to work with project.
