### TEXT SUMMARIZATION USING THE HUGGING FACE TRANSFORMERS LIBRARY

#### Problem Statement
Text summarization is the process of condensing extensive textual content into concise and coherent summaries while retaining critical information and context.

With over 2.5 quintillion bytes of data generated daily, manual summarization is impractical, creating a growing demand for automated solutions.

This project aims to develop a text summarization system leveraging advanced Natural Language Processing (NLP) techniques such as attention mechanisms and transformers to generate meaningful and accurate summaries of long conversations in dialogue format.

Such systems find applications in diverse fields, including news aggregation, where they enable users to digest headlines quickly, research paper summarization, facilitating academics to grasp key findings, and customer feedback analysis, improving decision-making by summarizing large volumes of reviews.

By saving time and enhancing productivity, automated summarization can significantly impact how information is processed and consumed.


[Data Source](https://github.com/entbappy/Branching-tutorial/raw/master/summarizer-data.zip)

The dataset is in the form of .arrow file. It includes various conversations in a dialogue format and their respective short summary.<br>
An example data point looks like this:-

**Dialogue:**<br>
Eric: MACHINE!<br>
Rob: That's so gr8!<br>
Eric: I know! And shows how Americans see Russian ;)<br>
Rob: And it's really funny!<br>
Eric: I know! I especially like the train part!<br>
Rob: Hahaha! No one talks to the machine like that!<br>
Eric: Is this his only stand-up?<br>
Rob: Idk. I'll check.<br>
Eric: Sure.<br>
Rob: Turns out no! There are some of his stand-ups on youtube.<br>
Eric: Gr8! I'll watch them now!<br>
Rob: Me too!<br>
Eric: MACHINE!<br>
Rob: MACHINE!<br>
Eric: TTYL?<br>
Rob: Sure :)
<br><br>
**Summary:**<br>
Eric and Rob are going to watch a stand-up on youtube.


#### Dependencies
**Tech Stack** - PEGASUS Transformer Library, Tokenization, FastAPI, Transfer Learning, AWS.


#### Project Workflow
* Developed an **end-to-end project** for text summarization of long conversations in dialogue format, utilizing the PEGASUS library.
* Experimented with **advanced Transformer models** like **cnn-daily-mail** and **multi-news**, fine-tuning hyperparameters to enhance system performance.
* Organized configurations in `config.yaml` and `params.yaml` files, detailing settings for the entire project pipeline.
* **Entity objects** were created to load relevant configuration sections for modular and reusable code design.
* A **Configuration Manager** in the `src.config` module handles entity objects, ensuring configurations are accessible across the project.
* Defined **components** for key functionalities, including data ingestion, data transformation, model training, metrics tracking, and model evaluation.
* Model evaluation is conducted using **unigram ROUGE** scores, a widely recognized and powerful metric for assessing the performance of text summarization models.
* Built **pipeline** objects to manage configuration creation and execute the respective components as part of the project pipeline.
* The `main.py` file integrates and executes the entire pipeline from start to finish.
* Designed an intuitive UI using **FastAPI** for providing an interactive experience to the users to utilize the app.


#### Usage
* Access the AWS link.
* Upload the X-Ray image and hit the predict button.
* Acquire the prediction.


#### Results
The model was able to process and parse the uploaded text input and generate the summarised text with a **rouge1 score of 0.49** and a **rougeL score of 0.46**.


#### Final Notes
This is a great project to learn:-
* Text processing and Tokenization.
* Designing and building a scalable industry grade project with a modular project structure.
* Transformer architectures for BERT model and PEGASUS library.
* How to use the Colab and the Kaggle environments for training such computationally expensive models.
* The working knowledge of the Tensorflow package (model creation, callbacks designing, ) and the Hugging Face library.
* Understanding the ROGUE Scores for fine tuning the model.
* AWS and Docker for deployment of the project.

