# How do I save and load any Tidy3D object?

| Date       | Category    |
|------------|-------------|
| 2023-12-03 20:34:44 | Simulations |


You can save/load Tidy3D objects to/from JSON files. If the object <code>obj</code> is an instance of <code>ObjClass</code>, save and load it with <code>obj.to_file(fname='path/to/file.json')</code> and <code>obj = ObjClass.from_file(fname='path/to/file.json')</code>, respectively.
