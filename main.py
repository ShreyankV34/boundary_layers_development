
#### main.py

```python
from simulation.boundary_layer import boundary_layer_simulation
from analysis.analysis import analyze_boundary_layer

if __name__ == "__main__":
    u, x, y = boundary_layer_simulation()
    analyze_boundary_layer(u, x, y)
