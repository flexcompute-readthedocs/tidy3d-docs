# Why the simulation time for the exact same simulation can vary?

| Date       | Category    |
|------------|-------------|
| 2023-10-24 14:48:15 | Simulations |



Depending on the size of the simulation task submitted, our cloud always tries to dynamically allocate the optimal amount of computational resources to run this task. When the server is busy, the sources could become limited so a smaller amount of resources are assigned to run the task, making the simulation time slightly longer than usual. However, this should be relatively rare as we constantly monitor the status of our server and ensure ample hardware resources are available at all times.