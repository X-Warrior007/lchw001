"""
需求:使用redis工具包里面的StrictRedis类,操作redis数据库里面的string数据类型
"""

from redis import StrictRedis

if __name__ == '__main__':
	
	try:
		# 创建StrictRedis对象
		sr = StrictRedis(host='192.168.103.129', port=6379, db=1)

		# 调用对象方法,操作string
		# 新增
		result = sr.set('name','test_sr')
		print(result)

		# 修改
		# sr.set('name', 'test')

		# 查询
		# sr.get('name')

		# 删除
		# sr.delete('name')

	except Exception as e:
		print(e)
		raise e
	