# falcon-crossorigin

A simple [Falcon](https://github.com/falconry/falcon) module for Cross-Origin Resource Sharing (CORS).


## Install
```shell script
pip install falcon-crossorigin
```

## Usage
```python
import falcon
from falcon_crossorigin import CrossOrigin

cross_origin = CrossOrigin(allow_origins="https://app.example.com")

api = falcon.API(middleware=[cross_origin])
```
