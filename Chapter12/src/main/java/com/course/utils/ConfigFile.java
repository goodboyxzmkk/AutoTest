package com.course.utils;

import com.course.model.InterfaceName;

import java.util.Locale;
import java.util.ResourceBundle;

public class ConfigFile {

    private static ResourceBundle bundle=ResourceBundle.getBundle("application", Locale.CHINA);

    /**
     *
     * @param 测试接口名称
     * @return 返回接口地址
     */
    public static String getUrl(InterfaceName name){

        String address=bundle.getString("test.url");

        //接口uri
        String uri="";

        //最终的测试地址;
        String testUrl;
        if (name==InterfaceName.GETUSERLIST){
            uri=bundle.getString("getUserList.uri");
        }
        if (name==InterfaceName.LOGIN){
            uri=bundle.getString("login.uri");
        }
        if (name==InterfaceName.UPDATEUSERINFO){
            uri=bundle.getString("updateUserInfo.uri");
        }
        if (name==InterfaceName.GETUSERINFO){
            uri=bundle.getString("getUserInfo.uri");
        }
        if (name==InterfaceName.ADDUSERINFO){
            uri=bundle.getString("addUser.uri");
        }

        testUrl=address+uri;

        return testUrl;
    }
}
