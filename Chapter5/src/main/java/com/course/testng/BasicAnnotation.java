package com.course.testng;

import org.testng.annotations.*;

public class BasicAnnotation {

    @Test
    public void  testCase1(){

        System.out.println("这是测试用例1");

    }
    @Test
    public  void  testCase2(){
        System.out.println("这是测试用例2");
    }
    @BeforeMethod
    public void beforeMethond(){

        System.out.println("beforeMethond这是在测试方法之前运行的");
    }
    @AfterMethod
    public void afterMethond(){
        System.out.println("afterMethond 这是在测试方法之后运行的");
    }
    @BeforeClass
    public void beforeClass(){
        System.out.println("beforeClass 这是在类运行之前运行的方法");
    }
    @AfterClass
    public void  afterClass(){
        System.out.println("afterClass这是在类运行之后运行的方法");
    }
    @BeforeSuite
    public void  beforeSuite(){
        System.out.println("beforeSuite在类之前运行的测试套件");
    }
    @AfterSuite
    public  void  afterSuite(){
        System.out.println("afterSuite在类之后运行的测试套件");
    }
}
