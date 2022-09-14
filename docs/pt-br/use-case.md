## Visão Geral

Plugin Spring Data Jpa adiciona em uma Stack  ou Projeto Spring Boot a capacidade de trabalhar em alta performance com as abstrações da Spring Data e JPA/Hibernate junto ao RDBMS a sua preferência.

### Banco de dados (BD) suportados

- H2
- Mysql
- PostgreSQL

### Beneficios

- HikariPool 
    
    Pool de conexão configurado para operar em ambientes de alto througput extraindo melhor performance junto ao BD selecionado.

- Hibernate 

    ORM configurado para operar em ambientes de alto througput extraindo melhor performance junto ao BD selecionado.

- Banco de dados 
    
    Banco de dados provisionado para ambiente de desenvolvimento através do docker-compose.

- Test Containers 

    Banco de dados para ambiente de test provisionado através de container docker, favorecendo que seus testes se aproximem o maxímo possível do ambiente de produção.

- Samples
    
     Códigos de exemplo para guiar o uso do plugin e a escrita de testes de integração para camada de persistência.