package com.course.server.bean;

import lombok.Data;  //lombok插件，自动生成get，set方法

@Data
public class User {
    private String userName;
    private String passWord;
    private String name;
    private String age;
    private String sex;
}
