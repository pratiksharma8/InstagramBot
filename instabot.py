from selenium import webdriver
from time import sleep

print("Welcome to Instagram Bot")

user = input("Username : ")
passcode = input("Password : ")

n = int(input("How many posts to like and comment? : "))
hashtag = input("What hashtag to use? : ")
message = input("What do you want to comment? : ")


browser = webdriver.Chrome('/Users/pratiksharma/Desktop/instabot/chromedriver')
browser.implicitly_wait(5)

browser.get("https://www.instagram.com/")

username_input = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
password_input = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")

username_input.send_keys(user)
password_input.send_keys(passcode)
sleep(2)

login_button = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button")
login_button.click()
sleep(3)

browser.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
sleep(3)

post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]')
post.click()
sleep(2)

for i in range(1, n + 1):
    like = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button")
    like.click()
    sleep(1)

    try:
        comment = browser.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea")
        comment.send_keys(message)
        sleep(2)

        comment_post = browser.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button")
        comment_post.click()
        sleep(5)
    except:
        comment = browser.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea")
        comment.send_keys(message)
        sleep(2)

        comment_post = browser.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button")
        comment_post.click()
        sleep(5)

    next_one = browser.find_element_by_css_selector("._65Bje")
    next_one.click()
    sleep(2)

    print(f"{i} posts liked and commented, {n - i} posts left")

browser.close()
