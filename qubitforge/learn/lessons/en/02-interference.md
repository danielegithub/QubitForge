# Interference

Amplitudes carry a sign (a phase): they can add up or cancel out.
This is the real engine of quantum computing.

  1. qreg 1
  2. h 0           50/50 superposition
  3. h 0           H again: the amplitudes of |1> cancel!
  4. state         you are back to |0> with 100%

Now put a phase in the middle:
  5. reset  →  h 0  →  z 0  →  h 0  →  state
     Z flips the sign of |1>, so the second H now leads to |1>.

Without Z the two paths to |1> interfere destructively.
With Z they interfere constructively.
