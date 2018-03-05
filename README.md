# PySSH
JSON parser for SSH connection in Python


## Table of contents  
#### [JSON](#json)   
#### [OrderedDict](#ordereddict)  

## JSON

The main purpose of this application is to write and read JSON files.
jwriter.json allows one to create a json format file and store ssh login information for a user.

In the near future, a jreader.json file will allow one to remotely connect to a server using another config file.

## OrderedDict

```
from collections import OrderedDict
```

This will be used to create a dictionnary to be able to handle ordering within the JSON files.
