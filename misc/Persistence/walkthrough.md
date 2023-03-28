# Challenge Name: [Challenge name]

**Category:** [Category]  
**Points:** [Point value]  
**Author:** [Your name]  
**Team:** [Your team name]  
**Completion Date:** [Date of comple7tion]

## Introduction

The idea of this challenge is to create an automation to execute a get request more than 1000 times. 

## Tools Used

- Bash/Any Programming Language
- Burp

## Initial Analysis

[Explain your initial thoughts and observations upon receiving the challenge. Describe any clues, hints, or files provided.]

## Detailed Methodology

### Step 1: Wit burp

- Send the request to intruder
- use numbers payload 

### Step 2: With custom bash

run the get_x_times.sh

```chmod +x get_x_times.sh```
```./get_x_times.sh IP/flag 1001 ```

grep based on regex HTB\{[a-zA-Z0-9_!]+\} 

```grep -E 'HTB\{[a-zA-Z0-9_!]+\}' responses.txt```

## Vulnerability Identification and Exploitation

[Describe the vulnerabilities you identified during your analysis. Explain how you exploited these vulnerabilities to achieve the challenge objectives.]

## Flag Capture

[Detail the final steps leading to the capture of the flag. Include the flag itself (in a spoiler or hidden text, if necessary).]

<details>
<summary>Click to reveal the flag</summary>
HTB{y0u_h4v3_p0w3rfuL_sCr1pt1ng_ab1lit13S!}
