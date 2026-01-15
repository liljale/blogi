{
  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" ];
      perSystem = { pkgs, ... }:
        let
          pythonEnv = pkgs.python3.withPackages (ps: with ps; [
            flask
          ]);
        in {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            pythonEnv
            sqlite
          ];
          
          shellHook = ''
            # Create a sqlite database with our schema,
            # if a database does not exist.
            if [ ! -f "database.db" ]; then
              sqlite3 database.db < schema.sql
            fi
          '';
          };
        };
    };
}
