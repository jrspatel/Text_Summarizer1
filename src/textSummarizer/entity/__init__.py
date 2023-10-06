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
    