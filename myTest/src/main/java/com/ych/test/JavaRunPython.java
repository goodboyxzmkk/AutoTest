package com.ych.test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class JavaRunPython {

    public static String RumPython(String command) {
        String response_data = null;
        try {
            Process pr = Runtime.getRuntime().exec(command);
            BufferedReader b = new BufferedReader(new InputStreamReader(pr.getInputStream(), "GBK"));
            String line = null;
            StringBuilder response = new StringBuilder();
            while ((line = b.readLine()) != null) {
                response.append(line);
            }
            response_data = response.toString();
            b.close();
            pr.waitFor();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return response_data;
    }

    public static void main(String[] agrs) {
        // 传递给python的参数 -u 111 -p 222，-u,-p与python脚本中的参数名称一致,java接入python中print中的内容
        String command = "cmd /c python E://workspace//myTestTool//common//jmeter_py.py  -u areyouok -p 222";
        String response_data = RumPython(command);
        System.out.println(response_data);
    }

}
