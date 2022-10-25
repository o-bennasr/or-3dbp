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

## Meramaid-js
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;

```mermaid
graph LR
A[Square Rect] -- Link text --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```
