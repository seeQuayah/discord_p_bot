import requests
import mysql.connector as mariadb

class Scrapper:

    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect_db()
    
    def connect_db(self):
        self.connection = mariadb.connect(
            user="jc",
            password="password_database",
            host="mariadb",
            port=3306,
            database="discord_p"
        )
        self.cursor = self.connection.cursor()

    def create_category(self, category):
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS natural_tits (
            id INT NOT NULL AUTO_INCREMENT,
            thread_url VARCHAR(400) NOT NULL,
            image_url VARCHAR(400) NOT NULL,
            primary key(id));""")

    def scrap_content(self, category):
        offset = 1
        self.create_category(category)
        self.connection.commit()
        url = f"https://www.pornpics.com/{category}/?limit=500&offset="
        while True:
            body = requests.get(url+str(offset)).json()
            if body == []:
                break
            for child in body:
                thread_url = child['g_url']
                image_url = child['t_url']
                self.cursor.execute(f"INSERT INTO natural_tits (thread_url, image_url) VALUES (%s, %s);", (thread_url, image_url,))
                self.connection.commit()

    def close_db(self):
        self.connection.close()

scp = Scrapper()
scp.scrap_content("natural-tits")
scp.close_db()


