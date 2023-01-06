<h1>file-version-manager (fvm)</h1>

fvm is a command-line utility that allows you to easily manage multiple versions of a file. It works by creating a backup copy of the file, appending a `.bak` suffix to the filename. If a `.bak` copy already exists, fvm will create a `.bak-1` copy, `.bak-2` copy, and so on, until it finds a suffix that has not been used yet.

<br>

<h1>Installation</h1>

To install fvm, run the following command:

```bash
curl -s https://raw.githubusercontent.com/AsP3X/file-version-manager/master/install.sh | bash
```

This will download the fvm script and make it executable, and create a symlink to the script in `/usr/bin`, so you can run it from anywhere on your system.

<br>

<h1>Usage</h1>

To create a backup copy of a file, simply run `fvm` followed by the file path:

```bash
fvm --cleanup /path/to/file
```

To delete all backup copies of a file, use the `--cleanup` flag:

```bash
fvm --cleanup /path/to/file
```

You can also specify multiple files to be backed up or cleaned up:

```bash
fvm /path/to/file1 /path/to/file2 /path/to/file3

fvm --cleanup /path/to/file1 /path/to/file2 /path/to/file3
```

<br>

<h1>Limitations</h1>

- fvm will not work if the file does not have write permissions.
- fvm will not delete backup copies of a file if it does not have write permissions in the file's directory.
- fvm will not create a backup copy if a file with the same name and suffix already exists.
- fvm only works with files, not directories.

<br>

<h1>Disclaimer</h1>

Use fvm at your own risk. It is recommended to make a backup of your files before using fvm, in case something goes wrong. The author of fvm is not responsible for any loss of data.