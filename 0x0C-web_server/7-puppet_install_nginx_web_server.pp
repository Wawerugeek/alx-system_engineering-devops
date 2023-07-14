#this puppet script installs nginx

package {'nginx:
ensure => present,
name => 'nginx',
}

service {'nginx':
ensure => running,
enable => true,
hasrestart => true,
require => package['nginx'],
subscribe => file_line["add redirect"],
}

file {'/var/www/html/index.html':
ensure => present,
path => '/var/www/html/index.html',
content => Hello World!
}

file { '/etc/nginx/sites-available/default':
ensure => present,
content => '
server {
listen 80 default_server;
listen [::]:80 default_server;

server_name _;

location / {
root /var/www/html;
index index.html;
}

location /redirect_me {
return 301 http://muiruri.tech/redirect_me.html;
}
}'
,
require => package['nginx'],
notify => service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
ensure => 'link'
target => '/etc/nginx/sites-available/default',
require => file['/etc/nginx/sites-available/default'],
notify => service['nginx']
}
