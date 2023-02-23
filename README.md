<html><p><a href="https://loko-ai.com/" target="_blank" rel="noopener"> <img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/30443495/196493267-c328669c-10af-4670-bbfa-e3029e7fb874.png" width="8%" align="left" /> </a></p>
<h1>Loko Translate</h1><br></html>

**Loko Translate** extension is built on top Transformers translation models.

You can set your **source** and **target** language:

- English (en)
- Italian (it)
- Spanish (es)
- French (fr)
- German (de)
- Vietnamese (vi)
- Arabic (ar)
- Swedish (sv)
- Chinese (zh)

<p align="center"><img src="https://user-images.githubusercontent.com/30443495/220889681-28fdc279-37ba-4e2b-8815-297069b76a81.png" width="80%" /></p>

The first time you run your flow, the extension automatically downloads the requested model. Once the model is loaded in
memory, output results will be faster. 

**Example**:

Input: 
```
我叫萨拉，我住在伦敦。
```

Output:
```
{
    "translation_text": "Mi chiamo Sarah, vivo a Londra."
}
```


## Configuration

In the file *config.json* you can choose where to mount your huggingface volume.
All the downloaded models will be saved in this directory:

```
{
  "main": {
    "volumes": [
      "/var/opt/loko/huggingface:/root/.cache/huggingface"
    ]
  }
}
```