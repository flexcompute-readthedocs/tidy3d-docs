---
_schema: default
title: How do I export the final inverse design structure to GDS?
date: 2023-12-21 23:19:25
enabled: true
category: Inverse Design
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
<div><p>After performing adjoint inverse designs using the <code>adjoint</code> plugin, you can export the final structure to <code>GDS</code> files using the function <code>.to_gds_file()</code>.</p><div markdown class="code-snippet">{% highlight python %}
from tidy3d.plugins.adjoint.utils.penalty import RadiusPenalty

# Convert the final adjoint simulation to a regular one.
sim_final = sim_adj.to_simulation()[0]

# Export the final simulation to GDS.
sim_final.to_gds_file(fname="inverse_design.gds", z=0, permittivity_threshold=6, frequency=200e14)

{% endhighlight %}
{% include copy-button.html %}</div><p> </p></div>

<div> </div>

<div> </div>