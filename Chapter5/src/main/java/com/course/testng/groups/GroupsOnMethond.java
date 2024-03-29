package com.course.testng.groups;

import org.testng.annotations.AfterGroups;
import org.testng.annotations.BeforeGroups;
import org.testng.annotations.Test;

public class GroupsOnMethond {
    @Test(groups = "server")
    public  void test1(){
        System.out.println("这是服务端组的测试方法1111");

    }
    @Test(groups = "client")
    public  void test2(){
        System.out.println("这是客户端的测试方法2222");

    }
    @Test(groups = "server")
    public  void test3(){
        System.out.println("这是服务端组的测试方法33333");

    }
    @Test(groups = "client")
    public  void test4(){
        System.out.println("这是客户端的测试方法44444");

    }


    @BeforeGroups("server")
    public void beforeGroupsOnServer(){
        System.out.println("这是服务端组运行之前的方法");
    }
    @AfterGroups("server")
    public void afterGroupsOnServer(){
        System.out.println("这是服务端组运行之后运行的方法");
    }
    @BeforeGroups("server")
    public void beforeGroupsOnClient(){
        System.out.println("这是客户端组运行之前的方法");
    }
    @AfterGroups("server")
    public void afterGroupsOnClient(){
        System.out.println("这是客户端组运行之后运行的方法");
    }
}
