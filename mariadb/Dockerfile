FROM mariadb:latest

# Set the root password for MariaDB
ENV MYSQL_ROOT_PASSWORD=password

# Create a new database and user for the Python script to use
RUN mysql -u root -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE mydatabase;"
RUN mysql -u root -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL ON mydatabase.* TO 'jc'@'localhost' IDENTIFIED BY 'mypassword';"

# Expose the default MariaDB port
EXPOSE 3306

# Run the MariaDB server
CMD ["mysqld"]

