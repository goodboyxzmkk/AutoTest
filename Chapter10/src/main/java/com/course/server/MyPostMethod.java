package com.course.server;


import com.course.server.bean.User;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController  //标注说明我是需要被扫描的类
@Api(value = "/",description = "这是我全部的get方法")
public class MyPostMethod {

    //这个变量是用来装我们的cookies信息的
    private static Cookie cookie;

    //用户登陆成功获取到的cookies,然后再访问其他接口获取列表

    @RequestMapping(value = "/login",method = RequestMethod.POST)
    @ApiOperation(value = "登陆接口，成功后获取cookies信息",httpMethod = "POST")
    public String login(HttpServletResponse response,
                        @RequestParam(value = "userName",required = true) String userName,
                        @RequestParam(value = "password",required =true) String password){
        if (userName.equals("zhangsan")&& password.equals("123456")){
            cookie = new Cookie("login","true");
            response.addCookie(cookie);
            return "恭喜你登陆成功！！";

        }
        return "用户名或者是密码错误！";

    }
    @RequestMapping(value = "/getUserList",method = RequestMethod.POST)
    @ApiOperation(value = "获取用户列表",httpMethod = "POST")
    public String GetUserList(HttpServletRequest request,
                            @RequestBody User u){
        //获取cookies
        Cookie[] cookies =request.getCookies();
        //验证cookies是否合法
        User user;
        for (Cookie cookie:cookies){
            if (cookie.getName().equals("login")&&cookie.getValue().equals("true")&& u.getUserName().equals("zhangsan")&&u.getPassWord().equals("123456"))
            {
                user= new User();
                user.setName("lisi");
                user.setAge("18");
                user.setSex("man");
                return user.toString();
            }
        }
        return "参数不合法";
    }


}
