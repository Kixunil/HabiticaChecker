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

How to make gnome/mate-power-manager hook
-----------------------------------------

If you want to hook this script to gnome-power-manager or mate-power-manager, you can follow this howto:

1. Run `apt-get source gnome-power manager` or `apt-get source mate-power manager`
2. Change into downloaded directory
3. Open src/gpm-manager.c in your favourite editor
4. Find definition of function `gpm_manager_action_suspend` and put this code in it before anything else:
```
int hook = WEXITSTATUS(system("~/.gpmhook"));
if(hook > 0 && hook < 127)
	return FALSE;
```
5. Save and exit
6. Run `dpkg-source --commit` and follow the instructions
7. Run `dpkg-buildpackage`. If it fails because of missing packages, install them using `sudo apt-get install` and re-run it.
8. Change to parent directory and run `sudo dpkg -i gnome-power-manager_*.deb` or `sudo dpkg -i mate-power-manager_*.deb`
9. Kill power manager with `killall gnome-power-manager` or `killall mate-power-manager`
10. Rerun power manager
11. Copy `check_dailies.py` to `~/.gpmhook`

Author
------

Martin Habovštiak <martin.habovstiak@gmail.com>

Released under the terms of MIT License.
