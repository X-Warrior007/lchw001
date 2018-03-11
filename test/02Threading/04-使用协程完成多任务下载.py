from gevent import monkey
# monkey.patch_all()
import gevent
import time
import urllib.request

def down_html(url):
    # url就是网址
    print("开始请求" + url)
    # 向远处服务器发起请求  得到一个结果对象 recv
    response = urllib.request.urlopen(url)
    # 从结果对象中获取到数据      # 写入文件
    data = response.read()

    dest_file = open('douyu', 'wb')
    dest_file.write(data)
    dest_file.close()

    print("获取网页数据成功 %s 共计%d字节" %(url, len(data)))

if __name__ == '__main__':
    begin = time.time()

    g1 = gevent.spawn(down_html,"https://staticlive.douyucdn.cn/upload/game_cate/63057a52455e06c53bbd11b915bf6e9_pc.jpg")

    g1.join()
    end = time.time()

    print("总共花费 %fs" % (end-begin))