package com.course.httpclient.cookies;

import org.apache.http.HttpResponse;
import org.apache.http.client.CookieStore;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.cookie.Cookie;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;
import org.testng.Assert;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import java.io.IOException;
import java.util.List;
import java.util.Locale;
import java.util.ResourceBundle;
import com.alibaba.fastjson.JSONObject;

public class MyCookiesForPost {
    private String url;
    private ResourceBundle bundle;
    //用来存储CookiesStore的变量
    private CookieStore store;
    @BeforeTest
    public void beforTest(){
        bundle=ResourceBundle.getBundle("application", Locale.CANADA);
        url= bundle.getString("test.url");
    }
    @Test
    public void testGetCookies() throws IOException {
        String result;
        String uri=bundle.getString("getCookies.uri");
        String testUrl=this.url+uri;
        HttpGet get= new HttpGet(testUrl);
        DefaultHttpClient client= new DefaultHttpClient(); //DefaultHttpClient才可以获取cookies信息
        HttpResponse response = client.execute(get);
        result = EntityUtils.toString(response.getEntity(),"gbk");
        System.out.println(result);

        //获取cookies信息
        this.store=client.getCookieStore();
        List<Cookie> cookieList= this.store.getCookies();
        for (Cookie cookie : cookieList){
            String name=cookie.getName();
            String value =cookie.getValue();
            System.out.println("cookies name="+ name+"; value="+value);
        }

    }
    @Test(dependsOnMethods = "testGetCookies")
    public  void testPostMethod() throws IOException {
        String uri=bundle.getString("test.post.with.cookies");
        //拼接最终的测试地址
        String testUrl=this.url+uri;

        //声明一个Client 对象，用来进行方法的执行
        DefaultHttpClient client = new DefaultHttpClient();

        //声明一个方法，这个方法就是post方法
        HttpPost post = new HttpPost(testUrl);

        //添加参数
        JSONObject param = new JSONObject();
        param.put("name","huhansan");
        param.put("age","18");

        //设置请求头信息,设置header
        post.setHeader("content-type","application/json");

        //将参数信息添加到方法中
        StringEntity entity =new StringEntity(param.toString(),"gbk");
        post.setEntity(entity);

        //声明一个对象进行响应结果的存储
        String result;

        //设置Cookies信息
        client.setCookieStore(this.store);

        //执行post方法
        HttpResponse response = client.execute(post);

        //获取响应结果
        result = EntityUtils.toString(response.getEntity(),"gbk");
        System.out.println(result);

        //处理结果，就是判断返回结果是否符合预期
        //将响应字符串转换为JSONObject
        JSONObject resultJson= JSONObject.parseObject(result);

        String success=resultJson.get("huhansan").toString();
        String status = resultJson.get("status").toString();
        Assert.assertEquals("success",success);
        Assert.assertEquals("1",status);


    }
}
