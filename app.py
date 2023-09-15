from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def question_form():
    prompts = story.prompts

    return render_template('questions.html', prompts=prompts)

@app.route('/story')
def story_page():
    text = story.generate(request.args)

    return render_template('story.html', text=text)