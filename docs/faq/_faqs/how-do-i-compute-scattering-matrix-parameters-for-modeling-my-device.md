---
_schema: default
title: How do I compute scattering matrix parameters for modeling my device?
date: 2023-12-20 16:57:31
enabled: true
category: Scattering Matrix
_inputs:
  title:
    type: text
    label: QUESTION TITLE
  enabled:
    type: switch
    hidden: true
  date:
    type: datetime
    label: DATE
    instance_value: NOW
  category:
    type: select
    options:
      values: data.faq_categories
      value_key: key
      preview:
        text:
          - key: category_name
---
To compute scattering matrix parameters, you need to create a base [tidy3d.Simulation](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.Simulation.html){: target="_blank" rel="noopener"}&nbsp;(without the modal sources or monitors used to compute S-parameters) and include&nbsp;[tidy3d.plugins.smatrix.Port](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.smatrix.Port.html){: target="_blank" rel="noopener"} objects. These ports will be converted into modal sources&nbsp; and monitors later, so they require a mode specification and a definition of the direction that points into the system. You should also give them names to refer to later. For example:

<div markdown class="code-snippet">{% highlight python %}
from tidy3d.plugins.smatrix.smatrix import Port

num_modes = 1

# Port definition.
port_right_top = Port(
  center=[-5, 3, 0],
  size=[0, 4, 2],
  mode_spec=tidy3d.ModeSpec(num_modes=num_modes),
  direction="-",
  name="right_top",
)

{% endhighlight %}
{% include copy-button.html %}</div>



Next, add the base simulation and ports to the [tidy3d.plugins.smatrix.ComponentModeler](https://docs.flexcompute.com/projects/tidy3d/en/latest/api/_autosummary/tidy3d.plugins.smatrix.ComponentModeler.html){: target="_blank" rel="noopener"}, along with the frequency of interest and a name for saving the batch of simulations that will get created later.

<div markdown class="code-snippet">{% highlight python %}
from tidy3d.plugins.smatrix.smatrix import ComponentModeler

modeler = ComponentModeler(
  simulation=sim,
  ports=ports,
  freqs=[freq0],
  verbose=True
)

modeler.plot_sim(z=0)

{% endhighlight %}
{% include copy-button.html %}</div>



With the component modeler defined, you should call it's&nbsp;`.solve()`&nbsp;method to run a batch of simulations to compute the S matrix. The tool will loop through each port and create one simulation per mode index (as defined by the mode specifications), where a unique modal source is injected. Each of the ports will also be converted to mode monitors to measure the mode amplitudes and normalization.

<div markdown class="code-snippet">{% highlight python %}
from tidy3d.plugins.smatrix.smatrix import Port

smatrix = modeler.run(path_dir="data")

{% endhighlight %}
{% include copy-button.html %}</div>



The scattering matrix returned by the solve is an xr.DataArray relating the port names and mode indices. For example&nbsp;`smatrix.loc[dict(port_in=name1, mode_index_in=mode_index1, port_out=name2, mode_index_out=mode_index_2)]`&nbsp;gives the complex scattering matrix element.

See this [tutorial](https://www.flexcompute.com/tidy3d/examples/notebooks/SMatrix/) for more details on computing the scattering matrix.