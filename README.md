## A Mixed Integer programming solution to solve packing one bin
The enviroment is py3dbp python package
The LP solver is Pulp from Coin-OR


## Set up
pip install -r requirements.txt


## Disclaimer
This is a minimilastic approach, solving for one bin. <br />
TODO (): Formulate the problem, and find a way to scale to multi-binsi <br />
TODO (): Add support for rotation, Unloading priority and weight distribution <br />

## Green main
Running pytest in branch main should mark all tests as passed.

## TDD
Only TDD will be accepted to contribute to this repo <br />
I should see the Client code first.

## Model visualization
can be done by mermaid 

```
[//]: # (
```mermaid
graph LR
A((Start)) -- action --> B((S1))
C((S2)) -- action --> B
B -- action --> D((S3))
C -- action --> D
D -- action --> D
```

)
