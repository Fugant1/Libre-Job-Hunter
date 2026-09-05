import logging                                                                                                                                                            
import os                                                                                                                                                                 
import sys                                                                                                                                                                 
from typing import Optional                                                                                                                                               
from pythonjsonlogger.json import JsonFormatter                                                                                                                           
                                                                                                                                                                              
                                                                                                                                                                              
def setup_logging(default_level: str = "INFO") -> None:                                                                                                                       
        log_level = os.getenv("LOG_LEVEL", default_level).upper()                                                                                                             
                                                                                                                                                                            
        formatter = JsonFormatter(                                                                                                                                            
            fmt="%(asctime)s %(levelname)s %(name)s %(funcName)s %(message)s",                                                                                                
            rename_fields={                                                                                                                                                   
                "asctime": "timestamp",                                                                                                                                       
                "levelname": "level",                                                                                                                                         
                "funcName": "caller",                                                                                                                                         
            },                                                                                                                                                                
            datefmt="%Y-%m-%dT%H:%M:%S%z",                                                                                                                                    
        )                                                                                                                                                                     
                                                                                                                                                                              
        handler = logging.StreamHandler(sys.stdout)                                                                                                                           
        handler.setFormatter(formatter)                                                                                                                                       
                                                                                                                                                                              
        root_logger = logging.getLogger()                                                                                                                                     
        root_logger.setLevel(log_level)                                                                                                                                       
                                                                                                                                                                          
        if not root_logger.handlers:                                                                                                                                          
            root_logger.addHandler(handler)                                                                                                                                   
        else:                                                                                                                                                                 
            root_logger.handlers = [handler]                                                                                                                                  
                                                                                                                                                                             
        logging.getLogger("httpx").setLevel(os.getenv("HTTPX_LOG_LEVEL", "WARNING"))                                                                                          
        logging.getLogger("urllib3").setLevel(os.getenv("URLLIB3_LOG_LEVEL", "WARNING"))                                                                                      
                                                                                                                                                                              
                                                                                                                                                                              
def get_logger(name: Optional[str] = None) -> logging.Logger:                                                                                                                  
        if not logging.getLogger().handlers:                                                                                                                                  
            setup_logging()                                                                                                                                                   
        return logging.getLogger(name or __name__)  