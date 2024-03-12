from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

targets = []
driver = webdriver.Chrome()

titles = [
    'https://tech12h.com/cong-nghe/trac-nghiem-ngu-van-10-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-sinh-hoc-10-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-lich-su-10-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-dia-li-10-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-tin-hoc-10-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-kinh-te-va-phap-luat-10-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-quoc-phong-ninh-10-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-ngu-van-11-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-sinh-hoc-11-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-lich-su-11-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-dia-li-11-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-tin-hoc-11-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-cong-nghe-co-khi-11-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-cong-nghe-chan-nuoi-11-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-quoc-phong-ninh-11-ket-noi-tri-thuc.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-kinh-te-phap-luat-11-ket-noi-tri-thuc.html'
    'https://tech12h.com/cong-nghe/trac-nghiem-ngu-van-12.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-sinh-hoc-12.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-lich-su-12.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-gdcd-12.html',
    'https://tech12h.com/cong-nghe/trac-nghiem-dia-ly-12.html'
]
def get_title(title):
    driver.get(title)
    try:
        content = driver.find_element(By.CLASS_NAME, "my_set")
        links = content.find_elements(By.CSS_SELECTOR, 'a')
        for link in links:
            href = link.get_attribute('href')
            if href:
                targets.append(href)
    except:
        pass
def get_lesson(target):
    driver.get(target)
    driver.implicitly_wait(10)
    content = driver.find_element(By.CLASS_NAME, "trac_nghiem")
    p_tags = content.find_elements(By.TAG_NAME,'p')
    h6 = content.find_elements(By.CSS_SELECTOR, "li h6")
    length = len(p_tags) if len(p_tags) < len(h6) else len(h6)
    with open("data/question_answer.txt","a", encoding="utf-8") as f:
        f_csv = open('data/question_answer.csv','a',encoding="utf-8")
        writer = csv.writer(f_csv)
        writer.writerow(['question', 'answer'])
        for i in range(length):
            question = p_tags[i].text
            answer = h6[i].text
            id_q = question.find(':')
            id_a = answer.find('.')
            question = question[id_q+1:]
            answer = answer[id_a+1:]
            f.write(f'[Q] {question}[A] {answer}')
            writer.writerow([question,answer])
        f_csv.close()
            
for title in titles:
    get_title(title)
for target in targets:
    get_lesson(target)

driver.quit()
