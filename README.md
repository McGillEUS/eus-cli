# EUS Command Line Tool

This repo will contain the code behind the EUS CLI. This command line tool will be primarily used to integrate Github with deployments to our AWS server.

Right now, the development flow is very awkward as it involves running `scp` manually a whole lot. This CLI will make developing websites hosted by the EUS easier.

Please report any bugs or issues with this CLI to it.director@mcgilleus.ca

# Install

To use this CLI, simply run `pip install .` from the root of this repository.

Then, it can be used via the command `eus` in a similar fashion to Git.

# Use

There are a variety of commands you can use with this CLI, all of which are described when you type `eus` into your command line terminal.

## Generic `git` Commands

Some common functionalities of `git` are used by this CLI. For example:

- add
- status
- commit
- push

You can use these exactly the same way you would with `git`. [For more information, visit this page.](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)

## Specific EUS Commands

Most of the time, we want to update websites on our server. There are two interesting commands to do this:

- get: simply run `eus get`, then specify the name of the project you want. It will copy all the files from that project to your current directory. The "name of the project" refers to its name on our server as you would find it under `/srv/www/`.

- deploy: used by running `eus deploy`. You will be faced with a few parameters, namely...

... Source: This refers to the path on your machine to the files you want to copy. For example, if I want to update the `potato` website, I would go in the folder which contains the `index.html` for `potato` on my local computer and put `.` as the Source.
... Destination: In the previous example, this would be `potato`. This matches to the same thing as the project name for `eus get`: the project's name on the server under `/srv/www/<project>`.

Both of these commands will prompt you to input your username and password. These credentials refer to your server credentials.

- create: COMING SOON (will be used to create a new website based on our existing templates.
