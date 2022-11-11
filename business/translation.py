from functools import lru_cache

from transformers import pipeline
from utils.logger_utils import stream_logger

logger = stream_logger(__name__)

def translate(source, target, text):
    try:
        trans_pipeline = get_pipeline(source, target)
    except OSError as e:
        if 'is not a valid model identifier' in str(e):
            logger.debug('is not a valid model identifier')
            trans_pipeline = get_pipeline(source, 'en')
            text = [t['translation_text'] for t in trans_pipeline(text)]
            trans_pipeline = get_pipeline('en', target)
        else:
            raise e
    return trans_pipeline(text)

@lru_cache(2)
def get_pipeline(source,target):
    return pipeline(model=f'Helsinki-NLP/opus-mt-{source}-{target}')