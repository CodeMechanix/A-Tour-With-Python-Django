## Using GIT on local server and local PC


There is no difference in accessing a central Git repository on local and remote servers. All tutorials are valid in either case. For the basic access you simply need:

Create a normal user account on the server (e.g. git or george).
Set up a SSH key access to that account. There are many tutorials online, just pick one. For example Github tutorial. The objective is that when you are on your Mac you can SSH to the user account on the server without a username/password, just with the key.
Login to the user account on the server create a bare Git repository.
That's it, then you can access that repository from your Mac.

For example, assume that the server name is myserver.com and it's IP is 192.168.1.50. You login to that server over SSH:
```py
ssh george@192.168.1.50
```
If the key is set up correctly, you are now logged in (without providing username/password). Now create the bare repository:
```py
mkdir mygit
cd mygit
mkdir myrepository.git
cd myrepository.git/
git --bare init
```
Then on the Mac create a new repository:
```py
mkdir mylocalrepo
cd mylocalrepo
git init
echo "sometext" > firstfile.txt
git add firstfile.txt
git commit -m "First commit"
```
Now you can specify the repository created on the server as the remote repository for your local repository. On your Mac (or any other machine on which you want to access that repository):
```py
git remote add origin george@192.168.1.50:mygit/myrepository.git
git push origin master
```
Alternatively, use the server name rather than IP, and a different remote name:
```py
git remote add origin2 george@myserver.com:mygit/myrepository.git
git push origin2 master
```
Once you have those basics working you can then start thinking about adding a WWW interface.

Problems Link: 
[Click Me](https://stackoverflow.com/questions/36896958/using-git-on-local-server-and-local-pc)

[Click Me](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server)