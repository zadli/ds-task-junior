import easyocr, json
from flask import Flask, request

app = Flask(__name__)

reader = easyocr.Reader(['en','ru'])

@app.route('/')
def start():
	page = '<form method="post" enctype="multipart/form-data" action="/image-text-recognition"><input type="file" name="image"><button type="submit">Send</button></form>'
	return page

@app.route('/image-text-recognition', methods=['POST'])
def main():
	file = request.files['image']
	file.save(file.filename)
	data = {"out": reader.readtext(file.filename, detail = 0)}
	return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True)
