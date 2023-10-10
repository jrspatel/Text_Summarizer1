from textSummarizer.entity import ModelTrainerConfig
import torch
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import os

class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig) -> ModelTrainerConfig:
        self.config = config 

    def train(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu' 
        # calling the tokenizer
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt) 
        # loading the model
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        # sending the bath data 
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        # loading the data from data_transformation
        dataset_samsum_pt = load_from_disk(self.config.data_path) 

        # setting trainign argumetns
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
            per_device_train_batch_size=2, per_device_eval_batch_size=2,
            weight_decay=0.01, logging_steps=10,
            evaluation_strategy='steps', eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16
        
        ) 
        trainer = Trainer(model=model_pegasus, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["test"], 
                  eval_dataset=dataset_samsum_pt["validation"])
        
        trainer.train()

        #saving the model 
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,'pegasus-samsum-model'))
        # save the tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,'tokenizer'))