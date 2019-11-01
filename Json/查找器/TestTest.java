package com.cocresoft.cccs.test.test;

import java.util.List;

import com.cocresoft.commons.el.ELException;

public class TestTest {

	public static void main(String[] args) throws ELException {
		Searcher searcher = new Searcher();
//		System.out.println("总数为: " + searcher.totalNum());
//		List<AD> ads = searcher.findByName("常熟", false, true);
//		System.out.println(ads);
//		ads = searcher.findByCode("320581", false, false);
//		System.out.println(ads);
//		ads = searcher.findRouteToCode("320581407498-111");
//		System.out.println(ads);
		System.out.println("总数为: " + searcher.totalNum());
		List<AD> ads = searcher.findByName("潘东村村民委员会", true, false);
		System.out.println(ads);
		ads = searcher.findRouteToCode("320282103204-220");
		System.out.println(ads);
	}

	
	
	

}
