import java.util.List;

import com.cocresoft.commons.el.ELException;

public class TestTest {

	public static void main(String[] args) throws ELException {
		Searcher searcher = new Searcher("C://json/data_15726038.json");
		List<AD> ads;
//		System.out.println("总数为: " + searcher.totalNum());
//		ads = searcher.findByName("常熟", false, true);
//		print(ads);
//		ads = searcher.findByCode("320581", false, false);
//		print(ads);
		ads = searcher.findRouteToCode("320581003004-111");
		print(ads);
	}

	private static void print(List<AD> ads) {
		System.out.println();
		for (AD ad : ads) {
			System.out.println(ad);
		}
	}

}
