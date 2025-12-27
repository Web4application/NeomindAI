class MPR_sde(par: dict = {}, parbold={})[source]
MPR model

set_initial_state()[source]
check_parameters(par: dict)[source]
get_default_parameters()[source]
prepare_input()[source]
Prepare input parameters for passing to C++ engine.
run(par: dict = {}, x0: ndarray | None = None, verbose: bool = False)[source]
Integrate the MPR model with the given parameters.

Parameters:
pardict
Dictionary of parameters.
x0array_like
Initial condition of the system.
verbosebool
If True, print the progress of the simulation.
Returns:
boldarray_like
Simulated BOLD signal.
class BoldParams(par={})[source]
check_parameters(par)[source]
get_default_parameters()[source]
get_params()[source]
check_sequence(x: int | float | ndarray, n: int)[source]
check if x is a scalar or a sequence of length n

Parameters:
x: scalar or sequence of length n
n: number of nodes
Returns:
x: sequence of length n
set_initial_state(nn, seed=None)[source]
