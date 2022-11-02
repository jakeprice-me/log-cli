# Log Command Line Interface

An interactive command line interface to make working with my personal log quicker and easier.

## Install Python Dependencies

From within the repository, run the following `pip` commands to install the dependencies and make an executable that you can call.

```sh
pip3 --requirement requirements.txt
pip3 install .
```

## Generate Bash Command Completion File

To generate a bash completion file run the below.

```sh
_LOG_COMPLETE=bash_source log > ./log-complete.bash
```

## Enable Bash Command Completion

Then source it in your `.bashrc` file.

```sh
. <path-to-repo>/log-complete.bash
```

## Usage

Type `log` and away you go.

