# **SERVER COMMANDS/NOTES**
View General Logs:
`tail -f /var/log/app.log`

## SUPERVISOR
Edit Config:
`sudo vim /etc/supervisor/conf.d/hello_world.conf`

Re-read Config:
`sudo supervisorctl reread`

Start/Stop/Restart:
`sudo service supervisor start/stop/restart`

Status:
`sudo supervisorctl status`

View Supervisor Output Log:
`tail -f /var/log/hello_world/hello_world.out.log`
## NGINX

Edit Config:
`sudo vim /etc/nginx/conf.d/virtual.conf`

Test Config:
`sudo nginx -t`

Start/Stop/Restart:
`sudo service nginx start/stop/restart`

View NGINX Access Log:
`tail -f /var/log/nginx/access.log`


# **TIMELINE**
04/20/2020:
- Web Server setup on Google Cloud Platform (GCP) Compute Engine [[TUTORIAL]](https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18)
- SSL Certificate created

04/21/2020:
- SSL Certificate installed [[TUTORIAL]](https://www.digicert.com/kb/csr-ssl-installation/nginx-openssl.htm#ssl_certificate_install) and [[TUTORIAL]](https://serversforhackers.com/c/testing-and-debugging-ssl-certificates)
- http --> https re-reroute setup in nginx config [[TUTORIAL]](https://linuxize.com/post/redirect-http-to-https-in-nginx/)

04/22/2020:
- Flask Logging Setup (found a "/var/log/app.log"), very barebones currently
- Fixed Geolocation API request, wasn't a secured connection and was blocked by Chrome browser
- 'Index.db' file works and saves properly
- Downloaded SSL certificates, saved to GDrive
- Created JS function that runs on page load, will collect IP info w/out needing a test to be submitted
- changed index.html favicon to vineyard vines logo
- Began work on stats.html page
- app.py accepts POST and GET requests now
- added randomize button to test.html
- Began work on Python script to spam data

04/23/2020:
- Random Sample Data (python script) created and working

# **TO DO**
- Create stats/results page 
    - (https://dataset.readthedocs.io/en/latest/)
    - (https://inloop.github.io/sqlite-viewer/)
- Add routing for new schools + colors
- Reformat test.html
- Remove logging to client console