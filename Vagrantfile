# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

box_url = "https://github.com/kraksoft/vagrant-box-ubuntu/releases/download/14.04/ubuntu-14.04-amd64.box"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.ssh.insert_key = false

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
  end

  config.vm.define "node1" do |node|
    node.vm.box = "ubuntu14"
    node.vm.box_url = box_url
    node.vm.network "private_network", ip: "192.168.50.4"

    # Kafka broker
    node.vm.network "forwarded_port", guest: 9092, host: 11401, protocol: 'tcp'

    # Datomic
    node.vm.network "forwarded_port", guest: 4334, host: 4334, protocol: 'tcp'
    node.vm.network "forwarded_port", guest: 4335, host: 4335, protocol: 'tcp'
    node.vm.network "forwarded_port", guest: 4336, host: 4336, protocol: 'tcp'

    # Zookeeper
    node.vm.network "forwarded_port", guest: 2181, host: 22181, protocol: 'tcp'
  end

  config.vm.define "node2" do |node|
    node.vm.box = "ubuntu14"
    node.vm.box_url = box_url
    node.vm.network "private_network", ip: "192.168.50.5"

    # Riemann event receivers
    node.vm.network "forwarded_port", guest: 5555, host: 12201, protocol: 'tcp'
    node.vm.network "forwarded_port", guest: 5555, host: 12201, protocol: 'udp'
    node.vm.network "forwarded_port", guest: 5556, host: 12203, protocol: 'tcp'

    # Grafana
    node.vm.network "forwarded_port", guest: 3000, host: 12302, protocol: 'tcp'

    # Kafka broker
    node.vm.network "forwarded_port", guest: 9092, host: 12401, protocol: 'tcp'

    # Zookeeper
    node.vm.network "forwarded_port", guest: 2181, host: 22182, protocol: 'tcp'
  end

  config.vm.define "node3" do |node|
    node.vm.box = "ubuntu14"
    node.vm.box_url = box_url
    node.vm.network "private_network", ip: "192.168.50.6"

    # Kafka broker
    node.vm.network "forwarded_port", guest: 9092, host: 13401, protocol: 'tcp'

    # Zookeeper
    node.vm.network "forwarded_port", guest: 2181, host: 22183, protocol: 'tcp'

    # Onyx Dashboard
    node.vm.network "forwarded_port", guest: 8085, host: 25100, protocol: 'tcp'
  end
end
