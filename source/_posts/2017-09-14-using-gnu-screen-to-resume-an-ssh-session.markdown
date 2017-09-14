---
layout: post
title: "Using GNU Screen to resume an SSH session"
author: "波儿比 Bobbie"
date: 2017-09-14 13:30:46 -0400
comments: true
categories: technology
---

### Why GNU Screen?

**Scenario**: you finish working with an SSH session, you close your laptop to go for lunch or for a tea. Then you come back and open your laptop wanting to resume your job, but the connection is broken or the VPN breaks and forced you to disconnect. You have no choice but setup the connection once again and reopen the documents/apps before you can resume from where you left.

<!--more-->

**Solution**: with GNU Screen, you can directly resume from where you left, without having to reopen all the documents/apps you've been working on.

The concept of GNU Screen is like turning on and off of a computer screen. You turn off a screen when you are done, let the computer to hang in there; you come back later, turn the screen back on and continue your tasks.

### Steps Using GNU Screen

1. **Connect**. Connect to a remote server and create a Screen session via `ssh -t <server.domain.name> screen -R`
2. **Detach**. When done with the SSH session, use `ctrl-a d` to detach from the session. This also disconnect with the SSH server.
3. **Reconnect**. The SSH session is still running actually. When you are ready to resume working with the session, use `ssh -t <server.domain.name> screen -R` again to reconnect, then you are right where you left it.
4. **Terminate**. To permanently terminate a Screen session, just disconnect from the server the usual way (`ctrl-d`).

**Limitation**: If you are using apps with graphical interface, not just the command line environment, then `screen` is not suitable for resuming such jobs, and [VNC](https://en.wikipedia.org/wiki/Virtual_Network_Computing) instead would be the ideal choice.
