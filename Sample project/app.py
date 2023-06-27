# from flask import Flask, render_template, request
# import requests
# from bs4 import BeautifulSoup


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/check_price', methods=['POST'])
# def check_price():
#     # Get the user input from the form
#     url = request.form['url']
#     desired_price = float(request.form['price'])

#     # Set the headers to pretend to be a browser
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

#     # Get the HTML code of the product page
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find the price element on the page
#     price = soup.find('span', class_="a-price-whole").get_text()
#     price = float(price[1:])  # convert price from string to float and remove '$' sign

#     # Compare the price with the desired price and return the result to the template
#     if price <= desired_price:
#         return render_template('result.html', result=f"The price has dropped to {price}!")
#     else:
#         return render_template('result.html', result=f"The price is still {price}.")

   
# from flask import Flask, render_template, request
# import requests
# from bs4 import BeautifulSoup
# import smtplib

# app = Flask(__name__)

# def check_price(url, desired_price,email):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
#     page = requests.get(url, headers=headers)

#     soup = BeautifulSoup(page.content, 'html.parser')

#     #extracting the title
#     title = soup.find(id="productTitle").get_text()

#     #extracting the price
#     price = soup.find('span', class_="a-price-whole").get_text()
#     price = price[0:8].replace(',','')
#     price = int(float(price))

#     if price < desired_price:
#         send_mail(url, title,email)

# def send_mail(url, title,email):
#     message = f"Subject: Amazon Price Alert!\n\nThe price for {title} has fallen below your desired price.\n{url}"

#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()

#     server.login('trisjane018@gmail.com', 'guyf jsee ibuu ccgy')
#     server.sendmail('trisjane018@gmail.com', email, message)
#     print("Email has been sent")

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/price', methods=['POST'])
# def price():
#     url = request.form['url']
#     desired_price = float(request.form['price'])
#     email = request.form['mail']
#     check_price(url, desired_price,email)
#     return "Price check complete. Check your email for an alert if the price has dropped!"

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from apscheduler.schedulers.background import BackgroundScheduler
# import requests
# import smtplib
# from email.mime.text import MIMEText
# from bs4 import BeautifulSoup

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<root>:<rootpass>@<localhost>/<newpdt>'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200))
#     url = db.Column(db.String(500))
#     target_price = db.Column(db.Float)

# def check_price():
#     products = Product.query.all()

#     for product in products:
#         url = product.url
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
#         page = requests.get(url, headers=headers)
#         soup = BeautifulSoup(page.content, 'html.parser')
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#         price = soup.find('span', class_="a-price-whole").get_text()
#         price = price[0:8].replace(',','')
#         price = int(float(price))

#         if price >= product.target_price:
#             send_notification(product)

# def send_notification(product):
#     sender_email = 'your_sender_email@gmail.com'
#     sender_password = 'your_sender_password'
#     recipient_email = 'your_recipient_email@gmail.com'
#     subject = f'Target Price Reached for {product.name}!'
#     message = f'The price of {product.name} has reached the target price of ${product.target_price}. Click here to buy it now: {product.url}'

#     msg = MIMEText(message)
#     msg['From'] = sender_email
#     msg['To'] = recipient_email
#     msg['Subject'] = subject

#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(sender_email, sender_password)
#     server.sendmail(sender_email, recipient_email, msg.as_string())
#     server.quit()

# scheduler = BackgroundScheduler()
# scheduler.add_job(func=check_price, trigger='interval', minutes=60)  # check price every hour
# scheduler.start()

# if __name__ == '__main__':
#     app.run()

# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from apscheduler.schedulers.background import BackgroundScheduler
# import requests
# import smtplib
# from email.mime.text import MIMEText
# from bs4 import BeautifulSoup
# import mysql.connector

# app = Flask(__name__)

# # Connect to database
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="rootpass",
#     database="product"
# )

# # Function to check price and send email
# def check_price():
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM users")
#     users = cursor.fetchall()
#     for user in users:
#         url = user[1]
#         target_price = user[2]
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

#         res = requests.get(url, headers=headers)
#         soup = BeautifulSoup(res.text, 'html.parser')

#         try:
#             title = soup.find('span', {'id': 'productTitle'}).get_text().strip()
#             # price = soup.find('span', {'id': 'priceblock_ourprice'}).get_text().strip()[1:].replace(',', '')
#             price = soup.find('span', class_="a-price-whole").get_text()
#             price = price[0:8].replace(',','')
#             price = int(float(price))
#         except:
#             continue

#         converted_price = float(price)
#         if(converted_price <= float(target_price)):
#             send_email(user[0], url, title,price)

# # Function to send email
# def send_email(email, url, title,price):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()

#     server.login('trisjane018@gmail.com', 'guyf jsee ibuu ccgy')

#     subject = f"{title} is now {price}!"
#     body = f"Check the Amazon link: {url}"

