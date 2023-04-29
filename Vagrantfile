Vagrant.configure("2") do |config|

  config.vm.synced_folder '.', '/vagrant', disabled: true

  config.vm.define "jump" do |jump|
    jump.vm.box = "jump.box"
    jump.vm.network "forwarded_port", guest: 22, host: 2224
    jump.vm.network "private_network", ip: "172.26.176.1"
  end 

  config.vm.define "http" do |http| 
    http.vm.box = "http.box"
    http.vm.network "forwarded_port", guest: 22, host: 2223
    http.vm.network "private_network", ip: "172.26.176.1"
  end

  config.vm.define "ftp" do |ftp|
    ftp.vm.box = "ftp.box"
    ftp.vm.network "private_network", ip: "172.26.176.1"
    ftp.vm.network "forwarded_port", guest: 22, host: 2221
  end
  
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"  
  end

end
