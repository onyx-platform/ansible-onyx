## ansible-onyx

Ansible playbook for creating a cluster to support Onyx programs. Installs ZooKeeper, Kafka, Riemann, Datomic, Grafana, InfluxDB, and the Onyx Dashboard. Most installs are clustered, and are distributed through Docker.

## Installation

First, install Pip and the packages that Ansible will need:

```text
$ curl -sSL https://bootstrap.pypa.io/get-pip.py | sudo -H python
$ sudo pip install paramiko pyyaml jinja2 httplib2 six docker-py boto
```

Next, install Ansible 2 and source it's environmental variables. You can put this repository anywhere you'd like:

```text
$ git clone --recursive git@github.com:ansible/ansible.git
$ source ansible/hacking/env-setup
$ ansible-playbook --version # Should be ansible 2.x.x
```

Be sure to source `ansible/hacking/env-setup` each time you want to use Ansible in a new shell.

## Vagrant

Ensure your guests have the latest guest additions by installing the vbguests plugin:

```text
$ vagrant plugin install vagrant-vbguest
```

You can run this playbook against a 3 node Vagrant cluster. The Vagrantfile is in this directory. Spin them up with:

```text
$ vagrant up
```

SSH into each machine with:

```text
$ vagrant ssh node1 # or node2/node3
```

Once all the virtual machines come up, you can run the playbook to launch all the services:

```text
$ ansible-playbook --private-key=~/.vagrant.d/insecure_private_key -e remote_user=vagrant -i inventory/vagrant.cfg tasks/boot.yml
```

Next, bring up the Onyx peers with a separate playbook:
```text
$ ansible-playbook -e onyx_mode="prod" -e onyx_id="my-onyx-id" -e n_peers="4" -e dockerhub_password="xxx" -e dockerhub_username="xxx" -e dockerhub_email="xxx" --dockerhub_image="xxxx/yyyy" --private-key=~/.vagrant.d/insecure_private_key -e remote_user=vagrant -i inventory/vagrant.cfg tasks/peers.yml
```

### Developing with Vagrant

Vagrant gives you a cluster of 3 virtual machines to work with. These machines are identical to the images that will be deployed in the cluster. You can test your Onyx program locally on your developer machine while still exercising all of its distributed capabilities. We are able to do this by forwarding the traffic in the Docker containers to the Vagrant virtual machines, and then forwarding the traffic again back to the developer's machine using Vagrant itself. Use the following host/port connections for development with the virtual machines:

- ZooKeeper: `"127.0.0.1:22181,127.0.0.1:22182,127.0.0.1:22183"`
- Kafka: `"127.0.0.1:11401,127.0.0.1:12401,127.0.0.1:13401"`, or discovered dynamically from ZooKeeper
- Riemann: Host `"127.0.0.1"`, port `12201` on TCP or UDP
- Grafana: `http://localhost:12302` in your browser will get you the dashboard. The default credentials are admin/admin
- Datomic: Transactor can be reached at `datomic:free://localhost:4334/<DB-NAME>`
- Onyx Dashboard: Go to `http://localhost:25100` in your browser.

## Services

Here, we describe each of the services that are deployed with Ansible, and anything operationally important that you should know about them. The ZooKeeper, Kafka, Datomic, and InfluxDB containers all volume mount their data onto the host. This means that if you lose your container and restart it, the data survives. The Ansible playbooks that intentionally restart these services from scratch also blow away the host data directories to return you to a totally clean, initial state.

### ZooKeeper

ZooKeeper is deployed in clustered mode. Each instance runs inside a Docker container. Verify that it's working by SSHing into each machine that it was deployed to and run:

```text
$ docker logs zookeeper
```

You should see ZooKeeper log output if everything went okay. If you see repeated "connection refused" messages, something is wrong with the networking. When ZooKeeper is healthy, it produces relatively few log messages.

### Kafka

Kafka is deployed in clustered mode. Each instance runs inside a Docker container. Verify that it's working by SSHing into each machine that it was deployed to and run:

```text
$ docker logs kafka
```

You should see Kafka's typical log messages. If you see "connection refused" messages, the brokers are likely having trouble connecting to ZooKeeper, or the brokers on the other machines.

### Datomic

A Datomic transactor is deployed onto one machine. See it's logs with:

```text
$ docker logs datomic
```

### Riemann

Riemann is deployed onto one machine. See it's logs by running:

```text
$ docker logs riemann
```

### InfluxDB

InfluxDB is deployed onto one machine. You can see that InfluxDB's activity via its logs:

```text
$ docker logs influx
```

### Grafana

Grafana is deployed onto one machine. See it's logs with:

```text
$ docker logs grafana
```

### Onyx Dashboard

Onyx Dashboard is deployed onto one machine. See it's logs with:

```text
$ docker logs onyx-dashboard
```

### Acknowledgements

Many thanks to Flybot Pte. Ltd., for allowing this work to be open sourced and contributed back too the community.

### License

Copyright © 2015 Distributed Masonry LLC

Distributed under the Eclipse Public License, the same as Clojure.
