# Log Command Line Interface

An interactive command line interface to make working with my personal log quicker and easier.

## Install Python Dependencies

From within the repository, run the following `pip` commands to install the dependencies and make an executable that you can call.

```sh
pip3 install --requirement requirements.txt
pip3 install .
```

## Generate Command Completion File

To generate a completion file run the below.

```sh
# Bash:
_LOG_CLI_COMPLETE=bash_source log-cli > ./.log-cli-complete.bash

# Fish:
_LOG_CLI_COMPLETE=fish_source log-cli > ~/.log-cli-complete.fish
```

## Enable Command Completion

Then source it in your shell file.

```sh
# Bash:
. <path-to-repo>/.log-cli-complete.bash

# Fish:
source <path-to-repo>/.log-cli-complete.fish
```

## Usage

Type `log-cli` and away you go.

