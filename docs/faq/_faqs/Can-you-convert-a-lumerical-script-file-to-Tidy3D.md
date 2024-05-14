---
title: Can you convert a lumerical script file to Tidy3D?
date: 2023-10-24 19:16:52
enabled: true
category: "Simulations"
---

[This repo](https://github.com/hirako22/Lumerical-to-Tidy3D-Converter) offers a limited ability to convert `.lsf` project files to Tidy3D skeleton files in Python. Not every command in the `lsf` file is covered. The `lsf` project files often have default values/conventions that are not specified, so the created Tidy3D script will often need additional specification. Always be sure to check over the created Tidy3D script to see if any values are missing or if any objects have not been parsed.

