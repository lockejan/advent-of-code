# advent-of-code

Just some experimentations with programming languages, while trying to solve the advent-of-code puzzles.

To run the given code with the exact same environment on any machine, [Nix](https://github.com/NixOS/nix) needs to be installed.
[Direnv](https://github.com/nix-community/nix-direnv) will then provision everything else and drop you into a dev-shell.

## 2021

The following subsections are just to document language specific stuff.

### Lua

Tests have to be executed from the directory they are stored in.
```shell
cd ./2021/lua/
./tests.lua
```
or via the included Makefile &rarr; `make test`.
