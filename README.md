In-company task management service.

Features:
1. The service is an API
2. Two types of user : Employee and Customer. General fields: username, first name, last name, patronymic, email and telephone.
3. Customers can create tasks. Employees can see created tasks and assign them to themselves. After the employee has assigned himself a task,
only he can interact with her. The following people will be able to see this task: the customer who created it, the performing employee, and the administrator.
4. A task has three statuses: Waiting for executor, In process, and Finished.
5. The task has the following fields: Title, Description, Orderer, Executor, Created Date, Date of Last Modification, Closed Date, Status, and Report.
6. Authorization and authentication using access and refresh tokens.
   
Requirements:
Django~=5.0.7
djangorestframework~=3.15.2

Endpoints:
/api/token/ - send raw JSON POST request, containing username and password to authorize in system and get refresh and access tokens

/api/token/refresh/ - send raw JSON POST request, containing "refresh" token to get new access token

/api/auth/users/ - send raw JSON POST request, containing email, username, and password to create new user

/api/profiles/ - send a GET request with an access token to view a list of existing profiles

/api/tasks/ - send a GET requet with an access token as a Customer to view tasks created by this Customer
            - send a POST request, containing tittle and description of task with an access token as a Customer to create new task
            - send a GET request with an access token as an Employee to view tasks taken by this Employee
            
/api/tasks/<task's id> - send PUT request, containing status and report with access token as an Employee to change status of task having that id
