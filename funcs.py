import cirq



def n_adder():
    n = 4
    ctrl = cirq.GridQubit(0, 0)
    a = [cirq.GridQubit(0, i+1) for i in range(n-2)]
    q = [cirq.GridQubit(0, i+n-1) for i in range(n)]
    yield cirq.H(ctrl)
    yield cirq.CNOT(ctrl, q[n-1])
    yield cirq.TOFFOLI(ctrl, q[n-1], q[n-2])
    yield cirq.TOFFOLI(ctrl, q[n-1], a[0])
    yield cirq.TOFFOLI(q[n-2], a[0], a[1]) 
    for i in range(n-4):
        yield cirq.CNOT(a[i+1], q[n-i-3])
        yield cirq.TOFFOLI(a[i+1], q[n-i-3], a[i+2])
    yield cirq.CNOT(a[n-3], q[1])
    yield cirq.TOFFOLI(a[n-3], q[1], q[0])
    for i in range(n-3):
        yield cirq.TOFFOLI(q[i+2], a[n-i-4], a[n-i-3])
    yield cirq.TOFFOLI(ctrl, q[n-1], a[0])
    yield cirq.H(ctrl)
    if m:
        yield cirq.Moment([cirq.measure(ctrl, key = 'a')])

def param_unit():
    """
    Parameterized unitary gate
    """

def param_unit_dag():
    """
    Paramaterized unitary gate dagger
    """
