from dataclasses import dataclass 
from pathlib import Path

"""
    All the return types of classes will be here
"""

@dataclass(frozen=True) 
class DataIngestionConfig:
      
    root_dir : Path 
    source_URL: str 
    local_data_file : Path 
    unzip_dir : Path 


@dataclass(frozen=True) 
class DataValidationConfig:
    ''' return type --- these variable'''  
    root_dir : Path 
    STATUS_FILE : Path 
    ALL_REQUIRED_FILE : list  

@dataclass(frozen=True) 
class DataTransformationConfig:
    ''' return type --- these variable'''  
    root_dir : Path 
    data_path : Path 
    tokenizer_name : Path  

@dataclass(frozen=True) 
class ModelTrainerConfig:
    ''' return type --- these variable'''  
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int
    

@dataclass(frozen=True) 
class ModelEvaluationConfig:
    ''' return type --- these variable'''  
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path