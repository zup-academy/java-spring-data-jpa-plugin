#### inputs

- RDBMS: Sistema de gerenciamento de Banco de dados Relacional.
    - RDBMS suportados: 
        - H2
        - MySql
        - PostgreSQL

### Operações

1. A classe mapeada deve ser anotada obrigatoriamente com `@Entity` e `@Id`.
    ```JAVA
    @Entity
    public class Book {
        @Id
        private Long id;
    }
    ```
    Para mais detlhes sobre mapeamento consulte a [documentação](https://docs.jboss.org/hibernate/stable/orm/userguide/html_single/Hibernate_User_Guide.html#mapping-types) oficial.
2. Deverá ser criado uma interface que extenderá a abstração de repositorie da Spring Data JPA.
    - O primeiro argumento se referé ao tipo da entidade que o repositorie será criado.
    - O segundo argumento se trata do tipo do atributo anotado com `@Id` da entidade a qual o repositorie será criado.
    - Como boa prática anote a interface `@Transactional(readOnly = true)`.
    ```java
    @Transactional(readOnly = true)
    public interface BookRepository extends JpaRepository<Book,Long> {

    }
    ```
3. Ao realizar uma lógica de négocio que onde o resultado será persistido ao BD, anote o metodo com `@Transactional` para habilitar o controle transacional ao escopo.
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
4. Ao escrever testes a componente onde o  BD é utilizado, anote a classe de testes com `@SpringBootTest` e `@ActiveProfile("test")` para garantir que o contexto de persistência esteja disponivel e que o container docker do seu RDBMS seja utilizado na execução dos testes.

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