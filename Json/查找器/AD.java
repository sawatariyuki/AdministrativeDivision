package com.cocresoft.cccs.test.test;

import java.io.Serializable;
import java.util.List;

class AD implements Serializable {
	private static final long serialVersionUID = -1165839848397190074L;
	private String code;
	private String name;
	private String url;
	private List<AD> children;

	public String getCode() {
		return code;
	}

	public void setCode(String code) {
		this.code = code;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getUrl() {
		return url;
	}

	public void setUrl(String url) {
		this.url = url;
	}

	public List<AD> getChildren() {
		return children;
	}

	public void setChildren(List<AD> children) {
		this.children = children;
	}

	@Override
	public String toString() {
		return this.code + " " + this.name;
	}

	public AD getSelf() {
		AD self = new AD();
		self.setCode(this.code);
		self.setName(this.name);
		self.setUrl(this.url);
		return self;
	}

}
