import os
from box.exceptions import BoxValueError
import yaml 
from textSummarizer.logging import logger 
# different type of calling the dictionarie keys
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any

# the decorator makes sure to handle any input for,at errrors
# e.g. if its int , it makes sure you pass integer variable
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ reads the yaml file and returns 
        the content present in it
    Args:
        path_to_yaml (str) : windows path like input 

    Raises:
        valueError: if yaml file is empty 
        e: empty file 

    Returns:
        ConfigBox: cnfigBox type 
    
    # configBox converts the dictinary type to list 
    i.e we can access the dictionary elements in list format 

    """ 
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file) 
            print(" in common file")
            print(content)
            logger.info(f'yaml file: {path_to_yaml} successfully loaded') 
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty") 
    except Exception as e:
        raise e 


@ensure_annotations 
def create_directories(path_to_directories: list, verbose=True):
    """ 
        creates list of directories     
        Args: 
            path_to_directories (list): a list input which is a path to create directories
    """ 

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True) 
        if verbose:
            logger.info(f'created directory at: {path}') 

@ensure_annotations
def get_size(path: Path) -> str:
    """ gets size in KB 
    Args:
        path (path): windows path to a file
        
    Returns:
            str: size in kb
            
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'