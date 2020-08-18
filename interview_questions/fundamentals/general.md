## Web architecture primer

Let’s start with DNS (domain name system) and HTTP (hypertext transfer protocol). These are the underlying systems 
that web browsers use to send and fetch data to and from web apps. Familiarity with these protocols is essential 
for later discussions on application programming interfaces (APIs), performance and security.

## DNS
When you type an address into a web browser or follow a link, the browser first has to identify which computer server
in the world to ask for the content. Although web addresses use domain names like fivesimplesteps.com to make them 
easier for people to remember them, computers use unique numbers to identify each other1.

To convert names to numbers, the browser queries a series of DNS servers, which are distributed directories of names 
and numbers for all web servers. To speed up this process, the lookups are cached at a number of locations: your 
internet service provider (ISP) will hold a cache, your operating system may hold a cache and even your web browser 
software will hold a short lifetime cache.

## HTTP requests
Hypertext Transfer Protocol (HTTP) is an application-layer protocol for transmitting hypermedia documents, such as HTML.
It was designed for communication between web browsers and web servers, but it can also be used for other purposes.

Once your browser has identified the correct number associated with the domain name, it connects to the server with
the equivalent of, “Hello, can I ask you something?” The connection is agreed and your browser sends a message to 
request the content. As a single web server can host thousands of websites, the message has to be specific about 
the content that it is looking for.

Your browser will add supplementary information to the request message, much of which is designed to improve the speed 
and format of the returned content. For example, it might include data about the browser’s compression capabilities and 
your preferred language.

An HTTP request message for the BBC technology news page will look similar to the example below. Each separate line 
of the message is known as an HTTP header.

```
GET /news/technology/ HTTP/1.1
Host: www.bbc.co.uk
User-Agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.13) […]
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive
```
