from itertools import permutations
from transformers import pipeline
from config.app_config import LANGUAGES

for source, target in permutations(LANGUAGES, 2):
    source = 'es'
    target = 'sv'
    text = '¿Cuál es tu nombre?'
    print('SOURCE:', source, 'TARGET:', target)
    try:
        trans_pipeline = pipeline(model=f'Helsinki-NLP/opus-mt-{source}-{target}')
    except OSError as e:
        if 'is not a valid model identifier' in str(e):
            trans_pipeline = pipeline(model=f'Helsinki-NLP/opus-mt-{source}-en')
            text = [t['translation_text'] for t in trans_pipeline(text)]
            trans_pipeline = pipeline(model=f'Helsinki-NLP/opus-mt-en-{target}')
        else:
            raise e
    res = trans_pipeline(text)
    print(res)
