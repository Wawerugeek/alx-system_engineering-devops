#puppet script to install nginix
exec { '/usr/bin/env apt-get -y update':}
->package {'nginx':
ensure => installed,
}

->file {'/var/www/html/index.html':
content => 'Hello world!\n',
}

->file_line {'add protocol':
ensure => present,
path   => '/etc/nginx/sites-available/default',
after  => 'listen 80 default_server;',
line   => "\tadd_header X-Served-By ${hostname};",
}

->service { 'nginx':
ensure     => running,
}i
