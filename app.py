from flask import Flask,jsonify,request,render_template
import os
import model
app = Flask(__name__,  static_url_path='/static')

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'No file part'
        
        img = request.files['image']

        if img.filename == '':
            return 'No selected file'
        
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'uploads',img.filename)
        img.save(filepath)
        result = model.process_image(filepath)
        return render_template('index.html', result=result)
        
    return render_template('index.html')


if __name__ == 'main':
    app.run(debug=True)