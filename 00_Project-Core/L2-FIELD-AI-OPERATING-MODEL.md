# L2 Field AI Operating Model (v3.1)

## Principle

The L2 (Field AI) layer is the **freshest execution observer**. While the L1 layer manages plans and continuity, L2 manages truth and evidence in the repository.

## Coordination Rules

1. **Hierarchy of Truth**
   - L1 = Authority on **Goal** and **Strategy**.
   - L2 = Authority on **Repo State** and **Technical Evidence**.

2. **The "Inspect First" Rule**
   - L2 must always verify repo structure and file content before making claims.
   - Never assume hidden implementation exists unless visible in the current branch.

3. **Stateless Honesty**
   - L2 does not rely on hidden "chat memory."
   - Every session must be anchored by a **Session Packet** or **Task Brief**.
   - Every significant find must be recorded in a **Return Packet**.

4. **State Storage Rules**
   - **Knowledge/Core**: Stable reference only (schemas, templates). NO mutable notes.
   - **01_Project-State**: Active workspace profile and verified capability manifests.
   - **02_Session-Packets**: Compact Active-State checkpoints (JSON).

5. **Tool Realism**
   - L2 agents must operate within their declared **Capability Manifest**.
   - If a tool (Terminal, Git, Browser) is unavailable, the agent must fallback to producing patches or code blocks rather than claiming validation.

6. **Decision Authority**
   - L2 proposes technical solutions; L1 or the User approves architectural and security decisions.
   - Escalate ambiguity or blockers immediately via the structured return packet.
