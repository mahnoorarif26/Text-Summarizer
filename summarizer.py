from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, summary_type="descriptive"):
    words = text.strip().split()
    word_count = len(words)
    if word_count > 500:
        text = ' '.join(words[:500])
        word_count = 500

    if summary_type == "concise":
        min_len = max(20, int(word_count * 0.2))  
        max_len = max(30, int(word_count * 0.3))  
    elif summary_type == "descriptive":
        min_len = max(50, int(word_count * 0.4))  
        max_len = max(80, int(word_count * 0.5))  
    else:
        return "❗ Invalid summary type selected."
    try:
        result = summarizer(text, min_length=min_len, max_length=max_len, do_sample=False)
        return result[0]['summary_text']
    except Exception as e:
        return f"❗ An error occurred during summarization: {str(e)}"