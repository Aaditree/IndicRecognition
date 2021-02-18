from flask import Flask, render_template,request
import os
app = Flask(__name__)

upload_folder=r'C:\Users\Aaditree Jaisswal\Desktop\College Final Year\BE Project\IndicRecognition\static'
DEVICE = 'cuda'
MODEL = None

def model():

def predict():

    
@app.route('/', methods=['GET','POST'])
def upload_predict():
    if request.method =="POST":
        image_file = request.files["image"]
        if image_file:
            image_location =  os.path.join(upload_folder, image_file.filename)
            image_file.save(image_location)
            return render_template("index.html", prediction=1)

    return render_template("index.html",prediction=0)

if __name__ == "__main__":
    app.run(debug=True)
