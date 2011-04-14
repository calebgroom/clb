==================================================================
 Command-line tool for Rackspace Load Balancers
==================================================================

:Homepage:  https://github.com/calebgroom/clb
:Credits:   Copyright 2011 Caleb Groom <caleb@calebgroom.com>
:Licence:   BSD

Install
====

To install clb from source::

  $ git clone git://github.com/calebgroom/clb.git
  $ cd clb
  $ sudo python setup.py install

History
=====

clb is based on the shell.py script from jacobian's python-cloudservers project
(https://github.com/jacobian/python-cloudservers) and uses the python-cloudlb
library (https://github.com/rackspace/python-cloudlb).

Credentials
=====

Rackspace Cloud credentials can be specified on the command line or stored in your user's environment.  Your username, password, and region are required.  These two sets of commands are equivalent::

 $ export CLOUD_LOADBALANCERS_USERNAME='myusername'
 $ export CLOUD_LOADBALANCERS_API_KEY='abcdefg'
 $ export CLOUD_LOADBALANCERS_REGION='chicago'
 $ clb list

 $ clb --username myusername --apikey abcdefg --region chicago list

The following examples assume the credentials are stored in your user's environment. 

Output
=====

Output is formatted for visual display::

  $ clb list
  +----------------+------+------+----------+-------------+-------+--------------------+
  |      Name      |  ID  | Port | Protocol |  Algorithm  | Nodes |        IPs         |
  +----------------+------+------+----------+-------------+-------+--------------------+
  | lb-with-nodes2 | 1713 | 80   | HTTP     | ROUND_ROBIN | 3     | IPV4/10.183.252.96 |
  | lb-node-csv    | 7362 | 80   | HTTP     | RANDOM      | 2     | IPV4/10.183.253.16 |
  | publiclb       | 8738 | 21   | HTTP     | ROUND_ROBIN | 2     | IPV4/50.56.4.210   |
  +----------------+------+------+----------+-------------+-------+--------------------+

The optional argument for batch mode will create parsable output.  The field delimiter can be overwritten as well::

  $ clb --batch list
  Name,ID,Port,Protocol,Algorithm,Nodes,IPs
  lb-with-nodes2,1713,80,HTTP,ROUND_ROBIN,3,IPV4/10.183.252.96,
  lb-node-csv,7362,80,HTTP,RANDOM,2,IPV4/10.183.253.16,
  publiclb,8738,21,HTTP,ROUND_ROBIN,2,IPV4/50.56.4.210,

The field delimiter can be overwritten as well::

  $ clb --batch --delimiter='|' list
  Name|ID|Port|Protocol|Algorithm|Nodes|IPs
  lb-with-nodes2|1713|80|HTTP|ROUND_ROBIN|3|IPV4/10.183.252.96|
  lb-node-csv|7362|80|HTTP|RANDOM|2|IPV4/10.183.253.16|
  publiclb|8738|21|HTTP|ROUND_ROBIN|2|IPV4/50.56.4.210|

Usage
=====

Create a load balancer with two nodes behind a public IP::

  $ clb create mylb 80 HTTP '10.1.1.1:80,10.1.1.2:80' public

Create a load balancer with three nodes behind an internal Rackspace ServiceNet IP::

  $ clb create mylb 80 HTTP '10.1.1.1:80,10.1.1.2:80,10.1.1.3:80' servicenet

Create a load balancer with two nodes by sharing a VIP (id 1234) from an existing load balancer::

  $ clb create mylb 80 HTTP '10.1.1.1:80,10.1.1.2:80,10.1.1.3:80' 1234

List load balancers::

  $ clb list
  +----------------+------+------+----------+-------------+-------+--------------------+
  |      Name      |  ID  | Port | Protocol |  Algorithm  | Nodes |        IPs         |
  +----------------+------+------+----------+-------------+-------+--------------------+
  | lb-with-nodes2 | 1713 | 80   | HTTP     | ROUND_ROBIN | 3     | IPV4/10.183.252.96 |
  | lb-node-csv    | 7362 | 80   | HTTP     | RANDOM      | 2     | IPV4/10.183.253.16 |
  | lb-share       | 7364 | 81   | HTTP     | RANDOM      | 5     | IPV4/10.183.253.16 |
  +----------------+------+------+----------+-------------+-------+--------------------+

List deleted load balancers::

  $ clb list-deleted
  +------------------------------+------+
  |             Name             |  ID  |
  +------------------------------+------+
  | lb01                         | 1404 |
  | lb02                         | 1408 |
  +------------------------------+------+ 

List load balancer details::

  $ clb show mylb
  +---------------------+----------------------------------+
  |        Field        |              Value               |
  +---------------------+----------------------------------+
  | Name                | mylb                             |
  | ID                  | 7364                             |
  | Status              | ACTIVE                           |
  | Port                | 81                               |
  | Protocol            | HTTP                             |
  | Algorithm           | RANDOM                           |
  | VIP 663             | 10.183.253.16 (SERVICENET)       |
  | Node 0              | 10.5.5.5:444 / ENABLED / ONLINE  |
  | Node 1              | 10.7.7.7:80 / ENABLED / ONLINE   |
  | Node 2              | 10.8.8.8:8080 / ENABLED / ONLINE |
  | Node 3              | 10.4.4.4:444 / ENABLED / ONLINE  |
  | Node 4              | 10.6.6.6:80 / ENABLED / ONLINE   |
  | Session Persistence | None                             |
  | Connection Logging  | False                            |
  | Cluster             | ztm-n02.lbaas.ord1.rackspace.net |
  | Created             | 2011-03-28 15:50:56              |
  | Updated             | 2011-03-28 21:15:07              |
  +---------------------+----------------------------------+

List load balancer usage::

 $ clb show-usage mylb
 +-----------------------+---------------------+
 |        Property       |        Value        |
 +-----------------------+---------------------+
 | averageNumConnections | 0.0                 |
 | endTime               | 2011-03-29 04:58:44 |
 | eventType             | CREATE_LOADBALANCER |
 | id                    | 30444               |
 | incomingTransfer      | 0                   |
 | numPolls              | 158                 |
 | numVips               | 1                   |
 | outgoingTransfer      | 0                   |
 | startTime             | 2011-03-28 15:51:05 |
 +-----------------------+---------------------+
 +-----------------------+---------------------+
 |        Property       |        Value        |
 +-----------------------+---------------------+
 | averageNumConnections | 0.0                 |
 | endTime               | 2011-03-30 03:58:44 |
 | id                    | 30662               |
 | incomingTransfer      | 0                   |
 | numPolls              | 276                 |
 | numVips               | 1                   |
 | outgoingTransfer      | 0                   |
 | startTime             | 2011-03-29 05:03:44 |
 +-----------------------+---------------------+

Delete load balancer::

 $ clb delete mylb

Rename a load balancer::

 $ clb rename mylb my_new_name

Change the port of a load balancer::

 $ clb change-port mylb 81

Change the protocol of a load balancer::

 $ clb change-protocol mylb FTP

Change the algorithm of a load balancer.  Specify the full algorithm name or the abbreviation.::

 $ clb change-algorithm wlc
 $ clb change-algoritm WEIGHTED_LEAST_CONNECTIONS
 $ clb change-algoritm random

+--------------+----------------------------+
| Abbreviation | Algorithm                  |
+==============+============================+
| lc           | LEAST_CONNECTIONS          |
+--------------+----------------------------+
| rand         | RANDOM                     |
+--------------+----------------------------+
| rr           | ROUND_ROBIN                |
+--------------+----------------------------+
| wlc          | WEIGHTED_LEAST_CONNECTIONS |
+--------------+----------------------------+
| wrr          | WEIGHTED_ROUND_ROBIN       |
+--------------+----------------------------+

Add nodes to a load balancer::

 $ clb add-nodes mylb '10.8.8.8:8080,10.9.9.9:8080'

Remove nodes from a load balancer::

 $ clb remove-nodes mylb '10.8.8.8:8080,10.9.9.9:8080'

Enable nodes on the load balancer::

 $ clb enable-nodes mylb '10.8.8.8:8080,10.9.9.9:8080'

Disable nodes on the load balancer::

 $ clb disable-nodes mylb '10.8.8.8:8080,10.9.9.9:8080'

Set the active health check monitor to TCP connect::

 $ clb set-monitor-connect mylb 30 5 3

Set the active health check monitor for HTTP(S) transactions::

 $ clb set-monitor-http mylb 30 10 5 '/test.php' '^[234][0-9][0-9]$' 'my content'
 $ clb set-monitor-https mylb 30 10 5 '/test.php' '^[234][0-9][0-9]$' 'my content'

Display the current health check monitor::

 $ clb show-monitor share
 +----------+---------+
 |  Field   |  Value  |
 +----------+---------+
 | Type     | CONNECT |
 | Delay    | 30      |
 | Timeout  | 5       |
 | Attempts | 3       |
 +----------+---------+

List all supported load balancer algorithms::

 $ clb list-algorithms
 +----------------------------+
 |         Algorithms         |
 +----------------------------+
 | LEAST_CONNECTIONS          |
 | RANDOM                     |
 | ROUND_ROBIN                |
 | WEIGHTED_LEAST_CONNECTIONS |
 | WEIGHTED_ROUND_ROBIN       |
 +----------------------------+

List all supported protocols::

 $ clb list-protocols
 +-----------+
 | Protocols |
 +-----------+
 | FTP       |
 | HTTP      |
 | HTTPS     |
 | IMAPS     |
 | IMAPv4    |
 | LDAP      |
 | LDAPS     |
 | POP3      |
 | POP3S     |
 | SMTP      |
 +-----------+

LICENSE
=======

See LICENSE for license information.

Author
======

Caleb Groom <caleb@calebgroom.com>


