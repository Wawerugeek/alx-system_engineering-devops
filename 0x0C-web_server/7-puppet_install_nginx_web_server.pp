#this puppet script installs nginx
package {'nginx':
ensure => present,
name   => 'nginx',
}

service { 'nginx':
ensure     => running,
enable     => true,
hasrestart => true,
require    => Package['nginx'],
subscribe  => File_line["add redirect"],
}

file {'/var/www/html/index.html':
ensure  =>  present,
path    => '/var/www/html/index.html',
content => 'Holberton School for the win yeah!\n',
}

file_line {'add redirect':
ensure  => present,
path    => '/etc/nginx/sites-available/default',
replace => true,
line    => '	rewrite /redirect_me/ http://muiruri.tech permanent;',
match   => '# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000',
}
