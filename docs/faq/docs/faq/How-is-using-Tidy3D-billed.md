# How is using Tidy3D billed?

| Date       | Category    |
|------------|-------------|
| 2023-10-24 14:14:41 | About Tidy3D |


The [Tidy3D client](https://pypi.org/project/tidy3d/) that is used for designing simulations and analyzing the results is free and open source. We only bill the run time of the solver on our server, taking only the compute time into account (as opposed to overhead e.g. during uploading). When a task is uploaded to our servers, we will print the maximum incurred cost in FlexCredit. This cost is also displayed in the online interface for that task. This value is determined by the cost associated with simulating the entire time stepping specified. If early shutoff is detected and the simulation completes before the full time stepping period, this cost will be pro-rated. For more questions or to purchase FlexCredit, please contact us at `support@flexcompute.com`. 
