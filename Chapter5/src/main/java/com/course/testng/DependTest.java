package com.course.testng;

import org.testng.annotations.Test;

public class DependTest {
    @Test
    public void test1(){
        System.out.println("test1 rum");
        throw new RuntimeException();  //设置依赖方法执行失败，则test2,不执行
    }
    @Test(dependsOnMethods = {"test1"})
    public void test2(){
        System.out.println("test2 rum");
    }
    @Test
    public void test3(){
        System.out.println("test2 rum");
    }
}
