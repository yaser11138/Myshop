# Myshop

Hi this the biggest project i have built 
this project is Online Clothes Shopping that you can buy clothes from it

things i have learned by creating this project:
<br>
-how to create shop cart
<br>
-how to work with sessions
<br>
-Become familiar with celery and message brokers
<br>
-how to create pdf file in django
<br>
-how to connect project to payment getaway

Note:
**If Celery cannot connect to RabbitMQ:**

1. **Verify RabbitMQ Service Status:**
   - Ensure the RabbitMQ service is running and accessible. You can typically check this using a service management tool or command-line utilities specific to your operating system.

2. **Create A User for it and set permissions for it:**
   - go to the Rabbitmq container or if you run it locally go to the rabbitmq command line and enter this commands:

     ```bash
     rabbitmqctl add_user superuser superuser
     rabbitmqctl set_permissions -p / superuser ".*" ".*" ".*"
     ```
     - This grants the `celery` user read/write access to exchanges and queues. You might need to adjust permissions based on your specific needs.
     - if you want to change username or password you have to change the rabbitmq config in Shop-core/settings.py line 154. write your new password and username instead of superuser:superuser 
