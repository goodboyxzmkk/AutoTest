package com.course.testng.groups;

import org.testng.annotations.Test;

@Test(groups = "student")
public class GroupOnClass1 {
    public void stu1(){
        System.out.println("GroupOnClass111111中的stu1运行");
    }
    public void stu2(){
        System.out.println("GroupOnClass111111中的stu2运行");
    }
}
