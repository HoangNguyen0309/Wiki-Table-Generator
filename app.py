from flask import *  
from excel2table import write2text
from table2excel import writetoexcel
from excel2table2 import write2textSingle

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
@app.route('/success3', methods = ['POST'])  
def success3():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        write2textSingle(f.filename)
        return render_template("success3.html", filename='output.txt')
@app.route('/database_download/<filename>')
def database_download(filename):
    return send_file(filename, as_attachment=True)
if __name__ == '__main__':  
    app.run(debug = True)  
