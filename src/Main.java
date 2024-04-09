import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        Person person = new Person("Curtis", "Rubeck", LocalDate.of(1992, 9, 27));
        System.out.println(person.firstName);
        System.out.println(person.lastName);
        System.out.println(person.birthDate);
    }

}

