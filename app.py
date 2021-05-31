from flask import *  
from table import write2text
from write2excel import writetoexcel

app = Flask(__name__)  

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        write2text(f.filename)
        return render_template("success.html", filename='output.txt')
@app.route('/success2', methods = ['POST'])  
def success2():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        writetoexcel(f.filename)
        return render_template("success2.html", filename='output.xls')
@app.route('/database_download/<filename>')
def database_download(filename):
    return send_file(filename, as_attachment=True)
if __name__ == '__main__':  
    app.run(debug = True)  
