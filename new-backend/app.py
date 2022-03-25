from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import getData
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.getcwd() + '/temp/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
   return 'Home'

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(app.config['UPLOAD_FOLDER'] + filename)
        print("File Saved!")
        result = getData.main(app.config['UPLOAD_FOLDER'] + filename)
        res = jsonify(result)


        filetoremove = UPLOAD_FOLDER + filename

        ## If file exists, delete it ##
        if os.path.isfile(filetoremove):
            os.remove(filetoremove)
        else:    ## Show an error ##
            print("Error: %s file not found" % filetoremove)
        
        print(filetoremove)
    return res
 
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response 

if __name__ == '__main__':
   app.run(host='localhost', port=5000, debug=True)
