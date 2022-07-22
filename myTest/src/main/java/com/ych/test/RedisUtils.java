package com.ych.test;

import com.alibaba.fastjson.JSONObject;
import redis.clients.jedis.Jedis;

import java.util.Iterator;
import java.util.Set;

/**
 * 请问redis获取tokens
 */
public class RedisUtils {

    /**
     * 连接Redis,测试环境不需要密码验证
     * @param host
     * @param port
     */
    public static void GetRedisToken(String host, int port) {
        Jedis jedis = new Jedis(host, port);
//        jedis.auth("");
        jedis.select(0);
        Set<String> setkeys = jedis.keys("Identity:Session:*");
        Iterator<String> tokenKeys = setkeys.iterator();

        int i = 0;
        while (tokenKeys.hasNext()) {
            String key = tokenKeys.next();
            String value = jedis.get(key);
            String jsonValue = value.substring(value.indexOf("{"), value.lastIndexOf("}") + 1);
            JSONObject jsObj = JSONObject.parseObject(jsonValue);
            String templateVersion = jsObj.getString("TemplateVersion");//判断小程序登陆的token
            if (templateVersion != null) {
                System.out.println("key" + i + ":" + key.substring(17));
                System.out.println("Value" + i + ":" + jsonValue);
            }
            i++;
        }
        jedis.close();

    }

    public static void main(String[] args) {

        GetRedisToken("192.168.100.201", 6380);
    }
}
