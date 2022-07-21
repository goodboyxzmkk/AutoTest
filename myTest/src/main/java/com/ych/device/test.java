package com.ych.device;

import java.util.Iterator;
import java.util.Map;
import java.util.TreeMap;

public class test {
    private Map<String, Object> getHeader( Map<String, Object> map, String key) {
        StringBuffer sige = new StringBuffer();
        Map<String, Object> headerMapTyep = new TreeMap<>();
        for (String s : map.keySet()) {
            headerMapTyep.put(s.toLowerCase(), map.get(s));
        }
//        CLog.d("Okhttp: " + map);
        Iterator<Map.Entry<String, Object>> iterator = headerMapTyep.entrySet().iterator();
        while (iterator.hasNext()) {
            Map.Entry<String, Object> entry = iterator.next();
            sige.append(entry.getKey().toLowerCase()).append("=").append(entry.getValue());
            if (iterator.hasNext()) {
                sige.append("&");
            }
        }
//        CLog.d("Okhttp: " + sige.toString());
        Map<String, Object> headerMap = new TreeMap<>();
        String genHMAC = SignUtil_SHA1.genHMAC(sige.toString(), key);
        if (genHMAC != null)
            headerMap.put("Authorization", genHMAC);
        return headerMap;
    }

    public static void main(String[] args) {

    }
}
