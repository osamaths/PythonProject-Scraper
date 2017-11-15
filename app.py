from flask import Flask, render_template
import requests
import re
# import mysql.connector as mariadb

app = Flask(__name__)

# mariadb_connection = mariadb.connect(user='root', password='', database='mathWeb')
# cursor = mariadb_connection.cursor()



# cursor.execute("INSERT INTO mathWeb (chapter) VALUES (%s)", (chapter))

@app.route('/')
def dataFetcher():
    req = requests.get('http://www.mathhelp.com/intermediate-algebra-help/')

    collections = re.findall(r'<div class="et_pb_module et_pb_toggle et_pb_toggle_[a-z]*  et_pb_accordion_item_[0-9]">(.*?)</div> <!-- .et_pb_toggle -->', req.text, re.DOTALL)
    chapters = []

    for chapCol in collections:
        chapterName = re.findall (r'<h5 class="et_pb_toggle_title">CHAPTER [1-9]: (.*?)</h5>', chapCol)
        units = re.findall(r'Unit [0-9]: (.*?)<h5>|</div> <!-- .et_pb_toggle_content -->', chapCol, re.DOTALL)
        unitName = re.findall(r'(.*?)</h5>', str(units))
        links = re.findall (r'<p><a href=(.*?)>', str(units))
        collection = { 'chapterName': chapterName[0], 'unitName': unitName[0].split('\'')[1], 'links': links }
        chapters.append(collection)

    return render_template('index.html', chapters = chapters)

app.run(debug=True)
