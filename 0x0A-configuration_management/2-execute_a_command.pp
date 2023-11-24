# Kill a specific process

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
