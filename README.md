Habitica checker
================

What is this
------------

Do you sometimes forget to do your dailies or check them in Habitica web app? With this script, you can automatically check whether you did everything. If you forgot something, the script will print number of incomplete tasks and exit with error code 1. You should hook this script to run just before the end of the day (use cron or a sensor mounted to your bed :)).

Usage
-----

Create file ~/.habitica containing json object:
```
{
	"uuid" : "YOUR-UUID",
	"token" : "YOUR-API-TOKEN"
}
```

Then just run the script. Nothing else needed. If you don't have your home directory encrypted, you should put the file in encrypted filesystem (encfs should be enough) and symlink it to ~/.habitica.

Author
------

Martin Habovštiak <martin.habovstiak@gmail.com>

Released under the terms of MIT License.
