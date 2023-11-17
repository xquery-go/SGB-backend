<div align="center"> <h1><u>IAM</u></h1> </div>
<div align="left">
<h5>
<u>Contains</u> :
</h5>


1. Custom User model to get user details
2. Custom groups
3. User Group mapping
4. Django Auth.user model for admin login.
5. Contains permissions module to map a group for a particular permission(s) in django Auth Group  

<h5>
<u>Tasks in line</u> :
</h5>

1. I have to enable User login (from User model) as well as admin login (Auth.user model). <b> <span style="color:green"> DONE </span> </b>
<br><br>

2. To create a token based authentication (bearer token). <b> <span style="color:green"> DONE </span> </b>
<br><br>

3. Then will be containerising this whole project. <b> <span style="color:green"> DONE </span> </b><br><br>
4. To create refresh and access token and to register them on login. <b> <span style="color:green"> DONE </span> </b>
<br><br>
5. To create GRPC server and service reflection for IAM  <b> <span style="color:yellow"> In progress </span> </b> <br><br>
6. To create a middleware that pops token from the request, uses iam service's grpc service to verify token. <b> <span style="color:red"> Not Started </span> </b><br><br>
</div>