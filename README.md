**Author:** [Behrouz Safari](https://behrouzz.github.io/)<br/>
**License:** [MIT](https://opensource.org/licenses/MIT)<br/>

# sinsta
*Simple Instagram API*


## Installation

Install the latest version of *sinsta* from [PyPI](https://pypi.org/project/sinsta/):

    pip install sinsta

Requirements are *requests* and *pandas*.


## Quick start

```python
from sinsta import Instagram

ins = Instagram(USERNAME, PASSWORD)
ins.login()
ins.save_friends(['friend1', 'friend2', 'friend3', 'friend4', 'friend5'])
```
