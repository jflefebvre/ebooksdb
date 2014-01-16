ebooksdb
========

With the time passing by, I had many ebooks in various formats/folders/volumes.
It became difficult to search, so I've coded this small script.
Nothing fancy here, but it's really helpful and time saving !

It provides an easy way to build and search basic informations about your ebooks.
The data stored are the filename, the full path and the creation date.
***
#### Setup

##### Copy e.py in /usr/bin or /opt/local/bin (in my case on OSX)
To make things easier, create a symbolic link e pointing to e.py
```
ln -s /opt/local/bin/e.py /opt/local/bin/e
```

##### Configure the script 
Edit e.py and
- Modify the list of ebook extensions to be retrieved, add or remove as you need
- Set the path to the different folders storing your ebooks
- Set the full path to the ebooks sqlite db to be created

##### The script provides an help 
````
jeff@macbookproi5~/Downloads$ e
usage: e [-h] [-f FIND] [-b]

Allow to build or find ebooks

optional arguments:
  -h, --help            show this help message and exit
  -f FIND, --find FIND  find ebook
  -b, --build           build database
None
```

##### To create/reinitialize the db and rebuild the data :
```
e -b 
```
or 
```
e --build
```

##### Search for ebooks
```
e -f search_string
```

Feel free to send me ideas of improvements or new features.
