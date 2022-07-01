# SeLogerScrap

SeLogerScrap is a Python script for scrapping data on myselogerpro.com website's.

## Installation

```bash
pip install -r requiremnts.txt
```

## Usage

```python
# Import the class
from src.getcontact import ScrapContacts

# Create the browser (selenium)
browser = ScrapContacts()

# Login method
browser.login()

# Scrap contact to excel
browser.geContact()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)