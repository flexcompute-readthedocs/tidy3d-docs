# Can you convert a lumerical script file to Tidy3D?

| Date       | Category    |
|------------|-------------|
| 2023-10-24 19:16:52 | Uncategorized |


We offer a limited ability to convert Lumerical .lsf project files to
Tidy3D skeleton files in python. This can be done with the command
`tidy3d convert lumerical_project.lsf tidy3d_script.py`. This is an
experimental feature, and not every command in lsf is covered, and lsf
project files often have default values/conventions that are not
specified, so the created Tidy3D script will often need additional
specification. Always be sure to check over the created Tidy3D script to
see if there are any values missing or if any Lumerical objects have not
been parsed.

