---
title: "How do I save or load a\_tidy3d.web.Batch\_so I can work with it later?"
date: 2023-12-04 20:12:20
enabled: true
category: "Parameter Sweep"
---
<div><div>Like most other Tidy3D objects, <a target="_blank" rel="noopener" href="https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.web.api.container.Batch.html">tidy3d.web.Batch</a> instances have <code>to_file(path)</code> and <code>from_file(path)</code> methods that will export and load their metadata as JSON files. &nbsp;This is especially useful for loading batches for long analysis after they have run. For example, one can save the batch information to file and load the batch later if one needs to disconnect from the service while the jobs are running.</div><div><div markdown class="code-snippet">{% highlight python %}

# Save batch metadata.
batch.to_file("data/batch_data.json")

# Load batch metadata into a new batch.
loaded_batch = web.Batch.from_file("data/batch_data.json")

{% endhighlight %}
{% include copy-button.html %}</div><p> </p></div></div>
