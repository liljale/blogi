{
  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" ];
      perSystem = { pkgs, ... }: {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            (python3.withPackages (ps: [ ps.flask ]))
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
