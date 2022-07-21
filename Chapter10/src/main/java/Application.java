
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication  //托管
@ComponentScan("com.course") //扫描哪个包里的类托管
public class Application {

    public static void main(String[] args) {

        SpringApplication.run(Application.class,args);

        //http://localhost:8888/swagger-ui.html  生成接口文档地址
    }
}
