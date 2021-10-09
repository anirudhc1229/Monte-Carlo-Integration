# Monte-Carlo-Integration
I created this brief project in order to learn more about Monte Carlo simulation (and also to keep myself occupied on an otherwise boring day). The program takes as inputs the function to integrate, the lower and upper bounds of integration, and the sample size. It then returns an approximation distribution histogram for the integral's solution, with larger sample sizes obviously leading to more accurate overall tendencies. A sample size of 10000x10000 (which tended to be most optimal) takes less than 3 seconds to compute, thanks to multiprocessing and NumPy.

TODO: Implement a basic Flask frontend
