# **Java Spring Data JPA Plugin**

Java Spring Data JPA Plugin is a set of technologies and development methodology that together help in the use of Relational Database in Java Spring Boot Applications.

This Plugin has support for projects created with Stack Java Spring Boot REST API. And given that it also supports Java Spring Boot projects that use **Maven** as a dependency manager and have their property settings in the **YAML** pattern.

In the next sections you will find in detail information on how to use Java Spring Data JPA Plugin to enable the ability to handle RDBMS in your projects.

Below is a summary of each section of this documentation.

1. [Plugin Core Technologies](#plugin-base-technologies)
2. [Capabilities Enabled when using the Plugin](#what-are-the-capabilities-enabled)
3. [Benefits of using the Plugin](#what-are-the-benefits-of-using-java-spring-data-jpa-plugin)
4. [Applying Java Spring Data JPA Plugin](#applying-java-spring-data-jpa-plugin)


## **Plugin base technologies**
The purpose of this session is to inform which technologies are part of the Java Spring Data JPA Plugin.

By applying this plugin in a Java Spring Boot project, your application can benefit from the entire Spring Data and JPA/Hibernate tool infrastructure.


### **Technological Composition**

The definition of this Plugin was designed aiming at the greatest pains in the use of persistence tools with a Java application.

We understand that quality is non-negotiable, and we look to technologies and methodologies as a means to obtain the much-desired software quality. This premise was the guide for choosing each technology detailed below.


- Production environment
    - Spring Data JPA
        - Spring Data
        - Hibernate
        - HikariPool
    - JDBC drivers
        - H2
        - MySQL
        - PostgreSQL
- Development environment
    - Docker Compose
- Test environment
    - JUnit
    - TestContainers



## **What are the capabilities Enabled**

By applying the Java Spring Data JPA Plugin to your Java Spring Boot project, your project will be able to:

1. Map objects as entities and benefit from the entire JPA/Hibernate framework
2. Create Spring Data Repositories and benefit from abstractions.
3. Ability to handle high data throughput.
4. Create an automated integration test suite with TestContainers
5. Development environment set up next to Docker with Docker-compose.


## **What are the benefits of using Java Spring Data JPA Plugin**

1. Ease of configuring persistence tools in your project through the StackSpot CLI.
2. JDBC driver configuration for high performance..
3. Hibernate ORM configuration for high performance.
4. HikariPool configuration for high performance..
5. Repository Creation example codes based on good practices.
6. Integration Testing example codes based on best practices.
7. Configuration of the test environment with JUnit and TestContainers.
8. DockerCompose for using RDBMS in development environment.


[Watch this video to see the benefits of using Java Spring Data JPA Plugin in your project](https://youtu.be/8u6hdthmgu0)


## **Applying Java Spring Data JPA Plugin**

To apply the Java Spring Data JPA Plugin in your projects and enjoy its benefits, you must have the StackSpot CLI installed on your machine. [If not, follow this tutorial to install](https://docs.stackspot.com/docs/stk-cli/installation/).

### 1. Import the Stack on your machine

```sh
stk import stack https://github.com/zup-academy/java-springboot-restapi-stack
```

### 2. Now check if the Stack was successfully imported

```sh
stk list stack | grep java-springboot
```

### 3. Apply the Plugin, in your project directory, execute

```sh
stk apply plugin java-springboot-restapi-stack/java-spring-data-jpa-plugin
```

### 4. Choose a supported RDBMS

### 5. Check the changes in your project

```sh
git status
```



## Support

If you need help, please open an [issue in Stack's Github repository](https://github.com/zup-academy/java-spring-data-jpa-plugin/issues).