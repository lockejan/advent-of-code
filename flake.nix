{
  description = "Runtime environments for advent-of-code";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-23.11-darwin";
  inputs.nixpkgs-22-05.url = "github:NixOS/nixpkgs/nixos-22.05";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, nixpkgs-22-05, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pkgs-22-05 = nixpkgs-22-05.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          nativeBuildInputs = [ pkgs.bashInteractive ];
          buildInputs = [
            pkgs-22-05.lua5_1
            pkgs.lua51Packages.busted
            pkgs.gnumake
            # pkgs.ghc
            # pkgs.clojure
            pkgs.python311
            pkgs.python311Packages.pytest
            # pkgs.rustc
          ];
          shellHook = ''
            export PYTHONPATH="./2023/python:$PYTHONPATH"
          '';
        };
      });
}
