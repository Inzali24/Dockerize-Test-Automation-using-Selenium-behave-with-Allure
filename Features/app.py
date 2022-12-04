from cgi import test
import glob
import shutil
import subprocess
from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import send_from_directory

app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config["DEBUG"] = True

app = Flask(__name__,
            static_url_path='',
            static_folder='frontend',
            template_folder='templates')


@app.route('/')
def load_problems_file():
    path = "problems"
    filenames = glob.glob(path + "/*.html")
    name = []
    for file in filenames:
        file = file.replace("problems/", "").replace(".html", "").capitalize()
        print(file)
        name.append(file)
    return render_template('home.html', result=name)


@app.route('/index/<filename>')
def load_questions_detail(filename):
    path = "problems/"
    filepath = path + filename.lower() + ".html"
    # Opening the html file
    html_file = open(filepath, "r")
    # Reading the file
    index = html_file.read()
    # print(filepath)
    # with open(filepath, 'r') as file:
    #     data = file.read()
    #     print(data)
    return render_template('index.html', content=index, filename=filename.lower())


@app.route('/answer/<filename>', methods=['POST'])
def getResult(filename):
    data = request.form.get("sourceCode")
    path = 'answerfiles/'
    with open(path + filename.lower() + '.html', 'w') as f:
        f.write(data)
    f.close()
    #directory = "allure-report/data/test-cases"
    directory = "reports"
    feature_name = filename + '.feature'
    command_generate_allure_report = 'behave ./' + feature_name + ' -f allure_behave.formatter:AllureFormatter -o ' + directory
    subprocess.call(command_generate_allure_report, shell=True)
    # command_serve_allure_report = 'allure serve ' + directory
    # subprocess.call(command_serve_allure_report, shell=True)
    # command_combine_allure_report = 'allure-combine ./allure-report'
    # subprocess.call(command_combine_allure_report, shell=True)
    command_generate_allure_report = 'allure generate ' + directory+' --clean -o allure-report'
    subprocess.call(command_generate_allure_report, shell=True)
    command_combine_allure_report = 'allure-combine ./allure-report'
    subprocess.call(command_combine_allure_report, shell=True)
    # shutil.move("allure-report/complete.html", "templates/complete.html")
    # return redirect(url_for('test_akyint_pote',path = 'complete.html'))
    return 'Post created successfully'

@app.route('/allure-report/<path:path>')
def show_allure_report(path):
    return send_from_directory('allure-report',path)


@app.route('/answerfiles/<path:path>')
def test_route(path):
    return send_from_directory('answerfiles',path)


app.run()
