from transformers import AutoTokenizer
from transformers import pipeline

from text_summarization.config.configuration import ConfigurationManager


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()


    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        sum_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        pipe = pipeline("summarization", model = self.config.model_path, tokenizer = tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **sum_kwargs)[0]["summary_text"]
        print("\nModel Generated Summary:")
        print(output)

        return output