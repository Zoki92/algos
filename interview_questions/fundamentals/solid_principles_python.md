## What is SOLID design
The principles are

#### Single Responsibility Principle
#### Open Closed Princple
#### Liskov's Substitutablilty Principle
#### Interface Segregation Principle
#### Dependency Inversion Principle

## Python Way

The Zen of Python, by Tim Peters


#### Beautiful is better than ugly.
#### Explicit is better than implicit.
#### Simple is better than complex.
#### Complex is better than complicated.
#### Flat is better than nested.
#### Sparse is better than dense.
#### Readability counts.
#### Special cases aren't special enough to break the rules.
#### Although practicality beats purity.
#### Errors should never pass silently.
#### Unless explicitly silenced.
#### In the face of ambiguity, refuse the temptation to guess.
#### There should be one-- and preferably only one --obvious way to do it.
#### Although that way may not be obvious at first unless you're Dutch.
#### Now is better than never.
#### Although never is often better than right now.
#### If the implementation is hard to explain, it's a bad idea.
#### If the implementation is easy to explain, it may be a good idea.
#### Namespaces are one honking great idea -- let's do more of those!


## Code example

```python
class FTPClient:
  def __init__(self, **kwargs):
    self._ftp_client = FTPDriver(kwargs['host'], kwargs['port'])
    self._sftp_client = SFTPDriver(kwargs['sftp_host'], kwargs['user'], kwargs['pw'])

  def upload(self, file:bytes, **kwargs):
    is_sftp = kwargs['sftp']
    if is_sftp:
      with self._sftp_client.Connection() as sftp:
        sftp.put(file)
    else:
      self._ftp_client.upload(file)

  def download(self, target:str, **kwargs) -> bytes:
    is_sftp = kwargs['sftp']
    if is_sftp:
      with self._sftp_client.Connection() as sftp:
        return sftp.get(target)
    else:
      return self._ftp_client.download(target)

```


## Single Responsibility Principle (SRP) 


#### Definition: Every module/class should only have one responsibility and therefore only one reason to change.
#### Relevant Zen: There should be one-- and preferably only one --obvious way to do things

The Single Responsibility Principle (SRP) is all about increasing cohesion and decreasing coupling by organizing 
code around responsibilities. It's not a big leap to see why that happens. If all the code for any given responsibility
is in a single place that's cohesive and while responsibilities may be similar they don't often overlap. Consider this
non-code example. If it is your responsibility to sweep and my responsibility to mop there's no reason for me to keep
track of whether or not the floor has been swept. I can just ask you, "has the floor been swept"? and base my action 
according to your response.

I find it useful to think of responsibilities as use cases, which is how our Zen comes into play. Each use case should
only be handled in one place, in turn, creating one obvious way to do things. This also satisfies the, "one reason to
change" portion of the SRP's definition. The only reason this class should change is if the use case has changed.

Examining our original code we can see the class does not have a single responsibility because it has to manage 
connection details for an FTP, and SFTP server. Furthermore, the methods don't even have a single responsibility 
because both have to choose which protocol they will be using. This can be fixed by splitting the FTPClient class
into 2 classes each with one of the responsibilities.
```python
class FTPClient:
  def __init__(self, host, port):
    self._client = FTPDriver(host, port)

  def upload(self, file:bytes):
    self._client.upload(file)

  def download(self, target:str) -> bytes:
    return self._client.download(target)


class SFTPClient(FTPClient):
  def __init__(self, host, user, password):
    self._client = SFTPDriver(host, username=user, password=password)

  def upload(self, file:bytes):
    with self._client.Connection() as sftp:
      sftp.put(file)

  def download(self, target:str) -> bytes:
    with self._client.Connection() as sftp:
      return sftp.get(target)

```

##  Open Closed Principle (OCP)

#### Definition: Software Entities (classes, functions, modules) should be open for extension but closed to change.
#### Relevant Zen: Simple is better than complex. Complex is better than complicated.

