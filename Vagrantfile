Vagrant.configure("2") do |config|

  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.define "jump" do |jump|
    jump.vm.box = "ssh.box"
    jump.vm.network "forwarded_port", guest: 80, host: 8890, host_ip: "127.0.0.1"
    jump.vm.network "private_network", ip: "192.168.57.12"
  end 

  config.vm.define "http" do |http| 
    http.vm.box = "http.box"
    http.vm.network "forwarded_port", guest: 80, host: 8889, host_ip: "127.0.0.1"
    http.vm.network "private_network", ip: "192.168.57.10"
  end

  config.vm.define "ftp" do |ftp|
    ftp.vm.box = "ftp.box"
    ftp.vm.network "forwarded_port", guest: 80, host: 8888, host_ip: "127.0.0.1"
    ftp.vm.network "private_network", ip: "192.168.57.11"
  end
  
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
  end

end
