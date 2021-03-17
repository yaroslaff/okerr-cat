# okerr-cat

## Install
~~~
# apt install uwsgi uwsgi-plugin-python3
# python3 -m venv /opt/venv/okerr-cat
# cd /opt/venv/okerr-cat
# . bin/activate
(okerr-cat)# mkdir run
(okerr-cat)# chown www-data:www-data run
(okerr-cat)# pip3 install /tmp/okerr_cat...whl
(okerr-cat)# cp contrib/okerr-cat.default /etc/default/okerr-cat
(okerr-cat)# ln -s /opt/venv/okerr-cat/contrib/okerr-cat.service /etc/systemd/system
(okerr-cat)# cp contrib/okerr-cat.nginx /etc/nginx/sites-available/okerr-cat
(okerr-cat)# ln -s /etc/nginx/sites-available/okerr-cat /etc/nginx/sites-enabled/
(okerr-cat)#
(okerr-cat)#
(okerr-cat)#
(okerr-cat)#
(okerr-cat)#
(okerr-cat)#
(okerr-cat)#

~~~

## Configuration
Cat uses environment variables `ROLE`, `MYIP`, `FAILSTART`

## Development start
As any other simple Flask application.
~~~shell
$ export FLASK_APP=cat.py
$ export FLASK_ENV=development
$ flask run
$ flask run --host=0.0.0.0
~~~

# Other okerr resources
- [Okerr main website](https://okerr.com/)
- [Okerr-server source code repository](https://github.com/yaroslaff/okerr-dev/) 
- [Okerr client (okerrupdate) repositoty](https://github.com/yaroslaff/okerrupdate) and [okerrupdate documentation](https://okerrupdate.readthedocs.io/)
- [Okerrbench network server benchmark](https://github.com/yaroslaff/okerrbench)
- [Okerr custom status page](https://github.com/yaroslaff/okerr-status)
- [Okerr JS-powered static status page](https://github.com/yaroslaff/okerrstatusjs)
- [Okerr network sensor](https://github.com/yaroslaff/sensor)
- [Demo ISP](https://github.com/yaroslaff/demoisp) prototype client for ISP/hoster/webstudio providing paid okerr access to customers
- [Okerr cat](https://github.com/yaroslaff/okerr-cat) simple [Flask](https://flask.palletsprojects.com/) application to simulate frequent website outages. Runs on [cat.okerr.com](https://cat.okerr.com/).
