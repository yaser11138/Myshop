#!/bin/bash

# Start RabbitMQ server
rabbitmq-server #|| echo "Failed to start RabbitMQ server!"

# Check if setup has already been performed
if [ ! -f /var/lib/rabbitmq/.setup_done ]; then

  # Wait for RabbitMQ
  sleep 5

  # Add user
  rabbitmqctl add_user superuser superuser #|| echo "Failed to add user!"

  # Set permissions
  rabbitmqctl set_permissions -p / superuser ".*" ".*" ".*" #|| echo "Failed to set permissions!"

  # Mark setup as done
  touch /var/lib/rabbitmq/.setup_done
fi


exit 0  # Indicate successful script execution
