# PUI2016 HW1 - jp4772

*Initial Tangent*: To begin, I was having trouble SSHing into compute from gw. Turns out there was an issue with my version of OpenSSH on my Mac. A quick `brew install openssh`, though, took care of things. So, for reference, if a future student runs into issues with the vague `ssh_exchange_identification: Connection closed by remote host` error, have them upgrade OpenSSH and try again.

Now that I could log in to compute, I promptly got to work.

1. First, I created the directory `PUI2016_jp4772` in my home directory with the trusty `mkdir` command. Hasn't failed me yet.

2. Next, I opened up my `.bashrc` file with vim (Vim guy here), and added a few key lines:
![bashrc goodness](bashrc.png)

3. To test that my ENV variables and alias were working correctly, I spun up a new terminal (did not remember how to load new settings without a new window). Then, with great anticipation, I typed the three lines:
```
pwd
pui2016
pwd
```
This emerged:
![bashing it up](bash_alias.png)

All was well with the world.

![](http://ak-hdl.buzzfed.com/static/imagebuzz/terminal01/2010/2/2/13/zen-kitty-14134-1265133827-4.jpg)
