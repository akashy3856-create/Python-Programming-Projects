# The brief: logistics

Listen to the Director's note first (`DIRECTOR-NOTE.mp3`). That is the job. This is the paperwork.

1. **What you have.** This folder is the portal: the Flask app, a 100k-row database, a
   simulated SMS gateway. `docker compose up`, then read `README.md`.

2. **What you build.** Two MCP servers over streamable HTTP: one for applicants, one for the
   block officer. Separate endpoints; a citizen's assistant should not even see the officer's
   tools. Whatever APIs you need behind them. The portal stays the system of record.

3. **Your evals, your way.** Invent the citizens yourself. Make each one specific: a name, an
   age, a village, how they talk, what they want, and what must be true in the portal's
   database when the conversation ends. Play them against your assistant, through a real
   client, and check the database afterwards. Put it on a page at `/eval-dashboard` on your
   deployment: the citizens, the conversations, what you checked, what passed. What goes on
   that page is your choice. In your Loom, walk us through the people you invented, why those,
   what your evals found, and what you changed because of them. We test with people of our
   own, in the same spirit, and compare your pass rate with ours.

4. **How we test.** We point a real MCP client, Claude Code running a small model with a
   limited number of turns, at your endpoint. We sign in the way a citizen or an officer would
   on your deployment, play invented citizens, then read your portal to see what is there. We
   also read your `/eval-dashboard`.

5. **Keep it running.** Your own VM, up until the window closes. We may test more than once.

6. **What you submit** (in the application form): your portal URL and MCP endpoint(s); an
   officer login for us; a private GitHub repo named `sewasetu-assistant` with full history,
   `harshnisar` invited, plus a zip of the repo including `.git`; the `/eval-dashboard` URL;
   the Loom the Director asked for (3 minutes, face and screen): what you achieved, the design
   decisions across the two MCPs, your personas and evals and what you learned; and a one-page
   design note: the three decisions that mattered most, and the one you
   would make differently with more time.
