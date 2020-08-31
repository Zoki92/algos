## Node and Npm notes

When using -g with npm for example:

npm -g install express

It's being installed in the global cache, whilst done without -g is done in the local project.

You can add a dependency in dependencies object in package.json file, for example:

```
{
  "name": "temp",
  "version": "1.0.0",
  "description": "Init'ing a project",
  "main": "test.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "Frank W. Zammetti",
  "license": "ISC",
  "dependencies": {
    "express": "^4.16.1"
  }
}
```

And after adding it run npm install. Another alternative is to use the command line:

npm install express --save

This will add the dependency entry.
You can also replace --save with --save-dev, which means that devDependencies entry will be added to package.json. This
are modules that you only need during development. Two good examples of these are Webpack and Typescript. Also when 
uninstalling dependencies --save and --save-dev can be used.


Most common dependency versions:
    • “express” : “1.2.3” – NPM will grab this specific version only.
    • “express”: “~1.2.3” – NPM will grab the most recent patch version.
    (So, ~1.2.3 will find the latest 1.2.x version but not 1.3.x or anything
    below 1.2.x.)
    • “express”: “^1.2.3” – NPM will grab the most recent minor version.
    (So, ^1.2.3 will find the latest 1.x.x version but not 1.3.x or anything
    below 1.x.x.)
    • “express”: “ * ” – NPM will grab the newest version available. (There is
    also an explicit latest value that does the same thing.)

#### More on package.json

