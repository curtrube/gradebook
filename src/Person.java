import java.time.LocalDate;
import java.util.Date;

public class Person {
    public String firstName;
    public String lastName;
    public LocalDate birthDate;

    public Person(String firstName, String lastName, LocalDate birthDate) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthDate = birthDate;
    }
}

public class Student extends Person {
    public int grade;
    public double gradePointAverage;
}