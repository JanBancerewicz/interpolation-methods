# Analysis of Interpolation Methods for Altitude Profiles

## Project Overview

This project involves the implementation and analysis of numerical interpolation methods applied to the approximation of altitude profiles for various tourist routes. The ability to accurately determine intermediate heights along a path, based on a limited set of known data points, is crucial for numerous applications, including route planning, geographical analysis, and simulation.

The project was completed as part of the **Numerical Methods** course.

## Report

A detailed description of the algorithms, interpretation of results, and diagrams are available in [Interpolation_methods.pdf](./Interpolation_methods.pdf) (in Polish).

## What are the Interpolation Methods Used?

This project investigates three primary interpolation techniques:

* **Lagrange Polynomial Interpolation (Equidistant Nodes)**: This classical method constructs a single polynomial that passes through all selected data points. When using equidistant nodes, it is prone to the Runge phenomenon, especially with a higher number of nodes.
* **Lagrange Polynomial Interpolation (Chebyshev Nodes)**: To mitigate the undesirable oscillations of the Runge phenomenon, this approach utilizes Chebyshev nodes, which are distributed non-uniformly, with a higher concentration towards the boundaries of the interpolation interval.
* **Cubic Spline Interpolation**: This method employs piecewise cubic polynomials (splines) to interpolate data. Splines are designed to ensure smoothness by maintaining continuity of the function and its first and second derivatives at the connection points (nodes), making them highly robust against oscillations.

## Requirements

* Python 3.x
* `pandas`
* `numpy`
* `matplotlib`

You can install the necessary libraries using pip:

```bash
pip install requirements.txt
```

## How to Run
1. Assure the input data files (`mont_blanc_hike.txt, teide_hike.txt`) are in the `data/` directory.

2. Execute the main script:

```bash
python main.py
```

The script will automatically perform interpolation analysis for both specified routes ("Tour du Mont Blanc" and "Pico del Teide volcano tour") across all three implemented methods and for varying numbers of interpolation nodes (6, 12, 24, 48). All generated plots, including the original path, chosen nodes, and the interpolated path, will be saved to the diagrams/ folder and displayed.

## Program Objective
The Python scripts in this project are designed to:

- Load and preprocess raw altitude data, including normalization to a 0-100% scale.
- Implement and apply Lagrange polynomial interpolation using both equidistant and Chebyshev node distributions.
- Implement and apply cubic spline interpolation for altitude profiles.
- Generate clear and informative plots to visualize the original data, selected interpolation nodes, and the resulting interpolated curves.
- Enable a comparative analysis of the interpolation methods, highlighting their strengths, weaknesses, and suitability for different types of topographical data.