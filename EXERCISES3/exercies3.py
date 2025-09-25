# -------------------------------
# Project 80: Stack and Queue Tasks
# -------------------------------

from collections import deque

print("=== STACK QUESTIONS ===")

# -------------------------------
# Practical 1 (Rwanda)
# UR pushes ["Course1", "Course2", "Course3"]. Undo all. Which remains?
# -------------------------------
stack = []
stack.append("Course1")
stack.append("Course2")
stack.append("Course3")

print("\nPractical 1:")
print("Initial stack:", stack)

# Undo all (pop all)
stack.pop()
stack.pop()
stack.pop()

print("After undo all:", stack)   # should be empty


# -------------------------------
# Practical 2 (Rwanda)
# In Irembo, push ["Step1", "Step2", "Step3"]. Undo 1. Which is left?
# -------------------------------
stack = []
stack.append("Step1")
stack.append("Step2")
stack.append("Step3")

print("\nPractical 2:")
print("Initial stack:", stack)

stack.pop()   # undo 1
print("After undo 1:", stack)     # Step1, Step2 remain


# -------------------------------
# Challenge
# Push ["X", "Y", "Z"], pop one, push "W". Which is top?
# -------------------------------
stack = []
stack.append("X")
stack.append("Y")
stack.append("Z")

stack.pop()        # removes Z
stack.append("W")  # push W

print("\nChallenge (Stack):")
print("Final stack:", stack)
print("Top element:", stack[-1])  # should be W


# -------------------------------
# Reflection
# (No code, theory only)
# -------------------------------
print("\nReflection (Stack): A stack is LIFO (Last In, First Out). "
      "This means the last item pushed is the first removed, "
      "which naturally reverses sequences.")


print("\n=== QUEUE QUESTIONS ===")

# -------------------------------
# Practical 1 (Rwanda)
# At Nyabugogo, 10 buses queue. After 5 depart, who is front?
# -------------------------------
queue = deque(["Bus1", "Bus2", "Bus3", "Bus4", "Bus5",
               "Bus6", "Bus7", "Bus8", "Bus9", "Bus10"])

print("\nPractical 1:")
print("Initial queue:", list(queue))

for _ in range(5):  # 5 buses leave
    queue.popleft()

print("After 5 depart, front is:", queue[0])   # should be Bus6


# -------------------------------
# Practical 2 (Rwanda)
# At CHUK, 8 patients queue. Who is served last?
# -------------------------------
queue = deque(["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"])

print("\nPractical 2:")
print("Initial queue:", list(queue))
print("Last to be served:", queue[-1])  # should be P8


# -------------------------------
# Challenge
# Queue vs stack for lunch line. Which is fair?
# -------------------------------
queue = deque(["Student1", "Student2", "Student3"])
stack = ["Student1", "Student2", "Student3"]

print("\nChallenge (Queue vs Stack):")
print("Queue order (fair):", list(queue))
print("Stack order (unfair):", stack)


# -------------------------------
# Reflection
# (No code, theory only)
# -------------------------------
print("\nReflection (Queue): FIFO (First In, First Out) ensures fairness "
      "because the first person to arrive is the first served. "
      "No one can jump ahead in line.")