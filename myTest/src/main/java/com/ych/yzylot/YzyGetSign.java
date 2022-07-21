package com.ych.yzylot;

import com.alibaba.fastjson.JSONObject;
import com.ych.device.SignUtil_SHA1;
import com.ych.test.RandomUtils;
import java.util.UUID;

public class YzyGetSign {

    /**
     * 签名放在头里面 Authorization
     * 获得Authorization值
     *
     * @param map     要签名的数据
     * @param signKey 密钥
     * @return 签名后的数据
     */
    public static String getSign(String map, String signKey) {
        String sign = SignUtil_SHA1.genHMAC(map, signKey);
        return sign;
    }

    public static String getMacID() {
        String macID = UUID.randomUUID().toString().replaceAll("-", "");
        String sign = SignUtil_SHA1.genHMAC(macID, getRegisterKey());
        return macID + sign.substring(0, 4);

    }

    public static String getRegisterKey() {
        return "3A5B6BF5FAB891783A5B6CF4FAF79275";
    }

    public static void main(String[] args) {

        String macid = YzyGetSign.getMacID();
        long timeSpan = System.currentTimeMillis();
        JSONObject obj = new JSONObject();
        obj.put("MacID", macid);
        obj.put("TimeSpan", Long.toString(timeSpan));
        obj.put("OSVer", "7.1.2");
        obj.put("MainBoardNum", RandomUtils.getRandomStr(5));
        obj.put("Memery", RandomUtils.getRandomStr(5));
        obj.put("Disk", RandomUtils.getRandomStr(5));
        obj.put("OSName", RandomUtils.getRandomStr(5));
        obj.put("OSVerName", RandomUtils.getRandomStr(5));
        obj.put("RegCode", "YZYNMPEloAcPklkVvLaLil8Qw||52953DB5E1CBCF02760F15C2C397D6631655F771");

        String jsonObjStr = obj.toJSONString();
        String yzySign = YzyGetSign.getSign(jsonObjStr, getRegisterKey());
        System.out.println("sign值：" + yzySign);
    }

}
