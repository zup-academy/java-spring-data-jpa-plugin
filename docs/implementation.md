#### inputs

- RDBMS: Relational Database Management System.
     - RDBMS supported:
         - H2
         - MySql
         - PostgreSQL

### Operations

1. The mapped class must be annotated with `@Entity` and `@Id`.
     ```JAVA
     @Entity
     public class Book {
         @id
         private Longid;
     }
     ```
     For more details on mapping see the official [documentation](https://docs.jboss.org/hibernate/stable/orm/userguide/html_single/Hibernate_User_Guide.html#mapping-types).

2. An interface must be created that will extend the Spring Data JPA repository abstraction.
     - The first argument refers to the type of entity that the repository will be created on.
     - The second argument is the type of the attribute annotated with `@Id` of the entity to which the repository will be created.
     - As a good practice note the `@Transactional(readOnly = true)` interface.
     ```java
     @Transactional(readOnly = true)
     public interface BookRepository extends JpaRepository<Book,Long> {

     }
     ```

3. When performing business logic where the result will be persisted to the DB, annotate the method with `@Transactional` to enable transactional control to the scope.
     ```java
     @Service
     public class BookService{
         @Autowired
         private BookRepository repository;

         @Transactional
         public void save(Book book){
             repository.save(book);
         }
     }
     ```
     
4. When writing tests for the component where the DB is used, annotate the test class with `@SpringBootTest` and `@ActiveProfile("test")` to ensure that the persistence context is available and that your RDBMS docker container is available. be used to run the tests.

     ```java
     @SpringBootTest
     @ActiveProfile("test")
     public class BookRepositoryTest{
         @Autowired
         private BookRepository repository;

         @Test
         void mustSaveABook(){
             Book book = new Book("My Book","my experience description book");

             repository.save(book);

             assertEquals(1, repository.findAll().size());
         }
     }
     ```