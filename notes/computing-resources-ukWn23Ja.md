# Computing Resources

###### status: `reference` · last reviewed: TBD

###### tags: `computing` `git` `GitHub`

## Python/Anaconda

### Caltech HPC

At Caltech HPC the recommended way to install Python modules is also via Anaconda. Follow the instructions [here](https://www.hpc.caltech.edu/documentation/software-and-modules) (under "Anaconda Package Management" and "Example 1") to install `conda`. You can then install packages using:
```
conda install <packagename>
```

## Git and GitHub

Some basic resources for getting started with version control using `git` and GitHub are:

* [Using GitHub for academic research](https://hackmd.io/@vivek-blog/github_article)
* [`skills.github.com`](https://skills.github.com/)

### Authenticating to GitHub

GitHub no longer allows you to authenticate via username and password when pulling/pushing. Instead you can use a Personal Access Token or an SSH key. On Caltech HPC it is recommended to set up an SSH key for authentication.

#### Creating an SSH key

##### Generate the key

Enter the command:
```
ssh-keygen -t ed25519 -C "abenson@carnegiescience.edu"
```
replacing the `abenson` with you actual Carnegie username. This will start the process of generating an SSH key. You'll be asked for a file name, enter:
```
/home/abenson/.ssh/github_ed25519
```
replacing the `abenson` with your own username. When asked for a passphrase just hit `enter` so that no passphrase is required (then hit `enter` again to confirm). If this all works you will see output something like this:
```
$ ssh-keygen -t ed25519 -C "abenson@carnegiescience.edu"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/abenson/.ssh/id_ed25519): /home/abenson/.ssh/github_ed25519
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/abenson/.ssh/github_ed25519.
Your public key has been saved in /home/abenson/.ssh/github_ed25519.pub.
The key fingerprint is:
SHA256:fbbRNQr2u4pJfjaZv3lg9gu+1dlwIO1SFVD+fMhjlcs abenson@carnegiescience.edu
The key's randomart image is:
+--[ED25519 256]--+ 
|             .ooo|                                                
|             ....|                                               
|           o. ++o|                                                 
|         .. o*o*+|
|        S . =oOE=|
|           o O.+=|
|         .  *oooo|
|        o o*. =o |
|         +o.+B+..|
+----[SHA256]-----+ 
```
and a key will have been generated in the `~/.ssh` directory.

Next, edit your `~/.bashrc` file and add these lines at the end:
```
eval "$(ssh-agent -s)" >& /dev/null
ssh-add /home/abenson/.ssh/github_ed25519 >& /dev/null
```
which will ensure that your SSH key is activated every time you log in.

#### Adding the key to GitHub

First copy the newly generated public key to your clipboard:
```
cat ~/.ssh/github_ed25519.pub
```
will display the public key in the terminal, which will look something like:
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ0P4MArMGSypyBQv51d7ZSuDRhxfROWk2/Bg8NhAM/1 abenson@carnegiescience.edu
```
Select this entire text in the terminal and copy to the clipboard.

Next, go to [https://github.com/settings/keys](https://github.com/settings/keys) and click the green "New SSH key" button. In the "Title" box enter "Caltech HPC key". In the key box paste your new SSH key from the clipboard. Finally, click the green "Add SSH key" button. 

You should be all set and able to push/pull to/from GitHub.

#### Configure the cluster to use your key

On Caltech HPC run the command:
```
git config --global core.sshCommand "ssh -i ~/.ssh/github_ed25519"
```
which tells `git` to always use this key when communicating with GitHub over `ssh`.

### Special tools for `diff`ing files

The `git diff` command will show you changes in a file (relative to the last committed version by default, although you can pass options to have it show you chanegs relative to any version). This works well for text files (e.g. source code), but for binary files (e.g. `hdf5` files) it will only report if the file differs, not how it differs. we have some special diff tools available for this case (and for XML files). 

The configuration for these tools is stored in the `.gitconfig` file in the Galacticus repo. To make use of this configuration, first be sure that you have this file included in your `git` config. You can set this locally, just for the Galacticus repo that you are working in using:
```
git config --local --add include.path ../.gitconfig
```
or globally, for all `git` repos using:
```
git config --global --add include.path ../.gitconfig
```

Then, you can do, for example:
```
git difftool -t hdf5diff myHDF5File.hdf5
```
which will use the [`h5diff`]()https://support.hdfgroup.org/documentation/hdf5/latest/_h5_t_o_o_l__d_f__u_g.html tool to show you differences in the `myHDF5File.hdf5` file. 

For XML files you can do:
```
git difftool -t xmldiff myXMLFile.xml
```
which will use the [`xdiff`](https://hg.sr.ht/~nolda/xdiff) tool to show differences.

## Development tools

### VSCode

The recommended development environment for OBS HPC and Caltech HPC is [VSCode](https://code.visualstudio.com/). This provides a full IDE (Integrated Deveopment Environment), with a graphical interface, and powerful tools to help you write code more efficiently.

To install VSCode on your laptop, visit the [downloads](https://code.visualstudio.com/download) page and follow instructions there.

After installing, you'll likely want to install some extensions. As you use VSCode it will suggest extensions that might be useful to you (e.g. if you open a Python file, it will suggest that you install an extension that provides highlighting and other features for Python).

If you are developing Galacticus, it's recommended that you install the [`Galacticus Code`](https://marketplace.visualstudio.com/items?itemName=GalacticusOrg.galacticus-code) extension. To do this, simply browse the Extensions Marketplace - for instructions on how to do this see [here](https://code.visualstudio.com/docs/editor/extension-marketplace#_browse-for-extensions) - and search for "Galacticus". Click on the `Embedded XML/LaTeX in Galacticus` extension, and then click the "Install" button.

VSCode allows you to connect to a remote server (e.g. OBS HPC or Caltech HPC) over an `ssh` connection - see [here](https://code.visualstudio.com/docs/remote/ssh) for full details. To do this, in the Command Palette in VSCode (press `F1` or `Ctrl+Shift+P` to get to the Command Palette), and select `Remote-SSH: Connect to Host...` (just start typing this and it will appear). Then, when prompted, enter the connection details. For example, for OBS HPC you would enter:
```
abenson@obshpc.carnegiescience.edu
```
(replacing `abenson` with your own username).

VSCode will then prompt you to enter your password and then for Duo two-factor authentication (note that these prompts show up in the Command Palette - they're not alwasy super obvious to see). Once you have authentciated, VSCode will connect to the remote server, and (if this is your first time connecting) will install itself on that server automatically. You're then ready to start opening files and editing them on the remote server. (Note that some extensions may ask if you want them to be installed on the remote server also - in general, yes, you do want that).

#### Updates from Paul Menker

Note that the extensions "[marketplace](https://marketplace.visualstudio.com/VSCode)" can also be found on the left side of the screen, under the symbol with all the squares.   Some other useful extensions I've found are: 
* [Python](https://code.visualstudio.com/docs/languages/python) - I think Andrew mentioned this, but you probably need this extension for python to run. A debugger extension should be automatically installed when you download this, so now you can use a debugging session the way you would on a local machine. If anyone else found themselves trying to refactor/write code on a local machine, then transfer it back to compute cluster to finish editing, this should make development a lot faster. 
    * However, to my knowledge, one can't debug on interactive nodes (unless one uses the old school [PDB](https://docs.python.org/3/library/pdb.html) module, but that works without an IDE), and debuggers run ~30% slower than simply running code, so I've found I have to be mindful of sample size when I'm testing code, so I don't burden the login node.
* [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - I'm not 100% sure which extension does what, but I think this is the amazing one that enhances texture. Maybe other people don't have this problem, but when I was using Pycharm, I found about 90% of the red and yellow underlines to be completely bogus warnings, either saying that variables I'd already defined don't exist, or complaining about very specific formatting. But, whether it's through Pylance or default behavior, VScode's warnings actually work, and I've almost never seen a false warning. There's also a really good autocomplete feature, which makes it possible to write descriptive variables without having to repeat myself again and again. 
* [Pytest](https://marketplace.visualstudio.com/items?itemName=datoux.vscode-pytest-intellisence) a really cool testing module. If anyone has added tests to their code, you just type "pytest" in a directory, and every file starting with 'test_' (in the root directory or any subdirectory!) will run, and it'll give you a really pretty report on what worked.  I've found some minor bugs in my usage, but it just doesn't always show all the tests that worked, which matters far less than seeing the failures.
* [Indent Rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow), which makes reading deeply nested .xml files much easier (colors each level of indentation)
* [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv), adds a bunch of colors to many file types like .xml, making them so much more readable.
* [XML tools](https://marketplace.visualstudio.com/items?itemName=DotJoshJohnson.xml) - maybe this is actually the one that highlights .xml files. I'm not sure, these extensions are really easy to download, so I would just add them all. 
* [Fortran](https://marketplace.visualstudio.com/items?itemName=Gimly81.fortran) - if anyone has the unfortunate experience of having to parse through or edit all the .F90 source files, adding colors will give you a fighting chance. I went through basically all the Fortran extensions available on VSCode, and I personally thought this was the best. Note that it gives an error-looking red color to some indentations - I can't tell if this is a bug or poor design, but one has to learn to ignore these.
* [Git graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) I don't use this one that often, but it can be a good way to visualize all of one's GitHub branches (local and at origin I think) if one is using version control. 
* Themes: more than anywhere else I've seen, there are a bajillion different "themes" (color schemes) one can download. The internet loves [night owl](https://marketplace.visualstudio.com/items?itemName=sdras.night-owl) and [solarized](https://marketplace.visualstudio.com/items?itemName=ryanolsonx.solarized), but I find the default "Dark+" theme works really well. All the confetti colors looks kind of ridiculous at first, but you'd be shocked how much easier it is to find that missing parenthesis when each layer of a deeply nested function is in different colors, or to separate functions from variables from keywords. (Themes can be changed by using "Command + shift + P" to open that command pallete, then searching "color theme". Some of them have to be downloaded from the that "marketplace", but you're be automatically redirected if you click on an option)

For people coding in other languages, there are definitely just as many extensions for C++ or java, and if you just search "best VSCode extensions " on Google or YouTube, you'll find a bajillion options for any problem you might have

Unfortunately, VSCode doesn't have a default-opened terminal, so if you need to test a line of code quick, you'll either have to open a debug session, run interactively using "python3" or "ipython" commands, or, like me, keep pycharm installed so I can see if I've broadcasted arrays properly. 

Environments seem to work slighlty differently than if one accesses Caltech HPC using a default terminal, but people are welcome to use my environment at ``/central/groups/carnegie_poc/pmenker/miniconda3/envs/fastEnv/``, and I'm happy to help people troubleshoot if need be. 

On the whole, I've found that despite its reputaiton for approachability, VSCode can be pretty overwhelming at first, because it's completely customizable and has so many gadgets. It's a very polarizing IDE in the coding community (some people consider it the salvation of coding, others call it a failure because you have to add many of the extensions yourself). But, I can probably develop 5-10x faster using it. There's a search feature that works through all directories, so if you have that one test you wrote months ago but can't remember the filename, you can search for a specific line of code and all matches will come out. Also, if one is constantly jumping between different directories (because your data is stored in `/central/` but your code is stored in `/home/`, or if you have two separate repos you're combining like I am), VScode starts to remember the files you open a lot, making it easy to pull them out of a mess of code. The find and replace functionality is probably worse than PyCharm (although still much better than emacs), and you can't change function signatures automatically, but there are a bunch of other nonintuitive shorcuts that can be really helpful.  One can Google much better guides than this, but using `command + options + up/down` on Mac can give you multiple cursors, pressing `F12` on a function or variable will jump to all the other places it's used in the code, and `FN + ctrl + -` will jump back to the last (several) places you've been in code. Both these features work across files, so a lot of time can be saved if one needs to change a parameter, then go to another file to run a test. Also, VSCode defaults to autosaving files (can be turned off), so if you're like me where you always fix a bug in code, but forget to to hit save and then your simulation fails again, this can be really helpful and allow for real-time change. The files you had open in a directory will stay open when you log back in, and you can use multiple terminals (really helpful if you're waiting for Galacticus to rebuild, and want to do something else in the meantime, or want to run code in one place, and check what happens to files somewhere else)

Also, I've found that VSCode sessions are a lot more stable (using a regular terminal seems to disconnect much more frequently), but VSCode is a lot more finnicky with the login. For some reason, if one takes more than a few seconds to enter their password and Duo push, the login will timeout. It still takes me a few tries to log in usually, but if you have Duo already open, this can be a good way for us physicists to keep our reaction time sharp!

## `tmux`

`tmux` is a terminal multiplexer - it allows you to run multiple terminals inside a single `ssh` session. The most useful feature of this is that you can disconnect (intentionally or otherwise) from the remote computer, and your terminals inside `tmux` continue to exist - even continuing to run commands that were underway. When you reconnect to the remote computer you can then reconnect to the `tmux` session and everything will be just as you left it.

On Caltech HPC you can find `tmux` in `/usr/bin/tmux`.

There's a reasonably good introduction to `tmux` by RedHat that you can find [here](https://www.redhat.com/sysadmin/introduction-tmux-linux).

## Software Engineering

Here are a few useful links on concepts in software engineering - all generally on the theme of how to write good (understandable, maintainable, verifiable) code:
* [Why you shouldn't use "magic numbers"](https://csharpdeveloper.wordpress.com/2015/09/07/roberts-rules-of-coders-6-dont-use-magic-numbers/)
* [Why it's ok to write a kludge, sometimes](https://tommcfarlin.com/write-a-kludge/)
* [How to refactor your code](https://refactoring.guru/refactoring)
* [Cognitive load is what matters](https://minds.md/zakirullin/cognitive#long)

#### Updates from Paul Menker

If any of you are like me, and are a physicist first, coder second, and you find yourself needing to learn coding better without doing a whole computer science degree, here are a few classes I've found helpful. Some of them can be kind of long, but oftentimes they can be useful even for one specific topic. Also, maybe I should say this, but I have logins for basically all of them that I'm happy to share:
* [Understanding Git and Github](https://www.udemy.com/course/git-and-github-bootcamp/) - pretty long, but watching the first few videos in any section should be a good overview
* [Python Masterclass](https://www.udemy.com/course/the-modern-python3-bootcamp/?couponCode=ST6MT103124) - anything you could possibly need to know about python short of building your own AI, but same advice applies here. 
* [Writing "clean" code](https://www.udemy.com/course/writing-clean-code/) - maybe a little over the top, but can be helpful if everything feels sphagettified and impossible to debug
* [Faster python](https://www.linkedin.com/learning/faster-pandas/) - don't have access to this one anymore (but one can sign up for a free trial of Linked In Learning to watch it all for free). This one is technically geared towards the PANDAS module, but I think pretty much every idea can work with numpy as well
* [Writing tests](https://www.udemy.com/course/unit-testing-and-tdd-in-python/) - haven't finished this one yet, but it's a good introduction to the "veggies" of the coding world. 