import sys
sys.path.append('/home/amand/')
from Laplace.laplace.utils.utils import get_nll, validate, parameters_per_layer, invsqrt_precision, _is_batchnorm, _is_valid_scalar, kron, diagonal_add_scalar, symeig, block_diag, expand_prior_precision, normal_samples
from Laplace.laplace.utils.feature_extractor import FeatureExtractor
from Laplace.laplace.utils.matrix import Kron, KronDecomposed
from Laplace.laplace.utils.swag import fit_diagonal_swag_var
from Laplace.laplace.utils.subnetmask import SubnetMask, RandomSubnetMask, LargestMagnitudeSubnetMask, LargestVarianceDiagLaplaceSubnetMask, LargestVarianceSWAGSubnetMask, ParamNameSubnetMask, ModuleNameSubnetMask, LastLayerSubnetMask


__all__ = ['get_nll', 'validate', 'parameters_per_layer', 'invsqrt_precision', 'kron',
		   'diagonal_add_scalar', 'symeig', 'block_diag', 'expand_prior_precision',
		   'FeatureExtractor',
           'Kron', 'KronDecomposed',
		   'fit_diagonal_swag_var',
		   'SubnetMask', 'RandomSubnetMask', 'LargestMagnitudeSubnetMask', 'LargestVarianceDiagLaplaceSubnetMask',
		   'LargestVarianceSWAGSubnetMask', 'ParamNameSubnetMask', 'ModuleNameSubnetMask', 'LastLayerSubnetMask']
