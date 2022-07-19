package com.ych.test;

import redis.clients.jedis.Jedis;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class GetRedisKeys {


    public static void ReadRedis() {
        Jedis jedis = new Jedis("192.168.100.201", 6380);
//        jedis.auth("");
        jedis.select(0);
        Set<String> setkeys = jedis.keys("Identity:Session:*");
        Iterator<String> tokenvalue = setkeys.iterator();
        int i = 0;
        while (tokenvalue.hasNext()) {
            String key = tokenvalue.next();
            System.out.println("key" + i + ":" + key.substring(17));
            i++;
        }
        jedis.close();

    }
}
