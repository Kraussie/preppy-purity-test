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

# **TO DO**
- Download SSL certifications
- Add routing for new schools
- Add logging [MODULE DOCUMENTATION](https://docs.python.org/2.6/library/logging.html)
- Create stats/results page