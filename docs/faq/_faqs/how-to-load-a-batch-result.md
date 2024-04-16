---
title: How to load a batch result?
date: 2023-12-04 18:41:54
enabled: true
category: "Parameter Sweep"
---
When a batch is created, a `batch.hdf5` file will be created automatically. Users can use this file to collect all the simulation results from the batch. First, load the `batch.hdf5` file by

<div><div><div markdown class="code-snippet">{% highlight python %}

batch = web.Batch.from_file(“folder_name/batch.hdf5”)

{% endhighlight %}
{% include copy-button.html %}</div></div></div>

Then download and load all simulations results into a BatchData object by

<div><div><div markdown class="code-snippet">{% highlight python %}

batch_results = batch.load(path_dir=“data”)

{% endhighlight %}
{% include copy-button.html %}</div></div></div>

Then, you can further extract the result for each simulation from `batch_results`.