Since the definition of change and extension are so similar it is easy to get overwhelmed by the Open Closed Principle. 
I've found the most intuitive way to decide if I'm making a change or extension is to think about function signatures. 
A change is anything that forces calling code to be updated. This could be changing the function name, swapping the 
order of parameters, or adding a non-default parameter. Any code that calls the function would be forced to change in 
accordance with the new signature. An extension, on the other hand, allows for new functionality, without having to 
change the calling code. This could be renaming a parameter, adding a new parameter with a default value, or adding 
the *arg, or **kwargs parameters. Any code that calls the function would still work as originally written. The same
rules apply to classes as well.

Here is an example of adding support for bulk operations.

Your gut reaction is probably to add a upload_bulk and download_bulk functions to the FTPClient class. Fortunately, 
that is also a SOLID way to handle this use case.

```python
class FTPClient:
  def __init__(self, host, port):
      ... # For this example the __init__ implementation is not significant

  def upload(self, file:bytes):
      ... # For this example the upload implementation is not significant

  def download(self, target:str) -> bytes:
      ... # For this example the download implementation is not significant

  def upload_bulk(self, files:List[str]):
    for file in files:
      self.upload(file)

  def download_bulk(self, targets:List[str]) -> List[bytes]:
    files = []
    for target in targets:
      files.append(self.download(target))

    return files
```

In this case, it's better to extend the class with functions than extend through inheritance, because a BulkFTPClient
child class would have to change the function signature for download reflecting it returns a list of bytes rather 
than just bytes, violating the Open Closed Principle as well as Liskov's Substituitability Principle.

## Liskov's Substituitability Principle (LSP) 


#### Definition: If S is a subtype of T, then objects of type T may be replaced with objects of Type S.
#### Relevant Zen: Special cases aren’t special enough to break the rules.

You may have noticed all of the FTP client classes so far have the same function signatures. That was done 
purposefully so they would follow Liskov's Substituitability Principle. An SFTPClient object can replace an 
FTPClient object and whatever code is calling upload, or download, is blissfully unaware.

Another specialized case of FTP file transfers is supporting FTPS (yes FTPS and SFTP are different). Solving this 
can be tricky because we have choices. They are:
1. Add upload_secure, and download_secure functions.
2. Add a secure flag through **kwargs.
3. Create a new class, FTPSClient, that extends FTPClient.

For reasons that we will get into during the Interface Segregation, and Dependency Inversion principles the new 
FTPSClient class is the way to go.

```python
class FTPClient:
  def __init__(self, host, port):
    ...

  def upload(self, file:bytes):
    ...

  def download(self, target:str) -> bytes:
    ...

class FTPSClient(FTPClient):
    def __init__(self, host, port, username, password):
        self._client = FTPSDriver(host, port, user=username, password=password)

```
This is exactly the kind of edge case inheritance is meant for and following Liskov's makes for effective polymorphism.
You'll note than now FTPClient's can be replaced by an FTPSClient or SFTPClient. In fact, all 3 are interchangeable
which brings us to interface segregation.


## Interface Segregation Principle (ISP)

#### Definition: A client should not depend on methods it does not use.
#### Relevant Zen: Readability Counts && complicated is better than complex.

Unlike Liskov's, The Interface Segregation Principle was the last and most difficult principle for me to understand. 
I always equated it to the interface keyword, and most explanations for SOLID design don't do much to dispel that 
confusion. additionally, most guides I've found try to break everything up into tiny interfaces most often with a 
single function per-interface because "too many interfaces are better than too few".

There are 2 issues here, first Python doesn't have interfaces, and second languages like C# and Java that do 
have interfaces, breaking them up too much always ends up with interfaces implementing interfaces which can get 
complex and complex is not Pythonic.

First I want to explore the too small of interfaces problem by looking at some C# code, then we'll cover a Pythonic 
approach to ISP. If you agree or are just choosing to trust me that super small interfaces are not the best way 
to segregate your interfaces feel free to skip to the Pythonic Solution below.

```C#
# Warning here be C# code
public interface ICanUpload {
  void upload(Byte[] file);
}

public interface ICanDownload {
  Byte[] download();
}

class FTPClient : ICanUpload, ICanDownload {
  public void upload(Byte[] file) {
    ...
  }

  public Byte[] download(string target) {
    ...
  }
}
```

The trouble starts when you need to specify the type of a parameter that implements both the ICanDownload and 
ICanUpload interfaces. The code snippet below demonstrates the problem.

