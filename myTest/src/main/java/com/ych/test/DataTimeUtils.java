package com.ych.test;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

public class DataTimeUtils {


    public static List<String> getMonthDate() {
//        Calendar cale = null;
        /**cale = Calendar.getInstance();
         int year = cale.get(Calendar.YEAR);
         int month = cale.get(Calendar.MONTH) + 1;
         int day = cale.get(Calendar.DATE);
         int hour = cale.get(Calendar.HOUR_OF_DAY);
         int minute = cale.get(Calendar.MINUTE);
         int second = cale.get(Calendar.SECOND);
         int dow = cale.get(Calendar.DAY_OF_WEEK);
         int dom = cale.get(Calendar.DAY_OF_MONTH);
         int doy = cale.get(Calendar.DAY_OF_YEAR);*/
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
        String firstday, lastday;
        // 获取前月的第一天
        Calendar cale = Calendar.getInstance();
        cale.add(Calendar.MONTH, 0);
        cale.set(Calendar.DAY_OF_MONTH, 1);
        firstday = format.format(cale.getTime());
        // 获取前月的最后一天
        cale.add(Calendar.MONTH, 1);
        cale.set(Calendar.DAY_OF_MONTH, 0);
        lastday = format.format(cale.getTime());
        List<String> startEndTime = new ArrayList();
        startEndTime.add(firstday);
        startEndTime.add(lastday);
        return startEndTime;
    }

    /**
     * 计算与当前时间相差的年份
     *
     * @param year 相差年份
     * @return 返回前后年份列表
     */
    public static List<String> getDateCalendar(int year) {
        Calendar calendar = Calendar.getInstance();
        Date date = new Date();
        calendar.setTime(date);
        calendar.add(Calendar.YEAR, year);
        SimpleDateFormat sdformat = new SimpleDateFormat("yyyy-MM-dd");
        SimpleDateFormat sdformat2 = new SimpleDateFormat("yyyy-MM-dd");  //yyyy-MM-dd HH:mm:ss
        String startTime = sdformat.format(date);
        String endTime = sdformat2.format(calendar.getTime());
        List<String> startEndDate = new ArrayList();
        startEndDate.add(startTime);
        startEndDate.add(endTime);

        return startEndDate;
    }

    public static void main(String[] args) {

        System.out.println("开始年份：" + getDateCalendar(1).get(0) + " 结束年份：" + getDateCalendar(1).get(1));
        System.out.println("开始天数：" + getMonthDate().get(0) + " 结束天数：" + getMonthDate().get(1));
    }
}
