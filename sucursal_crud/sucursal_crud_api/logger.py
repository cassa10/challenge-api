import logging
import inspect

logger = logging.getLogger(__name__)

# normal arguments are ignored, used keyword arguments for logging
# kwargs can be n params
def logParamInfo(source, **kwargs):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = module.__file__
    params = []
    for key, value in kwargs.items():
        params.append(f'{key}: {value}')
    
    logger.info(f'file: {filename} | ({source.__class__.__name__}.{inspect.stack()[1][3]}) - Parameters: {params}')