# BGS AI Agent Workflow

Boundary Governance Suite

Use this when an AI agent is deciding what to do with a software task.
It is a progressive narrowing workflow, not a full planning spec.
The recommendation logic lives in `./DECISION-TREE.md`.

------------------------------------------------------------

1. READ THE TREE
----------------

Read `./DECISION-TREE.md` first.
If it is clear, use it.
If not, ask one clarifying question about the missing boundary or risk.

------------------------------------------------------------

2. USE THE MATRIX
-----------------

If the issue is about AI-specific problems, read the relevant matrix:
- `./AI-PROBLEM-MATRIX-SECURITY.md`
- `./AI-PROBLEM-MATRIX-RELIABILITY.md`
- `./AI-PROBLEM-MATRIX-OPERATIONS.md`
- `./AI-PROBLEM-MATRIX-LEGAL.md`

Use the matrix to identify the problem class and check what BGS already
covers versus what still needs external controls.

------------------------------------------------------------

3. PLAN THE WORK
----------------

Once the relevant slice is clear:
- define the scope
- define the request/result boundary
- define the tests or evidence needed
- define the external controls still required
- define the smallest implementation that improves the code

If the task is still ambiguous after this:
- ask the smallest clarifying question needed to continue

------------------------------------------------------------

4. EXECUTE
----------

Then:
- implement the smallest useful change
- keep the behavior explicit
- keep the contract versioned
- keep the evidence visible
- keep the change auditable

If a later step needs stronger governance:
- expand the BGS slice progressively
- do not jump straight to the full suite unless the problem needs it
