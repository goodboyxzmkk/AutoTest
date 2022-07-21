package com.ych.device;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;

public class TestToJson {

    public static void main(String[] args) {

        JSONObject jsObj = new JSONObject();
        JSONArray GoodsList = new JSONArray();
        JSONObject Goods = new JSONObject();
        JSONObject OrderExtend = new JSONObject();

        Goods.put("GoodsID", "b6c03e19-1753-4a48-b482-aba500aa0fd9");
        Goods.put("Amount", "1");
        Goods.put("DiscountPrice", "0.010000");
        GoodsList.add(Goods);


        OrderExtend.put("IsCalculatePrice", false);
        OrderExtend.put("OrderActivityType", "BulkPurchaseOrder");
        OrderExtend.put("OrderData", null);

        jsObj.put("GoodsList", GoodsList);
        jsObj.put("LeaguerID", "b459cfb6-7a19-45f0-a227-ab0c00c1374b");
        jsObj.put("CouponNumber", "");
        jsObj.put("ThirdOrderID", "FB9F73BBCAA24B8C1E5A2");
        jsObj.put("PayNumber", "11120200422023300001008be29");
        jsObj.put("PayMoney", "0.010000");
        jsObj.put("PayAccount", "4200000565202004224272538173");
        jsObj.put("Password", null);
        jsObj.put("OrderType", "WechatBuy");
        jsObj.put("CouponNumber", null);
        jsObj.put("OrderExtend", OrderExtend);

        String jsonstr = jsObj.toJSONString();
        System.out.println(jsonstr);

    }

}