Keys available:
    • name – We start with a simple one: the name of the thing you’re
    coding! The name element’s value must be no more than 214
    characters, cannot start with a dot or an underscore, can have no
    uppercase letters, and must be URL-safe.

    • author – The author is a single person and is defined by an object
    with three potential attributes: name, email, and url (where name is
    required, and both email and url are optional). Alternatively, you
    can make the value a single string in the form "<name> <email>
    (<url>)" and NPM will parse it for you automatically.
    bin – Some packages require executables to be installed to do their
    work and added to the path. That’s where the bin element comes
    in. You can make the value an object (or map, which is probably the
    more appropriate term here) that maps a command to an executable
    and NPM will take care of “installing” it for you when you install the
    package by creating the appropriate symlink.

    • browser – Some modules are meant to be used in a browser, not in
    Node, and for those packages, you can use this element instead of
    the main element (coming up shortly!) to hint to the users of your
    package that it depends on primitives available to JavaScript that
    aren’t available in Node.

    • bugs – If your project has an issue tracker, then you can reference
    it with the bugs element. The value of this is an object with two
    attributes, url and email, and you can specify either or both (but you
    must specify at least one, or NPM will complain).

    • bundledDependencies – Some projects need to preserve NPM
    packages locally or through a single download. For those, this
    element allows you to specify an array of package names that will be
    bundled with your package when you publish it.

    • config – If you need to have parameters available in the environment
    when your package is used, then the config element might do the
    trick. Here, you can specify a value like "config" : { "port" :
    "8888" } and then in your code you can reference npm_package_
    config_port as an environment variable to get the value configured.

    • contributors – The contributors element is just like the author element
    except that this is an array of people who helped with the project.

    • cpu – If your code is only meant to run on certain system architectures,
    you can specify which as an array of strings with the cpu element.

    • dependencies – You saw the dependencies element in the previous
    chapter, but I’ll also mention that in addition to specifying a package
    name and optionally a version to be pulled down from the NPM
    registry, you can also specify a URL to a tarball to be downloaded or a
    Git/GitHub URL or a local file system path.

    • description – A freeform string that describes your package. It’s as
    simple as that!

    • devDependencies – Again, one I mentioned in the previous chapter,
    and it’s simply the same as dependencies, but it names packages that
    are only needed during development.

    • directories – This element allows you to describe the structure
    your package, things like the location of library components binary
    content, man pages, Markdown documentation, examples, and tests.
    See the Common JS package specification for details on this.

    • engines – This element allows you to specify what version(s) of Node
    your package works on. You can also use this element to define what
    version(s) of NPM is capable of properly installing the package.

    • files – When your package is installed as a dependency, NPM will
    need to know what files to include. It will by default assume all, but if
    you want or need to be specified, then the files element will let you
    do that. It works a lot like a .gitignore file, but in reverse: anything
    listed in this element will be included, not ignored.

    • homepage – If your project has a web site, then you can specify the
    URL of its homepage with this element.

    • keywords – The keywords element is an arbitrary array of strings that
    can be used to help people find your package (more on this in the
    next section).

    • license – The value of the license element is the license your
    package is released under. The value of this must be a currently
    registered SPDX license identifier (see spdx.org for a list).
    Alternatively, if you are using a custom license or one that doesn’t yet
    have an SPDX identifier, then you can set the value to "SEE LICENSE
    IN <filename>" and place the <filename> license file alongside the
    package.json file. Or, if you don’t grant rights to use your package to
    anyone (vis-à-vis, you want to make it private and/or unpublished),
    then you can use a value of "UNLICENSED".

    • man – With this element you can specify a single file or an array of
    filenames to put in place for the Linux man program to display for
    your package.

    • main – This is the primary entry point to your package. For example,
    if your package is named super_duper_cool_package, then a user
    will expect to be able to do require("super_duper_cool_package")
    after they install it. To allow this, the main element must point to the
    file that exports your package’s main export object.
    • optionalDependencies – If your package has dependencies and
    NPM can’t install them, then it will fail the installation of your
    package. If, however, you want to specify that some dependencies
    are okay to be missing and that NPM should go ahead with the
    installation anyway, then optionalDependencies is where you can
    list them.

    • os – Just like cpu, if your package only works on certain OSs, then this
    element is where you can have an array of strings naming those it
    runs on.

    • peerDependencies – Sometimes, a package will function as a plugin
    to others, and so you’ll need a way to define what other packages
    yours is compatible with. The peerDependencies element allows you
    to do that.

    • private – If you want to ensure that you can’t accidentally publish
    your package, then set private to false, and NPM will refuse to publish
    it (more to come on publishing in the next section).

    • publishConfig – This element is an object that defines many pieces
    of metadata that come into play with publishing your package to the
    NPM registry. This includes things like tags and such. This can get
    fairly involved, and we won’t (for the most part) be worrying about
    any of it in this book beyond a few words in the next section, so I’ll
    leave this one to the NPM documentation if and when you need it.

    • repository – If you’d like to specify where the code for your package
    lives, whether GitHub or something else, whether public or private,
    the repository element is where you do that.

    • scripts – As mentioned in the previous chapter, the scripts element
    allows you to specify a dictionary of commands that can be run at
    various points in the lifecycle of your package for various purposes.
    Like publishConfig, this can get a bit involved, so I defer to the NPM
    docs for details.

    • version – This is the version of your module, and it must use SemVer
    as discussed in Chapter 1. The name and version values together
    form a unique “coordinate” to your package, an identifier that
    is assumed to be completely unique. If you plan to publish your
    package, then name and version are the most important elements
    in package.json (if you don’t publish it, then they’re a bit less
    important, but for your own sanity, you should probably make them
    meaningful anyway!).

#### Package security

The sad reality is that, sometimes, packages you use will be discovered to have security
vulnerabilities, just like any other software you use. But, being aware of this, the NPM
team has constructed a useful command for dealing with this:

npm audit

Running this command will scan your package.json file (or global packages if you
use -g) and submit the list of dependencies to the default NPM registry requesting a
report on any known vulnerabilities in them. This report will also include information on
how to remediate. But, if you want the quick answer, execute this command:

npm audit fix

That will cause NPM to update any vulnerable packages with the newest available
version that hasn’t had the vulnerability reported in it.
If you’d like to see a detailed audit report, execute

npm audit --json

or, if you prefer plain text

npm audit --readable

Finally, if you’d like to see what npm audit fix would do but without literally doing
it, you can use

npm audit fix --dry-run

#### Updating Packages
Once you have a project set up, you may on occasion want to update the packages it
depends on. This is very easy to do:

npm update

Yep, that’s it! NPM will go off and update all packages to the latest version, respecting
your SemVer settings. You naturally can stick a -g in there too in order to update global
packages.

