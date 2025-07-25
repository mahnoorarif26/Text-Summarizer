from flask import Flask, render_template, request
from summarizer import summarize_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    summary = None
    
    if request.method == 'POST':
        text = request.form.get('text', '')
        summary_type = request.form.get('summary_type', 'descriptive')
        
        # Check word count
        word_count = len(text.strip().split())
        if word_count < 50:
            error = f"❗ Please enter at least 50 words. You entered {word_count}."
        else:
            summary = summarize_text(text, summary_type)
    
    return render_template('index.html', error=error, summary=summary)
if __name__ == '__main__':
    app.run(debug=True)
