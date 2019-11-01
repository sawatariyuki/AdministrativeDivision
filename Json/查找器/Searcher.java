import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

import com.google.gson.Gson;

class Searcher {
	private AD ad;

	public Searcher(String fileName) {
		if (fileName == null) {
			ad = new AD();
			return;
		}
		String json = readFile(fileName);
		Gson gson = new Gson();
		ad = gson.fromJson(json, AD.class);
	}

	public int totalNum() {
		Stack<AD> stack = new Stack<AD>();
		stack.push(ad);
		int total = 0;
		while (!stack.isEmpty()) {
			AD node = stack.pop();
			total += node.getChildren().size();
			for (AD child : node.getChildren()) {
				stack.push(child);
			}
		}
		return total;
	}

	/**
	 * 按名称搜索
	 * @param name 关键字
	 * @param exactly 是否完全匹配
	 * @param containsChildren 是否包含children
	 * @return
	 */
	public List<AD> findByName(String name, boolean exactly, boolean containsChildren) {
		List<AD> result = new ArrayList<AD>();
		if (name == null) {
			return result;
		}
		Stack<AD> stack = new Stack<AD>();
		stack.push(ad);
		while (!stack.isEmpty()) {
			AD node = stack.pop();
			if (exactly) {
				if (name.equals(node.getName())) {
					if (containsChildren) {
						result.add(node);
					} else {
						result.add(node.getSelf());
					}
				}
			} else {
				if (node.getName() != null && node.getName().contains(name)) {
					if (containsChildren) {
						result.add(node);
					} else {
						result.add(node.getSelf());
					}
				}
			}
			for (AD child : node.getChildren()) {
				stack.push(child);
			}
		}
		return result;
	}

	/**
	 * 按编码搜索
	 * @param code 编码
	 * @param exactly 是否完全匹配
	 * @param containsChildren 是否包含children
	 * @return
	 */
	public List<AD> findByCode(String code, boolean exactly, boolean containsChildren) {
		return _findByCode(null, code, exactly, containsChildren);
	}

	/**
	 * 按确切编码查找路径
	 * @param code
	 * @return
	 */
	public List<AD> findRouteToCode(String code) {
		List<AD> result = new ArrayList<AD>();
		if (code == null) {
			return result;
		}
		Stack<AD> stack = new Stack<AD>();
		for (AD child : ad.getChildren()) {
			stack.push(child);
		}
		while (!stack.isEmpty()) {
			AD node = stack.pop();
			if (!_findByCode(node, code, true, false).isEmpty()) {
				result.add(node.getSelf());
				stack.clear();
				for (AD child : node.getChildren()) {
					stack.push(child);
				}
			}
		}
		return result;
	}

	private List<AD> _findByCode(AD root, String code, boolean exactly, boolean containsChildren) {
		List<AD> result = new ArrayList<AD>();
		if (code == null) {
			return result;
		}
		Stack<AD> stack = new Stack<AD>();
		if (root != null) {
			stack.push(root);
		} else {
			stack.push(ad);
		}
		while (!stack.isEmpty()) {
			AD node = stack.pop();
			if (exactly) {
				if (code.equals(node.getCode())) {
					if (containsChildren) {
						result.add(node);
					} else {
						result.add(node.getSelf());
					}
				}
			} else {
				if (node.getCode() != null && node.getCode().contains(code)) {
					if (containsChildren) {
						result.add(node);
					} else {
						result.add(node.getSelf());
					}
				}
			}
			for (AD child : node.getChildren()) {
				stack.push(child);
			}
		}
		return result;
	}

	/**
	 * 一次性读取全部文件数据
	 * @param strFile
	 */
	private String readFile(String strFile) {
		String result = null;
		try {
			InputStream is = new FileInputStream(strFile);
			int iAvail = is.available();
			byte[] bytes = new byte[iAvail];
			is.read(bytes);
			result = new String(bytes);
			is.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return result;
	}

	@SuppressWarnings("unused")
	private void write(String content, String fileName) {
		try {
			File file = new File(fileName);
			if (!file.exists()) {
				file.createNewFile();
			}
			FileWriter fileWriter = new FileWriter(file.getAbsoluteFile());
			BufferedWriter bw = new BufferedWriter(fileWriter);
			bw.write(content);
			bw.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