```C#
class ReportGenerator {
  public Byte[] doStuff(Byte[] raw) {
    ...
  } 

  public void generateReport(/*What type should go here?*/ client) {
    raw_data = client.download('client_rundown.csv');
    report = this.doStuff(raw_data);
    client.upload(report);
  }
}
```

In the generateReport function signature you either have to specify the concrete FTPClient class as the parameter type,
which violates the Dependency Inversion Principle or create an interface that implements both ICanUpload, and 
ICanDownload interfaces. Otherwise, an object that just implements ICanUpload could be passed in but would fail the 
download call and vice-versa with an object only implementing the ICanDownload interface. The normal answer is to 
create an IFTPClient interface and let the generateReport function depend on that.

```C#
public interface IFTPClient: ICanUpload, ICanDownload {
    void upload(Byte[] file);
    Byte[] download(string target);
}
```
The Pythonic Solution

To me, ISP is about making reasonable choices for how other developers will interface with your code. That's right 
it's more related to the I in API and CLI than it is the interface keyword. This is also where the "Readability Counts"
from the Zen of Python is a driving force. A good interface will follow the semantics of the abstraction and match 
the terminology making the code more readable.

Let's look at how we can add an S3Client since it has the same upload/download semantics as the FTPClients. We want to
keep the S3Clients signature for upload and download consistent, but it would be nonsense for the new S3Client to 
inherit from FTPClient. After all, S3 is not a special case of FTP. What FTP and S3 do have in common is that they
are file transfer protocols and these protocols often share a similar interface as seen in this example. So instead
of inheriting from FTPClient it would be better to tie these classes together with an abstract base class, 
the closest thing Python has to an interface.

We create a FileTransferClient which becomes our interface and all of our existing clients now inherit from that 
rather than inheriting from FTPClient. This forces a common interface and allows us to move bulk operations into 
their own interface since not every file transfer protocol will support them.

```python
from abc import ABC
def class FileTransferClient(ABC):
  def upload(self, file:bytes):
    pass

  def download(self, target:str) -> bytes:
    pass

  def cd(self, target_dir):
    pass


class BulkFileTransferClient(ABC):
  def upload_bulk(self, files:List[bytes]):
    pass

  def download_bulk(self, targets:List[str]):
    pass
```

What does this afford us though...well this.

```python
class FTPClient(FileTransferClient, BulkFileTransferClient):
  ...

class FTPSClient(FileTransferClient, BulkFileTransferClient):
  ...

class SFTPClient(FileTransferClient, BulkFileTransferClient):
  ...

class S3Client(FileTransferClient):
  ...

class SCPClient(FileTransferClient):
  ...

```

## Dependency Inversion Principle (DIP) 

#### Definition: High-level modules should not depend on low-level modules. They should depend on abstractions and abstractions should not depend on details, rather details should depend on abstractions.

#### Relevant Zen: Explicit is Better than Implicit

This is what ties it all together. Everything we've done with the other SOLID principles was to get to a place where 
we are no longer dependent on a detail, the underlying file transfer protocol, being used to move files around. 
We can now write code around our business rules without tying them to a specific implementation. Our code satisfies 
both requirements of dependency inversion.

Our high-level modules no longer need to depend on a low-level module like FTPClient, SFTPClient, or S3Client, 
instead, they depend on an abstraction FileTransferClient. We are depending on the abstraction of moving files 
not the detail of how those files are moved.

Our abstraction FileTransferClient is not dependent on protocol specific details and instead, those details 
depend on how they will be used through the abstraction (i.e. that files can be uploaded or downloaded).

Here is a example of Dependency Inversion at work.
```python
def exchange(client:FileTransferClient, to_upload:bytes, to_download:str) -> bytes:
    client.upload(to_upload)
    return client.download(to_download)

if __name__ == '__main__':
    ftp = FTPClient('ftp.host.com')
    sftp = FTPSClient('sftp.host.com', 22)
    ftps = SFTPClient('ftps.host.com', 990, 'ftps_user', 'P@ssw0rd1!')
    s3 = S3Client('ftp.host.com')
    scp = SCPClient('ftp.host.com')

    for client in [ftp, sftp, ftps, s3, scp]:
        exchange(client, b'Hello', 'greeting.txt')
```
