package com.ych.device;

import com.ych.test.WriteToFile;
import sun.misc.BASE64Encoder;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.util.Base64;
import java.util.Objects;

public class Base64Utils {


    public static String ImageToBase64(String imgPath) {
        byte[] data = null;
        // 读取图片字节数组
        try {
            InputStream in = new FileInputStream(imgPath);
            data = new byte[in.available()];
            in.read(data);
            in.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        // 对字节数组Base64编码
        BASE64Encoder encoder = new BASE64Encoder();
        // 返回Base64编码过的字节数组字符串
        return encoder.encode(Objects.requireNonNull(data));
//        System.out.println("本地图片转换Base64:" + encoder.encode(Objects.requireNonNull(data)))
    }

    /***
     * 字符串转base64
     * @param str
     * @return
     */
    public static String StrTobase64(String str) {
        String base64encodedString = "";
        try {
            base64encodedString = Base64.getEncoder().encodeToString(str.getBytes("utf-8"));
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }

        return base64encodedString;
    }

    /***
     * base64转字符串
     * @param base64str
     * @return
     */
    public static String Base64ToString(String base64str) {
        // 解码
        byte[] base64decodedBytes = Base64.getDecoder().decode(base64str);
        String base64tostr = "";

        try {
            base64tostr = new String(base64decodedBytes, "utf-8");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }

        return base64tostr;
    }

    public static void main(String[] args) {
        String base64str = ImageToBase64("D:\\jmeterlog\\TestSucess\\timg.jpg");
        String str = StrTobase64("abcdefg");
        String str2 = Base64ToString(str);
//        System.out.println("本地图片转换Base64:" + base64str);
        WriteToFile.writeToTXT("D:\\jmeterlog\\leaguerImg.txt", base64str);
        WriteToFile.writeToTXT("D:\\jmeterlog\\str.txt", str);
        WriteToFile.writeToTXT("D:\\jmeterlog\\str2.txt", str2);
    }

}