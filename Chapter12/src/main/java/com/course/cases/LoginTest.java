package com.course.cases;

import com.course.config.TestConfig;
import com.course.model.InterfaceName;
import com.course.model.LoginCase;
import com.course.utils.ConfigFile;
import com.course.utils.DatabaseUtil;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.ibatis.session.SqlSession;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import java.io.IOException;
import java.util.List;

public class LoginTest {

    @BeforeTest(groups = "loginTrue", description = "测试准备工作，获取httpclient")
    public void beforeTest() {
        TestConfig.getUserInfoUrl = ConfigFile.getUrl(InterfaceName.GETUSERINFO);
        TestConfig.getUserListUrl = ConfigFile.getUrl(InterfaceName.GETUSERLIST);
        TestConfig.addUserUrl = ConfigFile.getUrl(InterfaceName.ADDUSERINFO);
        TestConfig.loginUrl = ConfigFile.getUrl(InterfaceName.LOGIN);
        TestConfig.updateUserInfoUrl = ConfigFile.getUrl(InterfaceName.UPDATEUSERINFO);

        TestConfig.defaultHttpClient = new DefaultHttpClient();
    }

    @Test(groups = "loginTrue", description = "用户登陆成功接口测试")
    public void loginTrue() throws IOException {
        SqlSession session = DatabaseUtil.getSqlSession();
        //SQLMapper.xml中的id值：LoginCase
        LoginCase loginCase = session.selectOne("LoginCase", 1);
        List loginCase1 = session.selectList("LoginCase");
        System.out.println(loginCase.toString());
        System.out.println(loginCase1.toString());
        System.out.println(TestConfig.loginUrl);

    }

    @Test(groups = "loginFalse", description = "用户登陆失败接口测试")
    public void loginFalse() throws IOException {
        SqlSession session = DatabaseUtil.getSqlSession();
        LoginCase loginCase = session.selectOne("LoginCase", 2);
        System.out.println(loginCase.toString());
        System.out.println(TestConfig.loginUrl);

    }
}
