from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400
        if file:
            input_image = Image.open(file.stream)
            output_image = remove(input_image, post_process_mask=True)
            imgIO = BytesIO()
            output_image.save(imgIO, 'PNG')
            imgIO.seek(0)
            return send_file(imgIO, mimetype='image/png', as_attachment=True, download_name=f"{file.filename}.png")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)
