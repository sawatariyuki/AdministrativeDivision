# -*- coding: utf-8 -*-
import json
import time

filename = 'data'

def buildTree(treeNode, dataDict):
  parentCode = treeNode['code']
  if parentCode in dataDict:
    for child in dataDict[parentCode]:
      childNode = {}
      childNode['code'] = child['code']
      childNode['name'] = child['name']
      childNode['children'] = []
      if 'url' in child:
          childNode['url'] = child['url']
      treeNode['children'].append(childNode)
      buildTree(childNode, dataDict)

def main():
  with open('./' + filename + '.json', 'r', encoding='utf8') as f:
    data = json.load(f)

  # 预处理subCode, 并按code处理成dict {parentCode:[], ...}
  dataDict = {}
  for item in data:
    if 'subCode' in item:
      item['code'] = item['code'] + '-' + item['subCode']
      item.pop('subCode')
    parentCode = item['parentCode']
    if parentCode not in dataDict:
      dataDict[parentCode] = []
    dataDict[parentCode].append(item)

  tree = {}
  tree['code'] = '2018'
  tree['name'] = '2018年统计用区划代码'
  tree['url'] = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html'
  tree['children'] = []
  buildTree(tree, dataDict)

  dataStr = json.dumps(tree)
  with open('./' + filename + '_' + str(time.time())[0:8] + '.json', 'w', encoding='utf8') as f2:
    f2.write(dataStr)

if __name__ == '__main__':
  main()