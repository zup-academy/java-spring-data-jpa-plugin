## Java Spring Data JPA Plugin

The **java-spring-data-jpa-plugin** is a plugin to enable and configure Spring Data JPA in Spring Boot Java applications.

Applying this plugin into a Spring Boot project will prepare and configure it for all those features:

1. Enables and configures Spring Data JPA using the specified database;
2. Configures Hibernate following good practices for high performance and throughput;
3. Configures HikariCP connection pool following good practices for high performance and throughput;
4. Configures application to run Spring Boot integration tests using TestContainers so that you can write good tests to validate properly your persistence layer and SQL queries;
5. Configures Docker Compose so that you can run your application locally;

All configuration and tuning is done for the specified database. At this moment, these are the supported databases:

- H2
- PostgreSQL
- MySQL

New databases will be supported soon 😊

## How to use

The following steps show how to apply the plugin to an existing Java Spring Boot application.

1. First, import our stack if you haven't done it yet:
```sh
stk import stack https://github.com/zup-academy/java-springboot-restapi-stack
```

2. Now, in the project directory, apply the plugin and answer all the questions:
```sh
stk apply plugin java-springboot-restapi-stack/java-spring-data-jpa-plugin
```

3. Still inside the project directory, you can verify whether the plugin was applied or not by checking the updated and created files:
```sh
git status
```

Nice! You're ready for production I guess 🥳

[See here the benefits and how to use the Java Spring Data JPA Plugin](https://www.youtube.com/watch?v=amlI3pHkyh8)

## Support

If you need any help, please open an [issue on Plugin's Github repository](https://github.com/zup-academy/java-spring-data-jpa-plugin). 
