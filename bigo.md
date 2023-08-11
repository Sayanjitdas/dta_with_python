### big O notation
---

- **What is BigO?**
It is a way to mathematically compare efficiency between two sets of code which does the same work.

- **Time and space complexity**
BigO calculation is based on Time and space complexity. Time complexity is the amount of time a piece
of code consume to complete it's intended work and space complexity is the amount space (in computer memory)
it consume to complete it's intended work.
Time complexity is not measured in normal time unit cause a piece of code can take a minute to run a slow computer
but it can a take just few sec to run on a more powerful computer, this doesn't mean the piece of code has improved
so it is measured based on the no.of operations it does to complete it's intended work.
Depending on what is the purpose behind a particular piece of code we decide which is more important Time or space 
or we find a middle ground where both of them are optimized.

- **Categories of bigO cases (best,average,worst)**
There are basically three cases where Time and space complexity false for a piece of code.

***Best case (sigma)***
the time space complexity in a best case scenario is how many least operation the piece of code did to reach the intended result 
for e.g. in a list `[1,2,3,4,5,7]` to find element `1` it takes only one operation so it is a best case scenario.

***average case (theta)***
the time space complexity in a average case scenario is how many operation the piece of code did to reach the intended result 
for e.g. in a list `[1,2,3,4,5,7]` to find element `4` it takes only 4 operation so it is a average case scenario.

***worst case (O)***
the time space complexity in a worst case scenario is the most operation the piece of code did to reach the intended result 
for e.g. in a list `[1,2,3,4,5,7]` to find element `7` it takes 7 operation so it is a worst case scenario.

> mostly we deal with BigO which is the worst case scenario..


- ***BigO(n)***
This is the linear case scenario where n is the number operation it takes to reach the intended result.
> BigO(2n) is similar to BigO(n) as we always drop the constant C in this case C = 2. We also drop the non dominant as well i.e we only consider highest order. For e.g in equation n^3 + 2n + n we will only consider n^3 as it has the highest order.


- ***BigO(n^2)***
This is the exponential case scenario where n * n number operation occurs to reach the intended result.

- ***BigO(logn)***
This is the 2nd best case scenario ater BigO(1) where we have the least amount of operation to reach the result.

- ***BigO(1)***
This is the scenario where how to big the input n is the operation will always be a constant number.
for e.g. in case of a function which adds two number in that if we pass n as a parameter how big the n can be
we do only one addition operation.