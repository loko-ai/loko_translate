from loko_extensions.model.components import Component, save_extensions, Input, AsyncSelect

source = AsyncSelect(name='source',
                     label='Source Language',
                     url='http://localhost:9999/routes/loko_translate/languages',
                     required=True)
target = AsyncSelect(name='target',
                     label='Target Language',
                     url='http://localhost:9999/routes/loko_translate/languages',
                     required=True)
input = Input(id='input', service='translate', to='output')
translator = Component(name='Translate', args=[source, target], inputs=[input], icon='RiTranslate', configured=False)
save_extensions([translator])