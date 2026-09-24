# Glossary

The stack reuses a handful of ordinary words for very specific things, and a few
of them are reused for *several* specific things. This page is the single
definition each term points back to.

Terms are grouped by what they name. Where a word means more than one thing, every
meaning is listed — the ambiguity is real and naming it is more useful than
pretending one reading wins.

---

## The overloaded ones

### core

Four different things in this stack are called *core*. They are unrelated, and
telling them apart matters:

| Written as | What it is |
|---|---|
| `--role core` | A **node role**. A machine installed with this role runs the coordinating services of a grid. See *node role*. |
| `faigrid-core` | A **hostname on the control network**, the address of the Supervisor's Control API. A name a tenant dials, not a machine. |
| `core-heart` | A **deployment unit** — one stack of coordinating services (database, queue, automation) that a core node runs. |
| `nexus-core`, and names like it | A **host**. Someone's machine, named by them. Carries no meaning in the stack. |

A sentence like "core is down" is ambiguous in four ways. Say which one.

### runner

| Meaning | Where |
|---|---|
| **Runner Pool** — Grid's component that executes jobs in isolation, with resource limits and timeouts | `products/grid` |
| `--role runner` — a node role for a machine that only executes, without coordinating | node roles |
| A CI runner — the agent that executes a forge's pipeline jobs | forge configuration, unrelated to Grid |

The first two are Grid's. The third belongs to the forge and shares only the word.

### node

A machine that has been installed into a grid and carries a **node role**. Not a
Kubernetes node, and not a Docker Swarm node — Grid's notion predates and does not
imply either.

### tenant

An organisation whose workloads run **inside** someone else's grid, isolated at the
network level, with its own identity, routing and cost attribution. A tenant is not
a user and not a team; it is a separate party whose isolation is a security
property rather than a convenience.

---

## Grid

### Supervisor

The service that presents Grid's execution machinery as one addressable thing. It
is the umbrella over the **Scheduler**, the **Runner Pool** and the **Recovery
Engine**, and it exposes them through the **Control API**.

Callers submit jobs to the Supervisor, ask it for status, and read a job's recovery
history from it. Both a tenant's control plane and the OS layer address it the same
way — neither is privileged in how it speaks to Grid.

### Control API

The Supervisor's interface: submit jobs, query status, manage secrets. It is the
only supported way into Grid's execution machinery; the components behind it are
implementation.

### Scheduler

Queue management, priority dispatch and load balancing. Decides *what runs next and
where*. Reached through the Control API, not addressed directly.

### Runner Pool

Isolated execution with resource limits and timeout handling. Decides *nothing* —
it runs what the Scheduler hands it.

### Recovery Engine

Retry policies, circuit breakers and dead letter queues. Owns what happens after a
job fails, including preserving a job's identity across a restart so a caller can
reconcile the two.

### Node role

What a machine does in a grid, chosen at install: `core`, `edge`, `worker`,
`backup`, `external` or `runner`. The role determines which services are installed
and what the machine is expected to contribute, not what it is allowed to see.

### Worker

A node role for a machine that contributes **inference** — typically a local model
served on that machine. Distinct from `runner`, which contributes general job
execution. A worker's model is reached as a provider behind the Gateway, not
addressed directly by callers.

---

## Across the stack

### Gateway (faigate)

The single entry point for model access. Callers ask the Gateway for a model; the
Gateway decides which provider serves it, applies quotas and attributes cost.
Adding a model means adding a provider to the Gateway, never teaching each caller a
new endpoint.

### Provider

One source of model inference behind the Gateway — a hosted API, or a local engine
on a worker node. Providers are interchangeable from a caller's point of view,
which is the point.

---

## Reading the terms together

A worked example, using each word in its one meaning:

> A **tenant** runs its workloads on a **core** node. Its control plane submits work
> to the **Supervisor** through the **Control API**. The **Scheduler** places that
> work on the **Runner Pool**. A step needing a model asks the **Gateway**, which
> routes to a **provider** — possibly a local model on a **worker** node. If a job
> dies, the **Recovery Engine** restarts it and preserves its identity so the tenant
> can reconcile the restart against its own records.

Every noun there is defined above, and each means exactly one thing.
