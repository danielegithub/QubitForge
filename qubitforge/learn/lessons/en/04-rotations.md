# Phases and rotations

H, X and Z are special cases: you can rotate by any angle.
Angles accept pi, e.g. pi/2 or 2*pi/3.

  1. qreg 1
  2. ry pi/3 0     rotate 60° around Y
  3. bloch 0       watch the vector move
  4. probs         P(1) = sin²(θ/2) = 25%
  5. rz pi/2 0     changes only the phase: probabilities stay the same
  6. h 0           but now the phase shows up after an H!
  7. probs

Key idea: a phase is invisible if you measure right away, but it
affects everything that comes after.
