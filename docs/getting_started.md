#Installation

##Basic Installation
Installation is fairly simple. Start by cloning the github repo then install using
the setup.py file provided

```
git clone https://github.com/chelnak/vRAAPIClient.git
cd vRAAPIClient
python setup.py install
```

##Installation with virtualenv
Sometimes its nice to know that your python projects are isolated. This is why I like to
use virtualenv.

See [here](https://virtualenv.pypa.io/en/latest/) for the latest virtualenv docs

```
pip install virtualenv
mkdir vRAAPIClient-Scripts
cd vRAAPIClient-Scripts
virtualenv venv
source venv/bin/activate
git clone https://github.com/chelnak/vRAAPIClient.git
cd vRAAPIClient
python setup.py install
```

You can then run pip freeze to see what has been installed


#Basic Usage
