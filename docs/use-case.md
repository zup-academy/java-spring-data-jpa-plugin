## Overview

Spring Data Jpa plugin adds to a Spring Boot Stack or Project the ability to work in high performance with Spring Data and JPA/Hibernate abstractions along with the RDBMS of your choice.

### Database (DB) supported

- H2
- Mysql
- PostgreSQL

### Benefits

- HikariPool
    
    Connection pool configured to operate in high througput environments, extracting better performance from the selected DB.

- hibernate

    ORM configured to operate in high throughput environments extracting better performance from the selected DB.

- Database
    
    Database provisioned for development environment through docker-compose.

- Test Containers

    Database for test environment provisioned through docker container, favoring that your tests get as close as possible to the production environment.

- Samples
    
     Example codes to guide the use of the plugin and the writing of integration tests for the persistence layer.