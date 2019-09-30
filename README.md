# BioComparator
software toolset to compare biological-models

![Python version badge](https://img.shields.io/badge/python-3.6-blue.svg)
[![license](https://img.shields.io/github/license/LoLab-VU/BioComparator.svg)](LICENSE)
![version](https://img.shields.io/badge/version-0.1.0-orange.svg)
[![release](https://img.shields.io/github/release-pre/LoLab-VU/BioComparator.svg)](https://github.com/LoLab-VU/BioComparator/releases/tag/v0.1.0)


**BioComparator** is a python toolkit designed to compare
different versions of a biological model, principally employing parameter estimation and model selection methodologies to differentiate the different versions of a model. **BioComparator** is designed to be compatible with the
[PySB](http://pysb.org/) modeling framework.

 provides an easy to use interface for model calibration/parameter estimation using an implementation of continuous genetic algorithm-based optimization. Its functionality and API were designed to be familiar to users of the [PyDREAM](https://github.com/LoLab-VU/PyDREAM), [simplePSO](https://github.com/LoLab-VU/ParticleSwarmOptimization), and [Gleipnir](https://github.com/LoLab-VU/Gleipnir) packages.

------

# Install

| **! Warning** |
| :--- |
|  BioComparator is still under heavy development and may rapidly change. |

**BioComparator** installs as the `biocomparator` package. It is compatible (i.e., tested) with Python 3.6.

Note that `biocomparator` has the following core dependencies:
   * [NumPy](http://www.numpy.org/)
   * [pandas](https://pandas.pydata.org/)
   * [PySB](http://pysb.org/)
   * [simplePSO](https://github.com/LoLab-VU/ParticleSwarmOptimization)
   * [swarm_it](https://github.com/LoLab-VU/swarm_it)

### pip install
You can install the latest release of the `biocomparator` package using `pip` sourced from the GitHub repo:
```
pip install -e git+https://github.com/LoLab-VU/BioComparator/#egg=biocomparator
```
However, this will not automatically install the core dependencies. You will have to do that separately.

------

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

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
