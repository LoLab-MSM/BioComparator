# BioComparator
Rapidly compare biological models written in PySB using particle swarm optimization-based model fitting and model selection metrics.

![Python version badge](https://img.shields.io/badge/python-3.6-blue.svg)
[![license](https://img.shields.io/github/license/LoLab-VU/BioComparator.svg)](LICENSE)
![version](https://img.shields.io/badge/version-0.2.0-orange.svg)
[![release](https://img.shields.io/github/release-pre/LoLab-VU/BioComparator.svg)](https://github.com/LoLab-VU/BioComparator/releases/tag/v0.2.0)


**BioComparator** is a Python software tool designed to compare biological models encoded using the [PySB](http://pysb.org/) modeling framework. Candidate models may for example encode different mechanistic hypotheses or represent different granularities of a biological mechanism. Principally, the tool employs parameter estimation to the set of candidate models with respect to a common data-set (or set of data-sets) via a common cost function. **BioComparator** then provides users with a set of comparative metrics such as the minimum cost and Akaike Information Criterion, allowing users to easily evaluate candidate models' fit to the data and the trade offs between the fit to data and model size/complexity.

Currently, **BioComparator** uses particle swarm optimization-based parameter estimation, via the [simplePSO](https://github.com/LoLab-VU/ParticleSwarmOptimization) package, to minimize a cost function and fit models to a given data-set. In the future, interfaces may be added for other model calibration/parameter estimation tools, such as [Gleipnir](https://github.com/LoLab-VU/Gleipnir) (Bayesian parameter estimation and model evidence via Nested Sampling).

------

# Install

**BioComparator** installs as the `biocomparator` package. It is compatible (i.e., tested) with Python 3.6.

Note that `biocomparator` has the following core dependencies:
   * [NumPy](http://www.numpy.org/)
   * [pandas](https://pandas.pydata.org/)
   * [PySB](http://pysb.org/)
   * [simplePSO](https://github.com/LoLab-VU/ParticleSwarmOptimization)
   * [swarm_it](https://github.com/LoLab-VU/swarm_it)

### pip install
You can install the latest (possibly unreleased) version of the `biocomparator` package using `pip` sourced from the GitHub repo:
```
pip install -e git+https://github.com/LoLab-VU/BioComparator/#egg=biocomparator
```
However, this will not automatically install the core dependencies. You will have to do that separately.

You can also install the latest release (currently v0.2.0) version of the `biocomparator` package using `pip` sourced from the GitHub repo with an additional release tag:
```
pip install -e git+https://github.com/LoLab-VU/BioComparator/#egg=biocomparator@v0.2.0
```
You may check the [BioComparator releases page](https://github.com/LoLab-VU/Gleipnir/releases/) to find all available releases.

------

# License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details

------

# Documentation and Usage

### Quick Overview
Principally, **BioComparator** defines the **BioComparator** class,
```python
from biocomparator import BioComparator
```
which defines an object that can be used setup and run Particle Swarm Optimization (PSO)-based parameter estimation and subsequent Akaike Information Criterion (AIC)-based model selection of PySB models.


### Examples
Additional example scripts that show how to setup and launch comparison runs using **BioComparator** can be found under [examples](./examples).

------

# Contact

To report problems or bugs please open a
[GitHub Issue](https://github.com/LoLab-VU/BioComparator/issues). Additionally, any comments, suggestions, or feature requests for **BioComparator** can also be submitted as a [GitHub Issue](https://github.com/LoLab-VU/BioComparator/issues).

------

# Citing

If you use the **BioComparator** software in your research, please cite the GitHub repo.

Also, please cite the following references as appropriate for software used with/via **BioComparator**:

#### Packages from the SciPy ecosystem

These include NumPy and pandas for which references can be obtained from:
https://www.scipy.org/citing.html

#### PySB
  1. Lopez, C. F., Muhlich, J. L., Bachman, J. A. & Sorger, P. K. Programming biological models in Python using PySB. Mol Syst Biol 9, (2013). doi:[10.1038/msb.2013.1](dx.doi.org/10.1038/msb.2013.1)

#### simplePSO
You can export simplePSO reference from its Zenodo DOI entry: [10.5281/zenodo.2612912](https://doi.org/10.5281/zenodo.2612912).

#### swarm_it
Cite the GitHub repo: [https://github.com/LoLab-VU/swarm_it](https://github.com/LoLab-VU/swarm_it)
