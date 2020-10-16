"""Functions to convert between Mitiq's internal circuit representation and
pytket's circuit representation.
"""
import cirq
import pytket
from pytket.cirq import cirq_to_tk, tk_to_cirq

def to_pytket(circuit: cirq.Circuit) -> pytket.Circuit:
    """Returns a pytket circuit equivalent to the input Mitiq circuit.

    Args:
        circuit: Mitiq circuit to convert to a pytket circuit.

    Returns:
        pytket.Circuit object equivalent to the input Mitiq circuit.
    """
    return cirq_to_tk(circuit)


def from_pytket(circuit: pytket.Circuit) -> cirq.Circuit:
    """Returns a Mitiq circuit equivalent to the input pytket circuit.

    Args:
        circuit: pytket circuit to convert to a Mitiq circuit.

    Returns:
        Mitiq circuit representation equivalent to the input pytket circuit.
    """
    return tk_to_cirq(circuit)
