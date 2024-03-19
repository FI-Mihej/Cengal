[Readme](README.md)

---


# Workspace creation

Lets say I plan to develop my "Snake_3D_Game".

Install Cengal library:

```
python -m pip install cengal
```

Go to new folder you wish to use for your new project.

For example I'll use `~/dev/Snake_3D_Game` under Linux or macOS:

```
~/dev$ mkdir Snake_3D_Game
~/dev$ cd ./Snake_3D_Game
```

or `C:\Dev\Snake_3D_Game` under Windows:

```
C:\Dev> mkdir Snake_3D_Game
C:\Dev> cd .\Snake_3D_Game
```

Then I'll create a new project with an appropriate structure by executing `cengal__package__create`:

```
~/dev/Snake_3D_Game$ cengal__package__create
```

or:

```
C:\Dev\Snake_3D_Game> cengal__package__create
```

> An alternative way to execute this command is to run `python -m cengal.build_tools.packages.create`

As result you'll be asked a set of project related questions. You may either answer or just hit `Enter` button in order to use default value.

First question you'll be asked is a `project type`. There are two project types:

1. `Multi-project with internal python lib` - recommended for all cases.
2. `Single project` - consists only of a content of an internal python lib.

## Multi-project with internal python lib

Enter "1" (without quotes). Or just hit `Enter` button since it is a default value.

Next questions (in this example I'll use default values):

2. "Main project name:"
    * Default: current dir name will be use as a source of main project name generation.
    * Will be used in our case: "snake_3d_game"
3. "Internal python lib name:"
    * Default: main project name will be use as a source of main project name generation
    * Will be used in our case: "snake_3d_game_lib"
4. "Author:"
    * Default: "John Doe"
    * Will be used in our case:  "John Doe"
5. "Email:"
    * Default: "johndoe@localhost.com"
    * Will be used in our case: "johndoe@localhost.com"
6. "Copyright years range:"
    * Default: current year
    * Will be used in our case: "2023"
7. "Version:"
    * Default: "1.0.0"
    * Will be used in our case: "1.0.0"
8. "License:"
    * Default: "Apache License, Version 2.0"
    * Will be used in our case: "Apache License, Version 2.0"



## Single project


---

[Readme](README.md)