#     msg = f"Subject: {subject}\n\n{body}"

#     server.sendmail(
#         'trisjane018@gmail.com',
#         email,
#         msg
#     )
#     print("Email has been sent to", email)

#     server.quit()

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/form')
# def form():
#     return render_template('formpage.html')

# # Route to add user
# @app.route('/add', methods=['POST'])
# def add_user():
#     email = request.form['email']
#     url = request.form['url']
#     target_price = request.form['target_price']
#     cursor = db.cursor()
#     sql = "INSERT INTO users (email, url, target_price) VALUES (%s, %s, %s)"
#     val = (email, url, target_price)
#     cursor.execute(sql, val)
#     db.commit()
#     check_price()
#     return "added successfully"

# scheduler = BackgroundScheduler()
# scheduler.add_job(func=check_price, trigger='interval', minutes=60)  # check price every hour
# scheduler.start()


# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import mysql.connector
import requests
from bs4 import BeautifulSoup
import smtplib
from flask_apscheduler import APScheduler

app = Flask(__name__)

# Connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpass",
    database="product1"
)

# Function to check price and send email
# def check_price():
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM users")
#     users = cursor.fetchall()
#     for user in users:
#         email=user[0]
#         url = user[1]
#         target_price = user[2]
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

#         res = requests.get(url, headers=headers)
#         soup = BeautifulSoup(res.text, 'html.parser')

#         try:
#             title = soup.find('span', class_='B_NuCI').get_text().strip()
#             # price = soup.find('span', {'id': 'priceblock_ourprice'}).get_text().strip()[1:].replace(',', '')
#             price = soup.find('span', class_="_30jeq3 _16Jk6d").get_text()
#             price = price[0:8].replace(',','')
#             price = int(float(price))
#         except:
#             continue

#         converted_price = float(price)
#         if(converted_price <= float(target_price)):
#             send_email(email, url, title,price)

def check_price_amazon():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        email=user[0]
        url = user[1]
        target_price = user[2]
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        
        try:
            title = soup.find('span', {'id': 'productTitle'}).get_text().strip()
            price = soup.find('span', class_="a-price-whole").get_text()
            price = price[0:8].replace(',','')
            price = int(float(price))
            print(price)
        except:
            continue

        price = float(price)
        if(price <= float(target_price)):
            send_email(email, url, title,price)

def check_price_flipkart():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users1")
    users1 = cursor.fetchall()
    print(cursor.rowcount)
    for user1 in users1:
        email=user1[0]
        url = user1[1]
        target_price = user1[2]
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        # soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
        
        title = soup.find("span",{"class":"B_NuCI"}).get_text().strip()
        price = soup.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()
        price = price[0:8].replace(',','')
        price = price.replace("₹", "")
        price = int(float(price))
            # price = soup.find('div', attrs={"class": "_16Jk6d"}).text
            # # remove Rs symbol from price
            # price = price[1:]
            # # remove commas from price
            # price = price.replace(",", "")
            # # convert price from string to int
            # price = int(float(price)) 
        
        price = float(price)
        if(price <= float(target_price)):
            print(price)
            send_email(email, url, title,price)



# Function to send email
def send_email(email, url, title,price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('trisjane018@gmail.com', 'guyf jsee ibuu ccgy')

    title = title.encode('ascii', 'ignore').decode('ascii')
    url = url.encode('ascii', 'ignore').decode('ascii')
    
    subject = f"{title} is now {price}!"
    body = f"Check the Amazon link: {url}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'trisjane018@gmail.com',
        email,
        msg
    )
    print("Email has been sent to", email)

    server.quit()
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('formpage.html')

@app.route('/form1')
def form1():
    return render_template('formpage1.html')


# Route to add user
@app.route('/add', methods=['POST'])
def add_user():
    email = request.form['email']
    url = request.form['url']
    target_price = request.form['target_price']
    if 'amazon' in url:
        cursor = db.cursor()
        sql = "INSERT INTO users (email, url, target_price) VALUES (%s, %s, %s)"
        val = (email, url, target_price)
        cursor.execute(sql, val)
        db.commit()
        check_price_amazon()
        return render_template('success.html')
    elif 'flipkart' in url:
        cursor = db.cursor()
        sql = "INSERT INTO users1 (email, url, target_price) VALUES (%s, %s, %s)"
        val = (email, url, target_price)
        cursor.execute(sql, val)
        db.commit()
        check_price_flipkart()
        return render_template('success.html')
    else:
        print("Invalid URL")

# Create scheduler object
scheduler = APScheduler()

# Define job to check price every hour
@scheduler.task('interval', id='check_price', hours=1)
def check_price_job():
    check_price_amazon()
    check_price_flipkart()

if __name__ == '__main__':
    # Start scheduler
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True)

# if __name__ == '__main__':
#     app.run(debug=True)
