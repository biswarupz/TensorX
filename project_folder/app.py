from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Define the folder to store uploaded images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html', image_paths=[])

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    aadhar = request.form['aadhar']
    image_link = request.form['link']  # Get the image link

    # Here, you can store the name, aadhar, and image_link in your database or perform any other processing.
    # For demonstration purposes, we'll just print the data.
    print(f"Name: {name}")
    print(f"Aadhar Number: {aadhar}")
    print(f"Image Link: {image_link}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
