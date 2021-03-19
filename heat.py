import cirq
import numpy

def had_test(operator, squig):
    ctrl = cirq.GridQubit(0,0)
    q = [cirq.GridQubit(0, i+1) for i in range(4)]

    circuit = cirq.Circuit()

    circuit.append(cirq.H(ctrl))
    circuit.append(cirq.param_unit().controlled_by(ctrl))
    circuit.append(operator.controlled_by(ctrl))
    if squig:  
        circuit.append(cirq.param_unit_dag().controlled_by(ctrl))
    circuit.append(cirq.H(ctrl))
    circuit.append(cirq.measure(ctrl))

    return circuit


"""
C(l0,l) = l^2 + L^2(1 - 2*tau*term1 + tau^2 * term2) - 2*l*L*term3
"""

###TERM 3: (1 + 2*tau*4^n)*Re(<Psi~|Psi>) - tau*4^n*Re(<Psi~|A|Psi>) - tau*4^n*Re(<Psi~|Adag|Psi>)
####     = subterm1 + subterm2 + subterm3


def compute_cost(l0, l_squig):
    circut1 = had_test(identity, True)
    circuit2 = had_test(adder, True)
    circuit3 = had_test(adder_dag, True)
    #have to figure out simulation to get value
    term3 = (1 + 2*tau*4^4)*(circuit1_val) + tau*4^4*(circuit2_val) - tau*4^4*(circuit3_val)

    circuit4 = had_test(adder, False)
    term1 = 4^4*(2*circuit4_val - 2)

    circuit5 = had_test(adder_squared, False)
    circuit6 = had_test(adder, False)
    term2 = 4^8*(2*circuit5_val - 8*circuit6_val +6)

    cost = l_squig^2 + l_0^2*(1 - 2*tau*term1 + tau^2 * term2 - 2*l0*l_squig*term3)
    return cost


##minimize cost with respect to parameters
##apply new parameterized unitary gate to quantum register to obtain u(t + tau)