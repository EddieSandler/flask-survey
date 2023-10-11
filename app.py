from flask import Flask,request,render_template
from surveys import satisfaction_survey
# from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
# app.debug = True
app.config['SECRET_KEY'] = 'I got this'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# toolbar = DebugToolbarExtension(app)
responses = []

@app.route('/')
def get_survey():
    title=satisfaction_survey.title
    instructions=satisfaction_survey.instructions

    return render_template('base.html',title=title,instructions=instructions)

@app.route('/questions/0',methods=['POST','GET'])
def show_question1():

    this_question=satisfaction_survey.questions[0].question


    return render_template('question1.html',this_question=this_question)


@app.route('/questions/1',methods=['POST','GET'])
def show_question2():

    this_question=satisfaction_survey.questions[1].question



    return render_template('question2.html',this_question=this_question)

@app.route('/questions/2')
def show_question3():

    this_question=satisfaction_survey.questions[2].question
    choice_1=satisfaction_survey.questions[2].choices[0]
    choice_2=satisfaction_survey.questions[2].choices[1]






    return render_template('question3.html',this_question=this_question,choice1=choice_1,choice2=choice_2)

@app.route('/questions/3',methods=['POST','GET'])
def show_question4():

    this_question=satisfaction_survey.questions[3].question
  



    return render_template('question4.html',this_question=this_question)

@app.route('/result',methods=['POST','GET'])
def show_results():


    survey_responses= responses


    return render_template('result.html',responses=survey_responses)