import os
from transformers import AutoTokenizer
from datasets import load_from_disk

from text_summarization.logging import logger
from text_summarization.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)


    
    def convert_examples_to_features(self,example_batch):
        logger.info("Creating Input Encodings...")
        input_encodings = self.tokenizer(example_batch['dialogue'] , return_tensors="pt", max_length = 256, truncation = True )
        # input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True ) original

        logger.info("Creating Target Encodings...")
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], return_tensors="pt", max_length = 64, truncation = True )
            
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }


    def convert(self):
        logger.info("Loading Data...")
        dataset_samsum = load_from_disk(self.config.data_ing_dir)
        
        logger.info("Transforming Data...")
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        
        logger.info("Saving Transformed Data...")
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir))

