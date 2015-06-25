from selenium import webdriver
import getpass
import html2text
import re

username = ""
password = ""
keywords = []
limit = 10000

login_form_url = "https://www.topcoder.com/reg2/showRegister.action"
editorial_wiki_url = "http://apps.topcoder.com/wiki/display/tc/Algorithm+Problem+Set+Analysis"

def get_username():
    global username
    if username: return

    username = raw_input("Handle: ")

def get_password():
    global password
    if password: return

    password = getpass.getpass("Password: ")

def login_attempt(driver):
    driver.get(login_form_url)

    get_username()
    get_password()

    username_field = driver.find_element_by_name("handle")
    password_field = driver.find_element_by_name("password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    password_field.submit()

def get_text_from_span(driver, element):
    return driver.execute_script("""
        var parent = arguments[0];
        var child = parent.firstChild
        return child.textContent;
        """, element) 

def get_href_from_anchor(driver, element):
    return driver.execute_script("""
        var parent = arguments[0];
        return parent.getAttribute("href");
        """, element) 

def get_titles(driver, editorials):
    titles = []
    for editorial in editorials:
        title = get_text_from_span(driver, editorial)
        titles.append(title)

    return titles 

def get_urls(driver, editorials):
    urls = []
    for editorial in editorials:
        url = get_href_from_anchor(driver, editorial)
        urls.append(url)

    return urls 

def get_page_source(driver, editorial_url):
    driver.get(editorial_url)
    return driver.page_source

def get_text_from_html(html):
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_emphasis = True

    return h.handle(html)

def does_match(text):
    for keyword in keywords:
        keyword = r"\b" + re.escape(keyword) + r"\b"
        m = re.search(keyword, text, re.IGNORECASE)
        if m != None: return True

    return False

def get_matched_srms(driver, titles, urls):
    matched_srms = []
    for i in range(0, len(urls)):
        title = titles[i]
        url = urls[i]

        html = get_page_source(driver, url)
        text = get_text_from_html(html)

        if does_match(text):
            matched_srms.append((title, url))

        if len(matched_srms) >= limit:
            break

    return matched_srms

def render_html(srms):
    file = open("index.html", "w+")

    file.write("<!DOCTYPE html>\n")
    file.write("<html>\n")
    file.write("<body>\n")

    for (title, url) in srms:
        file.write("<a href=\"" + url + "\">")
        file.write(title)
        file.write("</a>\n")
        file.write("</br>\n")

    file.write("</body>\n")
    file.write("</html>\n")

def main():
    driver = webdriver.Firefox()
    login_attempt(driver)

    driver.get(editorial_wiki_url)
    editorials = driver.find_elements_by_class_name("analysis")

    titles = get_titles(driver, editorials)
    urls = get_urls(driver, editorials)

    srms = get_matched_srms(driver, titles, urls)
      
    render_html(srms)
    driver.close()

if __name__ == "__main__": main()
