import traceback

import sanic
from config.app_config import LANGUAGES
from sanic import Sanic, Blueprint
from sanic.exceptions import NotFound
from sanic_openapi import swagger_blueprint

from transformers import pipeline

from loko_extensions.business.decorators import extract_value_args
from utils.logger_utils import stream_logger

logger = stream_logger(__name__)

def get_app(name):
    app = Sanic(name)
    swagger_blueprint.url_prefix = "/api"
    app.blueprint(swagger_blueprint)
    return app

name = "loko_translate"
app = get_app(name)
bp = Blueprint("default", url_prefix=f"/")
app.config["API_TITLE"] = name

@bp.get('/languages')
async def lang(request):
    return sanic.json(LANGUAGES)


@bp.post('/translate')
@extract_value_args()
async def f(value, args):
    source = args.get('source')
    target = args.get('target')
    logger.debug(f'SOURCE: {source} - TARGET: {target}')

    try:
        trans_pipeline = pipeline(model=f'Helsinki-NLP/opus-mt-{source}-{target}')
    except OSError as e:
        if 'is not a valid model identifier' in str(e):
            logger.debug('is not a valid model identifier')
            trans_pipeline = pipeline(model=f'Helsinki-NLP/opus-mt-{source}-en')
            value = [t['translation_text'] for t in trans_pipeline(value)]
            trans_pipeline = pipeline(model=f'Helsinki-NLP/opus-mt-en-{target}')
        else:
            raise e

    return sanic.json(trans_pipeline(value))

@app.exception(Exception)
async def manage_exception(request, exception):
    e = dict(error=str(exception))
    if isinstance(exception, NotFound):
        return sanic.json(e, status=404)
    logger.error('TracebackERROR: \n' + traceback.format_exc() + '\n\n')
    status_code = exception.status_code or 500
    return sanic.json(e, status=status_code)

app.blueprint(bp)

app.run("0.0.0.0", port=8080, auto_reload=True)