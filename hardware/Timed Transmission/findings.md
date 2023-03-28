iR1d3sC3nT

We need to download Logic 2 on Kali Linux or Windows:
https://www.saleae.com/downloads/

Info: On Linux we need to right click on Logic-2.4.7-master.AppImage and Properties -Permissions and Allow this fil to run as a program.

Then we open the .sal file and we have 5 bin files. Each file is a Message Fragment that we need to decode to find the flag. 

The Information of the Challenge say that is a serial signals. So we need to use Async Serial for each bin file. 

I think that is a UART baud rate so:
What is the common UART baud rate?
9600
There are many different speeds supported on UARTS: 300, 600, 1200, 1800, 2400, 4800, 7200, 9600, 14,400, 19,200, 38,400, 57,600, and 115,200 baud. The most common speed used by default on systems is 9600.

We need to test each Async Serial Analyzer so we can find the right bit rate and export as ASCII to find the flag

I attach to the folder the .sal file with the current changes I apply. I think I'm close but something Ι'm missing.