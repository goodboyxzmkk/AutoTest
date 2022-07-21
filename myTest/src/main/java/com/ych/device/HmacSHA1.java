package com.ych.device;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

/**
 * 自助售票机、自助兑币机、验签算法
 */
public class HmacSHA1 {

    private static final String MAC_NAME = "HmacSHA1";
    private static final String ENCODING = "UTF-8";

    /**
     * 展示了一个生成指定算法密钥的过程 初始化HMAC密钥
     * @return
     * @throws Exception
     *
    public static String initMacKey() throws Exception {
    //得到一个 指定算法密钥的密钥生成器
    KeyGenerator KeyGenerator keyGenerator =KeyGenerator.getInstance(MAC_NAME);
    //生成一个密钥
    SecretKey secretKey =keyGenerator.generateKey();
    return null;
    }
     */

    /**
     * 使用 HMAC-SHA1 签名方法对对encryptText进行签名
     *
     * @param src 被签名的字符串
     * @param key 密钥
     * @return
     * @throws Exception
     */
    public static String hmacSha1(String src, String key) {
        try {
            SecretKeySpec signingKey = new SecretKeySpec(key.getBytes(), "HmacSHA1");
            Mac mac = Mac.getInstance("HmacSHA1");
            mac.init(signingKey);
            byte[] rawHmac = mac.doFinal(src.getBytes());
            return bytes2HexString(rawHmac);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private static final char hexDigits[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};

    private static String bytes2HexString(final byte[] bytes) {
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

    public static void main(String[] args) {
        String key = "C5D7C9FD354349B1A23D1DEE318D4E58";//写死
        String MacID = "bea56029-1e3e-4e27-bc62-aaea00f7f53f";
        String TerminalID = "55C95D4F-AC94-4B59-8220-AAE700EE8CF9";
        Long TS = System.currentTimeMillis();
        String data = "macid=" + MacID + "&terminalid=" + TerminalID + "&ts=" + TS; //指定排序顺序，key值小写，指定顺序
        String SIGN = HmacSHA1.hmacSha1(data, key);
        System.out.println(SIGN);
    }
}
