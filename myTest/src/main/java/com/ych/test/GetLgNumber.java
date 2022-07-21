package com.ych.test;

import java.nio.ByteBuffer;
import java.util.UUID;

/**
 * 生成会员芯片号及印刷号
 */
public class GetLgNumber {
    /**
     * 返回icnumber芯片号及印刷卡号
     * @return
     */
    public static String GetIcNum() {

        String printnumber = getNumString();
        UUID uuid = UUID.randomUUID();
        byte[] bts = GetByteArrayFromGuid(uuid.toString());
        bts[13] = 0;
        String icnumber = ByteToStr(bts);
        return icnumber + ",A" + printnumber.toUpperCase();
    }

    /**
     * 返回芯片号及二维码腕带会员编号
     * @return
     */
    public static String GetLQRNum() {

        UUID uuid = UUID.randomUUID();
        byte[] bts = GetByteArrayFromGuid(uuid.toString());
        bts[13] = 0;
        String icnumber = ByteToStr(bts);
        return icnumber + ",LQR_" + uuid.toString().toUpperCase().replaceAll("-","");
    }

    /**
     * 返回芯片号及会员号
     * @return
     */
    public static String GetLGNum() {


        UUID uuid = UUID.randomUUID();
        byte[] bts = GetByteArrayFromGuid(uuid.toString());
        bts[13] = 0;
        String icnumber = ByteToStr(bts);
        return icnumber + ",LG_" + uuid.toString().toUpperCase().replaceAll("-","");
    }

    private static String getNumString() {
        String str = "";
        for (int i = 0; i < 10; i++) {
            char c = (char) ((Math.random() * 26) + 97);
            str += (c + "");
        }

        int max = 1000000, min = 100;
        long randomNum = System.currentTimeMillis();
        int ran3 = (int) (randomNum % (max - min) + min);
        return str + ran3;
    }


    private static byte[] GetByteArrayFromGuid(String str) {
        UUID uuid = UUID.fromString(str);
        ByteBuffer bb = ByteBuffer.wrap(new byte[16]);
        bb.putLong(uuid.getMostSignificantBits());
        bb.putLong(uuid.getLeastSignificantBits());

        return bb.array();
    }


    private static String ByteToStr(byte[] bytes) {
        StringBuilder str = new StringBuilder(bytes.length * 2);
        for (byte bt : bytes) {
            str.append(String.format("%02X", bt));
        }
        return str.toString();
    }

    public static void main(String[] args) {
        String str = GetLgNumber.GetIcNum();
        String str2 = GetLgNumber.GetLQRNum();
        String str3 = GetLgNumber.GetLGNum();
        String[] strs = str.split(",");
        String[] strs2 = str2.split(",");
        String[] strs3 = str3.split(",");

        System.out.println("芯片号:" + strs[0] + "  印刷号:" + strs[1]);
        System.out.println("芯片号:" + strs2[0] + "  LQR印刷号:" + strs2[1]);
        System.out.println("芯片号:" + strs3[0] + "  LG印刷号:" + strs3[1]);
    }

}
