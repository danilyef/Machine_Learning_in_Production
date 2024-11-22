import gradio as gr
from utils import Model


model = Model(tokenizer_name="distilbert-base-uncased-finetuned-sst-2-english", model_name="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    # Get the prediction
    label = model.predict(text)
    probabilities = model.predict_proba(text)
    
    # Get probability score for predicted class
    score = probabilities[1] if label == "POSITIVE" else probabilities[0]
    score = f"{score:.3f}"

    # Add color to label
    colored_label = f"<span style='color: green'>{label}</span>" if label == "POSITIVE" else f"<span style='color: red'>{label}</span>"

    return colored_label, score

# Create the Gradio interface
demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(label="Enter text to analyze:", value="I love this app!"),
    outputs=[
        gr.HTML(label="Sentiment"),
        gr.Textbox(label="Confidence"),
    ],
    title="Sentiment Analysis with DistilBERT",
    description="Analyze the sentiment of your text using DistilBERT"
)

if __name__ == "__main__":
    demo.launch()