#this file creates a file with a text
file { '/tmp/school':
ensure  => present,
path    => '/tmp/school',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}

