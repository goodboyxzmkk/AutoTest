package com.course.testng.paramter;

import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import java.lang.reflect.Method;

public class DataProviderTest {
    @Test(dataProvider = "data")
    public void testDataProvider(String name,int age){
        System.out.println("testDataProvider方法  name="+ name + "  ;  age ="+ age);
    }
    @DataProvider(name = "data")
    public Object[][] providerData(){
           Object[][] o =new Object[][]{
                   {"zxhangsan", 10},
                   {"lisi", 20},
                   {"wangwu", 30},
           };
           return o;
    }
    @Test(dataProvider = "methodData")
    public  void  test1(String name, int age){
        System.out.println("test111方法  name="+name+";age="+age);
    }
    @Test(dataProvider = "methodData")
    public  void  test2(String name, int age){
        System.out.println("test122方法  name="+name+";age="+age);
    }
    @DataProvider(name ="methodData")
    public Object[][] methodDataTest(Method method) {     //根据方法名传参
        Object[][] result = null;
        if (method.getName().equals(("test1"))) {
            result = new Object[][]{
                    {"zxhangsan", 100},
                    {"lisi", 200},
                    {"wangwu", 300},
            };
        } else if (method.getName().equals("test2")) {
            result = new Object[][]{
                    {"zxhangsan", 1000},
                    {"lisi", 2000},
                    {"wangwu", 3000},
            };
        }
        return result;
    }
}
