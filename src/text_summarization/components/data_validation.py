import os
from text_summarization.config.configuration import ConfigurationManager
from text_summarization.entity import DataValidationConfig
from text_summarization.logging import logger

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = None
            dataset_path = os.path.join(self.config.data_ing_dir, "samsum_dataset")
            all_present_files = os.listdir(dataset_path)

            # print(all_present_files)

            for i, file in enumerate(self.config.ALL_REQUIRED_FILES):

                if i == 0:
                    status_file = open(self.config.STATUS_FILE, 'w')
                else:
                    status_file = open(self.config.STATUS_FILE, 'a')

                # file = os.path.join(dataset_path, file)
                
                if file not in all_present_files:
                    validation_status = False
                else:
                    validation_status = True
                
                status_file.write(f"{i+1}.) Validation status of file {file}: {validation_status}.\n")

            return validation_status

        except Exception as e:
            raise e