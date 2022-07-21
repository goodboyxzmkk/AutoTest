package com.ych.device;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

/**
 * 加密工具
 * 作者：VJKuo on 2019-07-09 15:05
 * 邮箱：529844698@qq.com
 */
public class SignUtil_SHA1 {

    /**
     * 使用 HMAC-SHA1 签名方法对data进行签名
     *
     * @param data 被签名的字符串
     * @param key  密钥
     * @return 加密后的字符串
     */
    private static final String HMAC_SHA1_ALGORITHM = "HmacSHA1";
    public static final String KEY = "C5D7C9FD354349B1A23D1DEE318D4E58";

    private static final char hexDigits[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};

    public static String bytes2HexString(final byte[] bytes) {
        if (bytes == null) return null;
        int len = bytes.length;
        if (len <= 0) return null;
        char[] ret = new char[len << 1];
        for (int i = 0, j = 0; i < len; i++) {
            ret[j++] = hexDigits[bytes[i] >>> 4 & 0x0f];
            ret[j++] = hexDigits[bytes[i] & 0x0f];
        }
        return new String(ret);
    }

    public static String genHMAC(String data, String key) {
        String result = null;
        try {
            //根据给定的字节数组构造一个密钥,第二参数指定一个密钥算法的名称
            SecretKeySpec signinKey = new SecretKeySpec(key.getBytes(), HMAC_SHA1_ALGORITHM);
            //生成一个指定 Mac 算法 的 Mac 对象
            Mac mac = Mac.getInstance(HMAC_SHA1_ALGORITHM);
            //用给定密钥初始化 Mac 对象
            mac.init(signinKey);
            //完成 Mac 操作
            byte[] rawHmac = mac.doFinal(data.getBytes());
            result = bytes2HexString(rawHmac).toUpperCase();

        } catch (NoSuchAlgorithmException e) {
            System.err.println(e.getMessage());
        } catch (InvalidKeyException e) {
            System.err.println(e.getMessage());
        }
        if (null != result) {
            return result;
        } else {
            return null;
        }
    }

    public static void main(String[] args) throws InterruptedException {
//        硬件设备登录验签
        for (int i = 0; i < 10; i++) {
            Thread.sleep(200);
            String MacID = "19dd4089fd074ff4a01c3b16dd2d547a696B";
            Long TS = System.currentTimeMillis();
            String TerminalType = "12";
            String data = "macid=" + MacID + "&terminaltype=" + TerminalType + "&ts=" + TS;
            String sign = genHMAC(data, KEY);
            System.out.println(sign);
        }

    }


}
