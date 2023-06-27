#setting SSH configuration file to connect to server without pw using puppet

file { '/etc/ssh/ssh_config':
  content => "
    Host *
      PasswordAuthentication no
      IdentityFile ~/.ssh/school
  "
}
