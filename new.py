from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys
driver = webdriver.PhantomJS(executable_path='D:\\PowerfulTool\\phantomjs.exe')
def get_shuoshuo(qq):
    driver.get('http://user.qzone.qq.com/{}/311'.format(qq))
    time.sleep(2)
    try:
        driver.find_element_by_id('login_div')
        print("正在登陆")
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('img_out_821816033').click()
    except:
        pass
    time.sleep(2)
    try:
        driver.switch_to.frame('app_canvas_frame')
    except:
        print("对不起，您没有权限访问该空间")
        sys.exit()
    while True:
        soup=BeautifulSoup(driver.page_source,'lxml')
        shuoshuolist=soup.ol.find_all('li',class_='feed')
        for shuoshuo in shuoshuolist:
            times=shuoshuo.find_all('a',class_='c_tx c_tx3 goDetail')
            posttime=times[len(times)-1].text
            postconcent=shuoshuo.find('pre').text
            print(posttime+postconcent)
        try:
            driver.find_element_by_link_text('下一页').click()
            time.sleep(2)
            continue
        except:
            break
    print("==========完成================")
    driver.close()
    driver.quit()
if __name__ == '__main__':
    get_shuoshuo(input("请输入qq号"))

