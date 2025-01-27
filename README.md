# Water Dynamics Analysis in Channel Proteins

Tools for analyzing water molecules within channel proteins, focusing on translational and rotational dynamics.

## 1. Selection of Water in Channel
- **Finding Channel Waters**: Identifies water molecules located within channel proteins.
  - Script: `Finding Channel Water.py`

## 2. Translational Dynamics
- **Z-Coordinate Time Series for OW Atom**: Tracks the Z-coordinate time series for the OW atom in channel waters.
  - Script: `Z(t) For Channel Waters.py`
- **Self-Diffusion Coefficient Calculation**: Computes the self-diffusion coefficient using Einstein's equation.
  - Notebook: `Self Diffusion Coefficient.ipynb`

## 3. Rotational Dynamics
- **Orientational Time Correlation Function**: Analyzes the orientational time correlation function for water molecules.
  - Script: `OrientationalTimeCorrelation Function.py`
- **Angle Orientation Analysis**: Determines the orientation angles between O and H atoms.
  - Notebooks: `m_x + m_y + m_z.ipynb`, `w_x + w_y + w_z.ipynb`
- **Rotational Jump Dynamics**: Examines rotational jump dynamics using the jump definition by Laage and Hynes (Laage, D., & Hynes, J. T. (2006). A molecular jump mechanism of water reorientation. Science, 311(5762), 832-835).
  - Notebook: `Jump_AP_Hynes Definition.ipynb`


## Reference

If using this code for research purposes, please cite:

```bibtex
@article{santra2021structural,
  title={Structural and dynamical heterogeneity of water trapped inside Na+-pumping KR2 rhodopsin in the dark state},
  author={Santra, Mantu and Seal, Aniruddha and Bhattacharjee, Kankana and Chakrabarty, Suman},
  journal={The Journal of Chemical Physics},
  volume={154},
  number={21},
  year={2021},
  publisher={AIP Publishing}
}
