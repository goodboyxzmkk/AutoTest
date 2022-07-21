package com.ych.test;


import com.ych.device.Base64Utils;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class WriteToFile {
    /**
     * @param Path     写入文件路径
     * @param data     写入文件数据
     * @param isappend true为追加写入，false为覆盖写入
     */
    public static void writeToTXT(String Path, String data) {

        String filePath = Path;
        try {
            File file = new File(filePath);

            if (!file.exists()) {
                file.createNewFile();
            }
            FileOutputStream fos = new FileOutputStream(file.getAbsoluteFile(),true);  //ture为追加写入,false为覆盖写入
            //fos.write(rpData);//字节码
            fos.write((data + "\r\n").getBytes("utf-8"));
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();

        }
    }

    /**
     * @param Path     写入文件路径
     * @param data     写入文件数据
     * @param isAppend true为追加写入，false为覆盖写入
     */
    public static void writeTolog(String Path, String data) {
        String filePath = Path;
        Date date = new Date();
        SimpleDateFormat sdformat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String datatimeStr = sdformat.format(date);
        try {
            File file = new File(filePath);

            if (!file.exists()) {
                file.createNewFile();
            }
            FileOutputStream fos = new FileOutputStream(file.getAbsoluteFile(), true);  //ture为追加写入
            //fos.write(rpData);//字节码
            fos.write((datatimeStr + " ：" + data + "\r\n\r\n").getBytes("utf-8"));
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();

        }
    }

    public static void main(String[] args) {
        Date date = new Date();
        SimpleDateFormat sdformat = new SimpleDateFormat("yyyy-MM-dd");
        String filename = sdformat.format(date);

        String fileName = "D:\\jmeterlog\\" + filename+".log";
        String datastr = "测试写入数据222";
        WriteToFile.writeToTXT(fileName,datastr);


    }
}
