package com.ych.test;

import java.security.SecureRandom;
import java.util.Random;

public class RandomUtils {
    private static final String ALLCHAR = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"; // 数字和26个字母组成
    private static final String ALLNUMBER = "0123456789";
    private static final String ENNUMBER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final Random RANDOM = new SecureRandom();

    /**
     * 获取指定长度的随机字母+数字
     *
     * @param length 指定字符串长度
     * @return
     */
    public static String getRandomStr(int length) {
        char[] nonceChars = new char[length];  //指定长度为6位/自己可以要求设置

        for (int i = 0; i < nonceChars.length; i++) {
            nonceChars[i] = ALLCHAR.charAt(RANDOM.nextInt(ALLCHAR.length()));
        }
        return new String(nonceChars);
    }

    /**
     * 获取指定长度的数字字符串
     *
     * @param length 指定字符串长度
     * @return
     */
    public static String getRandomNumber(int length) {
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < length; i++) {
            sb.append(ALLNUMBER.charAt(RANDOM.nextInt(ALLNUMBER.length())));
        }
        return sb.toString();

    }

    /**
     * 获取指定长度的英文字母字符串
     * @param length 指定字符串长度
     * @return
     */
    public static String getRandomEnNum(int length) {
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < length; i++) {
            sb.append(ENNUMBER.charAt(RANDOM.nextInt(ENNUMBER.length())));
        }
        return sb.toString();

    }

    public static void main(String[] args) {
        System.out.println(getRandomStr(5));
        System.out.println(getRandomStr(6));
        System.out.println(getRandomNumber(128));
        System.out.println(getRandomEnNum(128));
    }
}